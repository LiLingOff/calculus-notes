"""產生 Week 16-1 的圖：python week16-1/figs.py"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, _f, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


def band(p, x1, x2, y1, y2, color, opacity=0.15):
    p.items.append(f'<rect x="{_f(p.X(x1))}" y="{_f(p.Y(y2))}" width="{_f(p.X(x2) - p.X(x1))}" '
                   f'height="{_f(p.Y(y1) - p.Y(y2))}" fill="{color}" fill-opacity="{opacity}" '
                   f'clip-path="url(#clip)"/>')


# 1. ε-δ：f(x)=x² 在 x=2，ε=1.2，δ=ε/5=0.24
eps, d = 1.2, 0.24
p = Plot((-0.3, 3.3), (-0.6, 9.5), width=420, height=320, equal=False)
band(p, -0.3, 3.3, 4 - eps, 4 + eps, ORANGE, 0.18)
band(p, 2 - d, 2 + d, -0.6, 9.5, BLUE, 0.16)
p.axes(xticks=[2], yticks=[4])
p.func(lambda t: t * t, xr=(0, 3.1), color=BLUE)
p.func(lambda t: t * t, xr=(2 - d, 2 + d), color=RED, width=3.4)
p.segment(-0.3, 4 + eps, 3.3, 4 + eps, color=ORANGE, dash=True, width=1.2)
p.segment(-0.3, 4 - eps, 3.3, 4 - eps, color=ORANGE, dash=True, width=1.2)
p.text(0.05, 4 + eps + 0.3, "4 + ε", color=ORANGE)
p.text(0.05, 4 - eps - 0.75, "4 − ε", color=ORANGE)
p.text(2, 8.8, "2 − δ ～ 2 + δ", color=BLUE, anchor="middle")
p.text(2.9, 7.2, "y = x²", color=BLUE, italic=True, anchor="end")
p.save(out("fig-epsdelta.svg"))

# 2. ε-K：f(x)=1/x，ε=0.25，K=4
eps, K = 0.25, 4
p = Plot((-0.4, 9.5), (-0.5, 1.6), width=440, height=260, equal=False)
band(p, -0.4, 9.5, -eps, eps, ORANGE, 0.18)
band(p, K, 9.5, -0.5, 1.6, BLUE, 0.12)
p.axes(xticks=[K], yticks=[1])
p.func(lambda t: 1 / t, xr=(0.62, 9.5), color=BLUE)
p.func(lambda t: 1 / t, xr=(K, 9.5), color=RED, width=3.4)
p.segment(-0.4, eps, 9.5, eps, color=ORANGE, dash=True, width=1.2)
p.text(6.8, eps + 0.08, "ε", color=ORANGE)
p.text(4.1, 1.35, "x > K = 1/ε", color=BLUE)
p.text(1.1, 1.2, "y = 1/x", color=BLUE, italic=True)
p.save(out("fig-epsK.svg"))

# 3. |x|/x：寬 1 的帶子蓋不住 1 和 −1
p = Plot((-2.2, 2.2), (-1.8, 1.8), width=380, height=260, equal=False)
band(p, -2.2, 2.2, 0.5, 1.5, ORANGE, 0.18)
p.axes(xticks=[], yticks=[(1, "1"), (-1, "−1")])
p.segment(0, 1, 2.2, 1, color=BLUE, width=2.4)
p.segment(-2.2, -1, 0, -1, color=BLUE, width=2.4)
p.point(0, 1, color=BLUE, open=True)
p.point(0, -1, color=BLUE, open=True)
p.text(-2.1, 1.25, "猜 L = 1，帶寬 2ε = 1", color=ORANGE, size=13)
p.text(-1.1, -0.65, "左邊永遠在帶外", color=RED, anchor="middle", size=13)
p.save(out("fig-sign.svg"))

print("ok")
