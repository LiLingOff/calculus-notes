"""產生 Week 14 的圖：python week14/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


# 1. 1/(x²−4) 拆成兩個分式：靠近 x=2 時長得像 (1/4)/(x−2)
f = lambda x: 1 / (x * x - 4) if abs(x * x - 4) > 1e-9 else None
g = lambda x: 0.25 / (x - 2) if abs(x - 2) > 1e-9 else None
h = lambda x: -0.25 / (x + 2) if abs(x + 2) > 1e-9 else None
p = Plot((-4.5, 4.5), (-2.2, 2.2), width=440, height=260, equal=False)
p.vline(2, color=GRAY, dash=True, width=1)
p.vline(-2, color=GRAY, dash=True, width=1)
p.axes(xticks=[(-2, "−2"), 2], yticks=[1, (-1, "−1")])
p.func(g, color=RED, dash=True, width=1.6)
p.func(h, color=GREEN, dash=True, width=1.6)
p.func(f, color=BLUE)
p.text(2.25, 1.9, "1/(x²−4)", color=BLUE)
p.text(2.6, 0.55, "¼/(x−2)", color=RED)
p.text(-4.4, 0.45, "−¼/(x+2)", color=GREEN)
p.save(out("fig-pf.svg"))

# 2. 萬能變換的幾何：從 (−1,0) 連到 (cos x, sin x) 的直線斜率是 tan(x/2)
X = 1.0
cx, sy = math.cos(X), math.sin(X)
p = Plot((-1.45, 1.45), (-1.25, 1.35), width=340)
p.axes(xticks=[], yticks=[])
p.func(lambda x: math.sqrt(max(0, 1 - x * x)), xr=(-1, 1), color=GRAY, width=1.4)
p.func(lambda x: -math.sqrt(max(0, 1 - x * x)), xr=(-1, 1), color=GRAY, width=1.4)
p.segment(0, 0, cx, sy, color=BLUE, width=1.8)
p.segment(-1, 0, cx, sy, color=RED, width=2)
p.segment(cx, 0, cx, sy, color=GRAY, dash=True, width=1.2)
p.point(-1, 0, color=RED)
p.point(cx, sy, color=BLUE)
p.point(0, 0, color=GRAY, r=3)
p.text(0.2, 0.07, "x", color=BLUE, italic=True)
p.text(-0.72, 0.06, "x/2", color=RED, italic=True)
p.text(cx + 0.06, sy + 0.08, "(cos x, sin x)", color=BLUE)
p.text(-1.42, -0.2, "(−1, 0)", color=RED)
p.text(-0.95, 0.95, "斜率 t = tan(x/2)", color=RED)
p.save(out("fig-weier.svg"))

print("ok")
