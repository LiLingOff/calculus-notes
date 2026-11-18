"""產生 Week 12 的圖：python week12/figs.py"""
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
    p.items.append(f'<path d="{d}" fill="{color}" fill-opacity="{opacity}" stroke="none" '
                   f'clip-path="url(#clip)"/>')


def between(f, g, a, b, n=200):
    """上曲線 f、下曲線 g 在 [a,b] 之間的區域（逆時針一圈）。"""
    xs = [a + (b - a) * i / n for i in range(n + 1)]
    return [(x, f(x)) for x in xs] + [(x, g(x)) for x in reversed(xs)]


def curve(p, pts, color, width=2.2):
    d = "M" + " L".join(f"{_f(p.X(x))},{_f(p.Y(y))}" for x, y in pts)
    p.items.append(p._path(d, color, width, False))


# 1. 題 1：ln x / x 與 (ln x)^2 / x
f1 = lambda t: math.log(t) / t
g1 = lambda t: math.log(t) ** 2 / t
p = Plot((-0.2, 4.2), (-0.15, 0.6), width=400, height=260, equal=False)
region(p, between(f1, g1, 1, math.e), BLUE, 0.3)
p.axes(xticks=[1, (math.e, "e")], yticks=[])
p.func(f1, xr=(0.75, 4.1), color=RED)
p.func(g1, xr=(0.75, 4.1), color=GREEN)
p.text(3.6, f1(3.6), "y = ln x / x", color=RED, italic=True, anchor="middle", dy=20)
p.text(3.6, g1(3.6), "y = (ln x)² / x", color=GREEN, italic=True, anchor="middle", dy=-10)
p.save(out("fig-q1.svg"))

# 2. 題 2：1/x、x、x/4
p = Plot((-0.2, 3.2), (-0.2, 2.2), width=380)
top = lambda t: t if t <= 1 else 1 / t
region(p, between(top, lambda t: t / 4, 0, 2), BLUE, 0.3)
p.segment(1, 0, 1, 1, color=GRAY, dash=True, width=1.2)
p.axes(xticks=[1, 2], yticks=[1])
p.func(lambda t: 1 / t, xr=(0.45, 3.1), color=RED)
p.func(lambda t: t, xr=(0, 2.1), color=GREEN)
p.func(lambda t: t / 4, xr=(0, 3.1), color=ORANGE)
p.text(0.5, 2.0, "y = 1/x", color=RED, italic=True)
p.text(2.05, 2.05, "y = x", color=GREEN, italic=True)
p.text(3.1, 0.78, "y = x/4", color=ORANGE, italic=True, anchor="end", dy=-6)
p.text(0.62, 0.32, "左段", color=GRAY, anchor="middle", size=12)
p.text(1.4, 0.55, "右段", color=GRAY, anchor="middle", size=12)
p.save(out("fig-q2.svg"))

# 3. 題 3：y² = 2x + 1 與 y² = 5x − 5（橫躺的拋物線，對 y 積分）
s5 = math.sqrt(5)
ys = [-2.9 + 5.8 * i / 300 for i in range(301)]
L = lambda v: (v * v - 1) / 2
R = lambda v: (v * v + 5) / 5
p = Plot((-1, 3.4), (-3, 3), width=360)
yy = [-s5 + 2 * s5 * i / 200 for i in range(201)]
region(p, [(R(v), v) for v in yy] + [(L(v), v) for v in reversed(yy)], BLUE, 0.3)
p.segment(L(1.0), 1.0, R(1.0), 1.0, color=GRAY, width=1.4)
p.axes(xticks=[(-0.5, "−½"), 1, 2], yticks=[(s5, "√5"), (-s5, "−√5")])
curve(p, [(L(v), v) for v in ys], RED)
curve(p, [(R(v), v) for v in ys], GREEN)
p.point(2, s5, color=GRAY, r=3)
p.point(2, -s5, color=GRAY, r=3)
p.text(-0.85, 2.65, "x = (y² − 1)/2", color=RED, italic=True)
p.text(3.3, -2.75, "x = (y² + 5)/5", color=GREEN, italic=True, anchor="end")
p.text(R(1.0) + 0.1, 1.0, "右 − 左", color=GRAY, size=12, dy=4)
p.save(out("fig-q3.svg"))

# 4. 題 17：y = x² − 2x 與 y = x 繞 y = 4
par = lambda t: t * t - 2 * t
p = Plot((-0.6, 3.8), (-1.5, 4.8), width=360)
region(p, between(lambda t: t, par, 0, 3), BLUE, 0.3)
p.segment(-0.6, 4, 3.8, 4, color=GRAY, dash=True, width=1.4)
xs_ = 1.6
p.segment(xs_, 4, xs_, par(xs_), color=ORANGE, width=2.4)
p.segment(xs_ + 0.12, 4, xs_ + 0.12, xs_, color=RED, width=2.4)
p.axes(xticks=[1, 2, 3], yticks=[4])
p.func(par, xr=(-0.5, 3.4), color=GREEN)
p.func(lambda t: t, xr=(-0.5, 3.6), color=RED, width=1.8)
p.text(3.7, 4, "y = 4（轉軸）", color=GRAY, anchor="end", dy=-8, size=12)
p.text(xs_ - 0.08, 0.4, "R", color=ORANGE, anchor="end", italic=True)
p.text(xs_ + 0.2, 2.9, "r", color=RED, italic=True)
p.text(3.35, 3.0, "y = x² − 2x", color=GREEN, italic=True, anchor="end", dy=-28)
p.save(out("fig-q17.svg"))

# 5. 題 19：y = x·arccos x 繞 y 軸（殼層）
h = lambda t: t * math.acos(max(-1.0, min(1.0, t)))
p = Plot((-0.15, 1.25), (-0.1, 0.75), width=380, height=260, equal=False)
region(p, between(h, lambda t: 0, 0, 1), BLUE, 0.25)
xk, dx = 0.55, 0.05
region(p, [(xk, 0), (xk, h(xk)), (xk + dx, h(xk)), (xk + dx, 0)], ORANGE, 0.6)
p.axes(xticks=[(xk, "x"), 1], yticks=[])
p.func(h, xr=(0, 1), color=RED)
p.text(0.62, 0.7, "y = x cos⁻¹x", color=RED, italic=True, anchor="middle")
p.text(xk + dx / 2, h(xk) / 2, "高 f(x)", color=ORANGE, anchor="end", dx=-8, size=12)
p.save(out("fig-q19.svg"))

# 6. 題 21：y = x² − 4x + 5 與 y = 2x
q = lambda t: t * t - 4 * t + 5
p = Plot((-0.5, 6), (-0.8, 11), width=340, height=320, equal=False)
region(p, between(lambda t: 2 * t, q, 1, 5), BLUE, 0.3)
p.segment(0, 2, 2, 2, color=GRAY, dash=True, width=1.1)
p.axes(xticks=[1, 2, 5], yticks=[1, 2, 10])
p.func(q, xr=(-0.2, 5.6), color=GREEN)
p.func(lambda t: 2 * t, xr=(0, 5.6), color=RED)
p.text(4.3, 10.3, "y = 2x", color=RED, italic=True, anchor="end")
p.text(0.1, 6.5, "y = x² − 4x + 5", color=GREEN, italic=True)
p.save(out("fig-q21.svg"))

print("ok")
