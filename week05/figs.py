"""產生 Week 5 的圖：python week05/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


# 1. 題 1：x² + 3y³ = 12 在 (3, 1) 的切線
p = Plot((-4.4, 4.4), (-0.6, 2.4), width=440)
p.axes(xticks=[-4, -3, -2, -1, 1, 2, 3, 4], yticks=[1, 2])
p.func(lambda x: cbrt((12 - x * x) / 3), color=BLUE, n=1600)
p.line(-2 / 3, 3, 1, color=RED)
p.point(3, 1, color=RED)
p.text(-2.2, 1.9, "x² + 3y³ = 12", color=BLUE, italic=True, anchor="middle")
p.text(3, 1, "(3, 1)", color=RED, dx=6, dy=-10)
p.text(3.4, 0.3, "切線斜率 −2/3", color=RED, anchor="end")
p.save(out("fig-implicit.svg"))

# 2. tan y = x 的直角三角形
p = Plot((-0.3, 3.4), (-0.5, 2.5), width=340, pad=10)
A, B, C = (0, 0), (3, 0), (3, 2)
p.segment(*A, *B, color=BLUE, width=2)
p.segment(*B, *C, color=BLUE, width=2)
p.segment(*A, *C, color=BLUE, width=2)
p.segment(2.8, 0, 2.8, 0.2, color=GRAY, width=1.2)
p.segment(2.8, 0.2, 3, 0.2, color=GRAY, width=1.2)
p.text(0.55, 0.12, "y", color=RED, italic=True)
p.text(1.5, 0, "1", anchor="middle", dy=20)
p.text(3, 1, "x", italic=True, dx=8, dy=5)
p.text(1.35, 1.1, "√(1 + x²)", anchor="end", dx=-4, dy=-6)
p.save(out("fig-triangle.svg"))

# 3. (1 + 1/x)^x 往 e 靠近
g = lambda x: (1 + 1 / x) ** x if x > 0 or x < -1 else None
p = Plot((-12, 12), (0, 4.6), width=440, height=260, equal=False)
p.axes(xticks=[-10, -5, 5, 10], yticks=[1, 2, (math.e, "e"), 4])
p.segment(-12, math.e, 12, math.e, color=GRAY, width=1.2, dash=True)
p.func(g, xr=(0.02, 12), color=BLUE, n=1200)
p.func(g, xr=(-12, -1.02), color=BLUE, n=1200)
p.text(8.5, 2.2, "y = " + sup("(1 + 1/x)", "x"), color=BLUE, italic=True, anchor="middle")
p.save(out("fig-e-limit.svg"))

# 4. 題 21：f(x) = 2x + eˣ 與反函數，切線斜率互為倒數
F = lambda x: 2 * x + math.exp(x)


def inv(y):
    lo, hi = -50.0, 50.0
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if F(m) < y else (lo, m)
    return lo


y0 = 2 + math.e
p = Plot((-2.6, 6), (-2.6, 6), width=420)
p.axes(xticks=[-2, 2, 4], yticks=[-2, 2, 4])
p.func(lambda x: x, color=GRAY, width=1.2, dash=True)
p.func(F, color=BLUE)
p.func(inv, color=GREEN, n=600)
p.line(2 + math.e, 1, y0, color=RED, width=1.4)
p.line(1 / (2 + math.e), y0, 1, color=ORANGE, width=1.4)
p.point(1, y0, color=BLUE)
p.point(y0, 1, color=GREEN)
p.text(1, y0, "(1, 2+e)", color=BLUE, dx=10, dy=5)
p.text(y0, 1, "(2+e, 1)", color=GREEN, dy=20, anchor="middle")
p.text(-0.4, 4.9, "y = f(x)", color=BLUE, italic=True, anchor="end")
p.text(5.9, 2.25, sup("y = f", "−1") + "(x)", color=GREEN, italic=True, anchor="end")
p.text(5.9, 5.6, "y = x", color=GRAY, italic=True, anchor="end")
p.save(out("fig-inverse.svg"))

print("ok")
