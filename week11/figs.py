"""產生 Week 11 的圖：python week11/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, _f, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


def region(p, pts, color, opacity=0.28):
    d = "M" + " L".join(f"{_f(p.X(x))},{_f(p.Y(y))}" for x, y in pts) + " Z"
    p.items.append(f'<path d="{d}" fill="{color}" fill-opacity="{opacity}" stroke="{color}" '
                   f'stroke-width="1" stroke-linejoin="round" clip-path="url(#clip)"/>')


def under(f, a, b, n=200):
    return [(a, 0)] + [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)] + [(b, 0)]


H = math.pi / 2

# 1. King's rule：f(x) 與 f(π/2 − x) 互為鏡像，加起來是 1
C4 = lambda t: math.cos(t) ** 4 / (math.sin(t) ** 4 + math.cos(t) ** 4)
S4 = lambda t: math.sin(t) ** 4 / (math.sin(t) ** 4 + math.cos(t) ** 4)
p = Plot((-0.25, 1.9), (-0.2, 1.35), width=420, height=300, equal=False)
region(p, under(C4, 0, H), BLUE, 0.2)
p.vline(H / 2, color=GRAY, dash=True, width=1.2)
p.segment(0, 1, H, 1, color=GRAY, dash=True, width=1.2)
p.axes(xticks=[(H / 2, "π/4"), (H, "π/2")], yticks=[1])
p.func(C4, xr=(0, H), color=BLUE)
p.func(S4, xr=(0, H), color=RED)
p.text(0.05, 1.12, "cos⁴/(sin⁴+cos⁴)", color=BLUE)
p.text(H, 1.12, "sin⁴/(sin⁴+cos⁴)", color=RED, anchor="end")
p.save(out("fig-king.svg"))

# 2. 題 18：u = x² 在 [−1,1] 上不是一對一
p = Plot((-1.5, 1.5), (-0.3, 1.4), width=360, height=240, equal=False)
p.axes(xticks=[(-1, "−1"), 1], yticks=[1])
p.func(lambda t: t * t, xr=(-1, 0), color=RED)
p.func(lambda t: t * t, xr=(0, 1), color=BLUE)
p.text(-0.95, 0.55, "u 從 1 降到 0", color=RED, size=13)
p.text(0.95, 0.55, "u 從 0 升到 1", color=BLUE, anchor="end", size=13)
p.text(1.05, 1.15, "u = x²", color=GRAY, italic=True)
p.save(out("fig-weird.svg"))

# 3. 題 17：cos⁶/(sin⁶+cos⁶) 在 [0, 2π]，和 sin⁶ 版本面積相同
C6 = lambda t: math.cos(t) ** 6 / (math.sin(t) ** 6 + math.cos(t) ** 6)
S6 = lambda t: math.sin(t) ** 6 / (math.sin(t) ** 6 + math.cos(t) ** 6)
p = Plot((-0.4, 6.9), (-0.25, 1.45), width=460, height=230, equal=False)
region(p, under(C6, 0, 2 * math.pi, 600), BLUE, 0.18)
p.axes(xticks=[(H, "π/2"), (math.pi, "π"), (3 * H, "3π/2"), (2 * math.pi, "2π")], yticks=[1])
p.func(C6, xr=(0, 2 * math.pi), color=BLUE)
p.func(S6, xr=(0, 2 * math.pi), color=RED, dash=True)
p.text(0.1, 1.2, "cos⁶ 版", color=BLUE)
p.text(1.2, 1.2, "sin⁶ 版", color=RED)
p.save(out("fig-q17.svg"))

print("ok")
