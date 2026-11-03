"""產生 Week 6 的圖：python week06/figs.py"""
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


# 1. 題 1：f(x) = 3x e^(2x−10) 在 x = 5 的線性化
F = lambda x: 3 * x * math.exp(2 * x - 10)
p = Plot((4.2, 5.6), (0, 40), width=420, height=300, equal=False)
p.axes(xticks=[4.5, 5, 5.5], yticks=[10, 15, 20, 30])
p.segment(5, 0, 5, 15, color=GRAY, width=1.2, dash=True)
p.func(F, color=BLUE)
p.line(33, 5, 15, color=RED)
p.point(5, 15, color=RED)
p.text(5, 15, "(5, 15)", color=RED, dx=-8, dy=-8, anchor="end")
p.text(5.22, 34, "y = f(x)", color=BLUE, italic=True, anchor="end")
p.text(5.58, 21, "y = L(x)", color=RED, italic=True, anchor="end")
p.save(out("fig-linear.svg"))

# 2. 題 8：x³ − x 在 [0, 2]，割線與平行的切線
G = lambda x: x ** 3 - x
c = 2 / math.sqrt(3)
p = Plot((-0.6, 2.4), (-1.2, 6.6), width=400, height=340, equal=False)
p.axes(xticks=[1, 2], yticks=[2, 4, 6])
p.func(G, color=BLUE)
p.segment(0, 0, 2, 6, color=GREEN, width=1.8)
p.line(3, c, G(c), color=RED, dash=True)
p.segment(c, 0, c, G(c), color=GRAY, width=1.2, dash=True)
p.point(0, 0, color=GREEN)
p.point(2, 6, color=GREEN)
p.point(c, G(c), color=RED)
p.text(2, 6, "(2, 6)", color=GREEN, dx=-8, dy=4, anchor="end")
p.text(c, 0, "c = 2/√3", color=RED, dx=-2, dy=18)
p.text(0.55, 3.2, "割線斜率 3", color=GREEN, anchor="end")
p.text(2.3, 1.3, "切線斜率 3", color=RED, anchor="end")
p.text(1.3, 5.8, "y = x³ − x", color=BLUE, italic=True, anchor="end")
p.save(out("fig-mvt.svg"))

# 3. 題 20：x ∛(x² − 4) 的增減
H = lambda x: x * cbrt(x * x - 4)
r = math.sqrt(12 / 5)
p = Plot((-3.4, 3.4), (-3.6, 5.4), width=420, height=360, equal=False)
p.axes(xticks=[-3, -2, -1, 1, 2, 3], yticks=[-2, 2, 4])
p.func(H, xr=(-3.4, -r), color=BLUE)
p.func(H, xr=(-r, r), color=RED)
p.func(H, xr=(r, 3.4), color=BLUE)
p.point(-r, H(-r), color=RED)
p.point(r, H(r), color=RED)
p.text(r, H(r), "x = √(12/5)", color=RED, dy=22, anchor="middle")
p.text(-r, H(-r), "x = −√(12/5)", color=RED, dy=-12, anchor="middle")
p.text(2.9, 4.6, "遞增", color=BLUE, anchor="end")
p.text(-2.9, -2.9, "遞增", color=BLUE)
p.text(0.6, 0.6, "遞減", color=RED)
p.save(out("fig-mono.svg"))

# 4. 題 22：(x² − x − 30)/(x + 6) 的漸近線
K = lambda x: (x * x - x - 30) / (x + 6)
p = Plot((-26, 16), (-50, 30), width=440, height=340, equal=False)
p.axes(xticks=[-20, -10, 10], yticks=[-40, -20, 20])
p.vline(-6, color=GRAY, width=1.2, dash=True)
p.line(1, 0, -7, color=RED, width=1.6, dash=True)
p.func(K, color=BLUE, n=2000)
p.text(-6, 26, "x = −6", color=GRAY, dx=-6, anchor="end")
p.text(15, -12, "y = x − 7", color=RED, italic=True, anchor="end")
p.text(-24, -12, "y = f(x)", color=BLUE, italic=True)
p.save(out("fig-asymptote.svg"))

# 5. 題 29：牛頓法 x³ − 3x + 6，x₀ = −2
N = lambda x: x ** 3 - 3 * x + 6
dN = lambda x: 3 * x * x - 3
p = Plot((-2.8, -1.6), (-4, 6), width=420, height=320, equal=False)
p.axes(xticks=[(-2.6, "−2.6"), (-2.2, "−2.2"), (-2, "−2"), (-1.8, "−1.8")], yticks=[-2, 2, 4])
p.func(N, color=BLUE)
x0, x1 = -2.0, -22 / 9
x2 = x1 - N(x1) / dN(x1)
p.segment(x0, 0, x0, N(x0), color=GRAY, width=1.2, dash=True)
p.segment(x0, N(x0), x1, 0, color=RED, width=1.6)
p.segment(x1, 0, x1, N(x1), color=GRAY, width=1.2, dash=True)
p.segment(x1, N(x1), x2, 0, color=ORANGE, width=1.6)
p.point(x0, N(x0), color=RED)
p.point(x1, N(x1), color=ORANGE)
p.point(x1, 0, color=RED, open=True)
p.point(x2, 0, color=ORANGE, open=True)
p.text(x0, N(x0), "(−2, 4)", color=RED, dx=8, dy=4)
p.text(x1, 0, "x₁", color=RED, italic=True, dx=-6, dy=-8, anchor="end")
p.text(x2, 0, "x₂", color=ORANGE, italic=True, dx=9, dy=18)
p.text(-1.72, 5.2, sup("y = x", "3") + "− 3x + 6", color=BLUE, italic=True, anchor="end")
p.save(out("fig-newton.svg"))

print("ok")
