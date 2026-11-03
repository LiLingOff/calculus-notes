"""產生 Week 9 的圖：python week09/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, _f, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


def region(p, pts, color, opacity=0.28):
    """填色多邊形（數學座標的頂點串）。"""
    d = "M" + " L".join(f"{_f(p.X(x))},{_f(p.Y(y))}" for x, y in pts) + " Z"
    p.items.append(f'<path d="{d}" fill="{color}" fill-opacity="{opacity}" stroke="{color}" '
                   f'stroke-width="1" stroke-linejoin="round" clip-path="url(#clip)"/>')


def under(f, a, b, n=200):
    """y=f(x) 與 x 軸在 [a,b] 之間的多邊形頂點。"""
    return [(a, 0)] + [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)] + [(b, 0)]


# 1. 題 1、2：x² 在 [0,1] 的左端點與右端點矩形
SQ = lambda x: x * x
N = 5
for name, shift, color, label in [("fig-left.svg", 0, BLUE, "左端點：低估"),
                                  ("fig-right.svg", 1, ORANGE, "右端點：高估")]:
    p = Plot((-0.15, 1.2), (-0.12, 1.15), width=320)
    for i in range(N):
        h = SQ((i + shift) / N)
        region(p, [(i / N, 0), (i / N, h), ((i + 1) / N, h), ((i + 1) / N, 0)], color)
    p.axes(xticks=[(0.2, "1/5"), (0.6, "3/5"), (1, "1")], yticks=[1])
    p.func(SQ, xr=(0, 1.1), color=RED)
    p.text(0.05, 0.92, label, color=color)
    p.text(1.08, 1.0, "y = x²", color=RED, italic=True, anchor="end", dy=-10)
    p.save(out(name))

# 2. 題 7：∫_{-3}^{4} x dx 的有號面積
p = Plot((-3.8, 4.8), (-3.8, 4.8), width=360)
region(p, [(-3, 0), (-3, -3), (0, 0)], ORANGE, 0.4)
region(p, [(0, 0), (4, 4), (4, 0)], BLUE, 0.35)
p.axes(xticks=[(-3, "−3"), 4], yticks=[(-3, "−3"), 4])
p.func(lambda x: x, color=RED)
p.text(-1.6, -1.0, "−9/2", color=ORANGE, anchor="middle", size=17)
p.text(2.9, 1.0, "+8", color=BLUE, anchor="middle", size=17)
p.text(4.5, 4.4, "y = x", color=RED, italic=True, anchor="end", dy=-6)
p.save(out("fig-signed.svg"))

# 3. 題 8：半圓
C = lambda x: math.sqrt(max(0.0, 1 - x * x))
p = Plot((-1.4, 1.4), (-0.25, 1.3), width=360)
region(p, under(C, -1, 1), BLUE, 0.3)
p.axes(xticks=[(-1, "−1"), 1], yticks=[1])
p.func(C, xr=(-1, 1), color=RED, n=1200)
p.text(0, 0.42, "π/2", color=BLUE, anchor="middle", size=17)
p.text(0.8, 0.9, "y = √(1 − x²)", color=RED, italic=True)
p.save(out("fig-semicircle.svg"))

# 4. 題 11：∫_0^10 sin x dx 的正負面積
p = Plot((-0.6, 11), (-1.6, 1.6), width=460, height=230, equal=False)
cuts = [0, math.pi, 2 * math.pi, 3 * math.pi, 10]
for i in range(4):
    a, b = cuts[i], cuts[i + 1]
    region(p, under(math.sin, a, b), BLUE if i % 2 == 0 else ORANGE, 0.35)
p.axes(xticks=[(math.pi, "π"), (2 * math.pi, "2π"), (3 * math.pi, "3π")], yticks=[1, (-1, "−1")])
p.func(math.sin, xr=(-0.6, 11), color=RED)
p.text(math.pi / 2, 0.35, "+2", color=BLUE, anchor="middle")
p.text(3 * math.pi / 2, -0.55, "−2", color=ORANGE, anchor="middle")
p.text(5 * math.pi / 2, 0.35, "+2", color=BLUE, anchor="middle")
p.text(10, -0.75, "3π 到 10", color=ORANGE, anchor="middle", size=12)
p.save(out("fig-sin10.svg"))

# 5. 定理 9.5.1：反函數積分的兩塊面積
F = lambda x: 0.3 * x * x + 0.3
a, b = 1, 3
fa, fb = F(a), F(b)
p = Plot((-0.4, 3.8), (-0.4, 3.6), width=380)
region(p, under(F, a, b), GREEN, 0.3)
left = [(0, fa), (a, fa)] + [(a + (b - a) * i / 200, F(a + (b - a) * i / 200)) for i in range(201)] + [(b, fb), (0, fb)]
region(p, left, RED, 0.18)
p.segment(0, fb, b, fb, color=GRAY, width=1.2, dash=True)
p.segment(b, 0, b, fb, color=GRAY, width=1.2, dash=True)
p.segment(0, fa, a, fa, color=GRAY, width=1.2, dash=True)
p.segment(a, 0, a, fa, color=GRAY, width=1.2, dash=True)
p.axes(xticks=[(a, "a"), (b, "b")], yticks=[(fa, "f(a)"), (fb, "f(b)")])
p.func(F, xr=(0, 3.4), color=BLUE)
p.text(2.25, 0.55, "∫ f(x) dx", color=GREEN, anchor="middle")
p.text(0.9, 2.2, "∫ f⁻¹(y) dy", color=RED, anchor="middle")
p.text(3.35, 3.55, "y = f(x)", color=BLUE, italic=True, anchor="end", dy=8)
p.save(out("fig-inverse.svg"))

print("ok")
