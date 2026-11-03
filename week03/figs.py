"""產生 Week 3 的圖：python week03/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


# 1. 跳躍不連續：x (x<0)、x²+1 (x≥0)
p = Plot((-2.4, 2.4), (-2.4, 4.2), width=320)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-2, -1, 1, 2, 3, 4])
p.func(lambda x: x, xr=(-2.4, 0), color=BLUE)
p.func(lambda x: x * x + 1, xr=(0, 2.4), color=BLUE)
p.point(0, 0, color=BLUE, open=True)
p.point(0, 1, color=BLUE)
p.text(-0.9, -1.85, "y = x", color=BLUE, italic=True, anchor="end", dx=-6)
p.text(0.85, 0.75, "y = " + sup("x", "2") + " + 1", color=BLUE, italic=True)
p.save(out("fig-jump.svg"))

# 2. 可去不連續：sin x / x，x=0 處另外定義成 3
sinc = lambda x: math.sin(x) / x if x else None
p = Plot((-9, 9), (-1.2, 3.6), width=320, height=240, equal=False)
p.axes(xticks=[(-2 * math.pi, "−2π"), (2 * math.pi, "2π")], yticks=[1, 2, 3])
p.func(sinc, color=GREEN)
p.point(0, 1, color=GREEN, open=True)
p.point(0, 3, color=GREEN)
p.text(0, 3, "g(0) = 3", color=GREEN, italic=True, dx=10, dy=5)
p.text(-8.6, 1.5, "y = sin x / x", color=GREEN, italic=True)
p.save(out("fig-removable.svg"))

# 3. 本質不連續：1/x²
p = Plot((-2.4, 2.4), (-0.5, 4.2), width=320)
p.axes(xticks=[-2, -1, 1, 2], yticks=[1, 2, 3, 4])
p.func(lambda x: 1 / (x * x) if x else None, color=ORANGE, n=1600)
p.text(0.75, 3.4, "y = 1/" + sup("x", "2"), color=ORANGE, italic=True)
p.save(out("fig-essential.svg"))

# 4. 中間值定理示意
f = lambda x: 0.6 + 1.9 * math.sin((x - 0.8) * 0.75)
a, b = 1.0, 3.0
k = 2.0
c = 0.8 + math.asin((k - 0.6) / 1.9) / 0.75
p = Plot((-0.3, 3.6), (-0.4, 3.0), width=380)
p.axes(xticks=[(a, "a"), (c, "c"), (b, "b")], yticks=[(f(a), "f(a)"), (k, "k"), (f(b), "f(b)")])
p.func(f, xr=(a, b), color=RED, width=2.6)
p.segment(0, k, c, k, color=GRAY, width=1.2, dash=True)
p.segment(c, 0, c, k, color=GRAY, width=1.2, dash=True)
p.segment(0, f(b), b, f(b), color=GRAY, width=1.2, dash=True)
p.segment(b, 0, b, f(b), color=GRAY, width=1.2, dash=True)
p.segment(0, f(a), a, f(a), color=GRAY, width=1.2, dash=True)
p.segment(a, 0, a, f(a), color=GRAY, width=1.2, dash=True)
p.point(a, f(a), color=RED)
p.point(b, f(b), color=RED)
p.point(c, k, color=BLUE)
p.text(c, k, "f(c) = k", color=BLUE, italic=True, dx=8, dy=20)
p.save(out("fig-ivt.svg"))

# 5. 題 9：不連續就可能跳過 1/2
p = Plot((-1.5, 1.6), (-1.5, 2.4), width=320)
p.axes(xticks=[-1, 1], yticks=[-1, 1, 2])
p.func(lambda x: x, xr=(-1, 0), color=BLUE)
p.func(lambda x: x + 1, xr=(0, 1), color=BLUE)
p.point(-1, -1, color=BLUE)
p.point(0, 0, color=BLUE, open=True)
p.point(0, 1, color=BLUE)
p.point(1, 2, color=BLUE)
p.segment(-1.5, 0.5, 1.6, 0.5, color=RED, width=1.4, dash=True)
p.text(1.6, 0.5, "y = 1/2", color=RED, italic=True, anchor="end", dy=-8)
p.save(out("fig-gap.svg"))

# 6. 題 10：ex − eˣ − e²ˣ + 3 在 [−2, 1]
g = lambda x: math.e * x - math.exp(x) - math.exp(2 * x) + 3
p = Plot((-2.4, 1.4), (-5, 2), width=380, height=300, equal=False)
p.axes(xticks=[-2, -1, 1], yticks=[-4, -2, 1])
p.func(g, xr=(-2, 1), color=BLUE)
for x in (-2, 0, 1):
    p.point(x, g(x), color=RED)
p.text(-2, g(-2), "f(−2) &lt; 0", color=RED, italic=True, dx=8, dy=18)
p.text(0, g(0), "f(0) = 1", color=RED, italic=True, dx=10, dy=-10)
p.text(1, g(1), "f(1) &lt; 0", color=RED, italic=True, dx=-10, anchor="end")
p.save(out("fig-two-roots.svg"))

# 7. 題 12：4x² sin(π/x) 與 y = 10
h = lambda x: 4 * x * x * math.sin(math.pi / x) if x > 0 else 0.0
p = Plot((-0.6, 2.6), (-3, 18), width=380, height=300, equal=False)
p.axes(xticks=[1, 2], yticks=[5, 10, 15])
p.func(h, color=BLUE, n=4000)
p.segment(-0.6, 10, 2.6, 10, color=RED, width=1.4, dash=True)
p.point(1, 0, color=BLUE)
p.point(2, 16, color=BLUE)
p.text(2.6, 10, "y = 10", color=RED, italic=True, anchor="end", dy=18)
p.text(2, 16, "(2, 16)", color=BLUE, italic=True, anchor="end", dx=-10, dy=-4)
p.text(1, 0, "(1, 0)", color=BLUE, italic=True, anchor="end", dx=-6, dy=-10)
p.save(out("fig-4x2sin.svg"))

print("ok")
