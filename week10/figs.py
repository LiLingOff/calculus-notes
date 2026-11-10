"""產生 Week 10 的圖：python week10/figs.py"""
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


# 1. FTC II：F(x) 是累積面積，多走 h 多出一條細長條
F = lambda x: 1.2 + 0.6 * math.sin(1.1 * x) + 0.15 * x
c, x, h = 0.5, 2.6, 0.45
p = Plot((-0.3, 4.4), (-0.3, 2.6), width=420)
region(p, under(F, c, x), BLUE, 0.25)
region(p, under(F, x, x + h), ORANGE, 0.45)
p.axes(xticks=[(c, "c"), (x, "x"), (x + h, "x+h")], yticks=[])
p.func(F, xr=(0, 4.2), color=RED)
p.text((c + x) / 2, 0.55, "F(x)", color=BLUE, anchor="middle", size=17)
p.text(x + h / 2, F(x + h / 2) + 0.4, "≈ f(x)·h", color=ORANGE, anchor="middle")
p.text(4.15, F(4.15), "y = f(t)", color=RED, italic=True, anchor="end", dy=-12)
p.save(out("fig-accum.svg"))

# 2. 題 11：x²|x−1| 在 [−1,3]
G = lambda t: t * t * abs(t - 1)
p = Plot((-1.5, 3.5), (-1.5, 19.5), width=360, height=300, equal=False)
region(p, under(G, -1, 1), GREEN, 0.3)
region(p, under(G, 1, 3), BLUE, 0.3)
p.axes(xticks=[(-1, "−1"), 1, 3], yticks=[6, 12, 18])
p.func(G, xr=(-1.3, 3.2), color=RED)
p.text(-0.2, 2.6, "2/3", color=GREEN, anchor="middle")
p.text(2.45, 4.5, "34/3", color=BLUE, anchor="middle")
p.text(3.1, 18.5, "y = x²|x − 1|", color=RED, italic=True, anchor="end")
p.save(out("fig-abs.svg"))

# 3. 題 14：FTC I 用錯的兩個例子
p = Plot((-2.4, 1.6), (-0.5, 6), width=320, height=300, equal=False)
p.axes(xticks=[(-2, "−2"), 1], yticks=[])
p.func(lambda t: t ** -4 if abs(t) > 0.05 else float("nan"), xr=(-2.2, -0.02), color=RED)
p.func(lambda t: t ** -4 if abs(t) > 0.05 else float("nan"), xr=(0.02, 1.4), color=RED)
p.text(0.15, 5.4, "y = x⁻⁴", color=RED, italic=True)
p.text(-1.2, 2.5, "x = 0 處爆掉", color=GRAY, anchor="middle", size=12)
p.save(out("fig-xm4.svg"))

S2 = lambda t: 1 / math.cos(t) ** 2 if abs(math.cos(t)) > 0.05 else float("nan")
p = Plot((-0.4, 3.6), (-0.5, 6), width=320, height=300, equal=False)
p.vline(math.pi / 2, color=GRAY, dash=True, width=1.2)
p.axes(xticks=[(math.pi / 2, "π/2"), (math.pi, "π")], yticks=[1])
p.func(S2, xr=(0, math.pi / 2 - 0.01), color=RED)
p.func(S2, xr=(math.pi / 2 + 0.01, math.pi), color=RED)
p.text(2.3, 5.4, "y = sec²x", color=RED, italic=True)
p.save(out("fig-sec2.svg"))

print("ok")
