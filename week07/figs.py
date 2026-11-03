"""產生 Week 7 的圖：python week07/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, _f, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402

PI = math.pi


def out(name):
    return HERE / name


def curve(p, pts, color=BLUE, width=2.2):
    """依序連接參數曲線上的點 (x, y)。"""
    d = "M" + " L".join(f"{_f(p.X(x))},{_f(p.Y(y))}" for x, y in pts)
    p.items.append(p._path(d, color, width, False))


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


def pi_ticks(lo, hi):
    names = {-1: "−π", 1: "π", 2: "2π", 3: "3π"}
    return [(k * PI, names[k]) for k in range(lo, hi + 1) if k in names]


# 1. ln x / x 在 x = e 有最大值
f = lambda x: math.log(x) / x
p = Plot((-0.3, 7), (-1, 0.6), width=440, height=240, equal=False)
p.axes(xticks=[1, 2, (math.e, "e"), (PI, "π"), 5, 6], yticks=[(1 / math.e, "1/e")])
p.func(f, xr=(0.35, 7), color=BLUE)
p.segment(math.e, 0, math.e, 1 / math.e, color=GRAY, width=1.2, dash=True)
p.point(math.e, 1 / math.e, color=RED)
p.point(PI, f(PI), color=GREEN)
p.text(math.e, 1 / math.e, "最大值", color=RED, anchor="end", dx=-8, dy=-8)
p.text(PI, f(PI), "(π, ln π / π)", color=GREEN, dx=8, dy=-8)
p.text(6.9, 0.5, "y = ln x / x", color=BLUE, italic=True, anchor="end")
p.save(out("fig-lnx.svg"))

# 2. 題 3：x³ − x 在 [−2, 1] 的最大最小值
f = lambda x: x ** 3 - x
c = 1 / math.sqrt(3)
p = Plot((-2.5, 1.6), (-6.6, 1.4), width=400, height=300, equal=False)
p.axes(xticks=[-2, -1, 1], yticks=[-6, -4, -2])
p.func(f, xr=(-2.5, 1.6), color=GRAY, width=1.2, dash=True)
p.func(f, xr=(-2, 1), color=BLUE)
p.point(-2, -6, color=RED)
p.point(1, 0, color=BLUE)
p.point(-c, f(-c), color=RED)
p.point(c, f(c), color=BLUE)
p.text(-2, -6, "最小 (−2, −6)", color=RED, dx=10, dy=4)
p.text(-c, f(-c), "最大", color=RED, anchor="middle", dy=-12)
p.save(out("fig-extrema.svg"))

# 3. 凹口向上／向下：切線都在曲線下方／上方
for name, s in (("fig-concave-up.svg", 1), ("fig-concave-down.svg", -1)):
    p = Plot((-2.2, 2.2), (-2.6, 2.6) if s < 0 else (-0.6, 4.6), width=300)
    p.axes()
    p.func(lambda x: s * x * x, color=BLUE)
    for a in (-1.4, -0.5, 0.6, 1.5):
        p.segment(a - 0.6, s * (a * a - 1.2 * a), a + 0.6, s * (a * a + 1.2 * a), color=RED, width=1.6)
        p.point(a, s * a * a, color=RED, r=3)
    p.text(0, 4.3 if s > 0 else -2.3, sup("y = x", "2") if s > 0 else "y = −" + sup("x", "2"),
           color=BLUE, italic=True, anchor="middle", dy=4 if s > 0 else 0)
    p.save(out(name))

# 4. 題 10：y² = x³ + 2xy + 7 在 (1, 4) 的切線在曲線下方
f = lambda x: x + math.sqrt(x * x + x ** 3 + 7)
p = Plot((0.4, 1.7), (2.9, 5.6), width=380, height=300, equal=False)
p.axes(xticks=[0.5, 1, 1.5], yticks=[3, 4, 5])
p.func(f, color=BLUE)
p.line(11 / 6, 1, 4, color=RED)
p.point(1, 4, color=RED)
p.text(1, 4, "(1, 4)", color=RED, dx=-8, dy=-8, anchor="end")
p.text(1.65, 5.35, "曲線", color=BLUE, anchor="end")
p.text(1.62, 4.75, "切線 L(x)", color=RED, anchor="end", dy=24)
p.save(out("fig-linear.svg"))

# 5. 題 13：(x² − x − 2)/(x² − x − 6)
f = lambda x: 1 + 4 / (x * x - x - 6)
p = Plot((-6, 7), (-4, 5), width=440, height=320, equal=False)
p.axes(xticks=[-4, -2, 2, 4, 6], yticks=[-2, 2, 4])
p.segment(-6, 1, 7, 1, color=GRAY, width=1.2, dash=True)
p.vline(-2, color=GRAY, width=1.2, dash=True)
p.vline(3, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=2000)
p.point(0.5, 9 / 25, color=RED)
p.point(-1, 0)
p.point(2, 0)
p.text(0.5, 2.0, "極大 (1/2, 9/25)", color=RED, anchor="middle")
p.text(6.9, 1, "y = 1", color=GRAY, anchor="end", dy=-8)
p.save(out("fig-ex13.svg"))

# 6. 題 14：(3x³ − 2x² + 1)/(4x³ + 2x − 3)，左圖全貌、右圖放大看極值
f = lambda x: (3 * x ** 3 - 2 * x * x + 1) / (4 * x ** 3 + 2 * x - 3)
a = 0.728082123
p = Plot((-8, 6), (-2.5, 3.5), width=360, height=300, equal=False)
p.axes(xticks=[-6, -4, -2, 2, 4], yticks=[-2, -1, 1, 2, 3])
p.segment(-8, 0.75, 6, 0.75, color=GRAY, width=1.2, dash=True)
p.vline(a, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=3000)
p.point(0, -1 / 3)
p.save(out("fig-ex14.svg"))
p = Plot((-9, 5), (0.35, 1.0), width=360, height=300, equal=False)
p.axes(xticks=[-8, -6, -4, -2, 2, 4], yticks=[(0.5, "0.5"), (0.75, "0.75")])
p.segment(-9, 0.75, 5, 0.75, color=GRAY, width=1.2, dash=True)
p.vline(a, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=3000)
p.point(-3.2833, 0.83856, color=RED)
p.point(1.4965, 0.49074, color=GREEN)
for x0 in (-4.7935, 2.0917):
    p.point(x0, f(x0), color=ORANGE, r=3.5)
p.text(-3.2833, 0.83856, "極大", color=RED, anchor="middle", dy=-12)
p.text(1.4965, 0.49074, "極小", color=GREEN, anchor="middle", dy=22)
p.save(out("fig-ex14-zoom.svg"))

# 7. 題 15：1 + 2/x − 8/x²
f = lambda x: 1 + 2 / x - 8 / (x * x)
p = Plot((-14, 30), (-3, 1.8), width=440, height=340, equal=False)
p.axes(xticks=[-10, 10, 20], yticks=[-2, 1, 2])
p.segment(-14, 1, 30, 1, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=3000)
p.point(8, 9 / 8, color=RED)
p.point(12, 10 / 9, color=ORANGE)
p.point(-4, 0)
p.point(2, 0)
p.text(8, 9 / 8, "極大", color=RED, anchor="end", dx=-4, dy=-12)
p.text(12, 10 / 9, "反曲點", color=ORANGE, dx=4, dy=-12)
p.save(out("fig-ex15.svg"))

# 8. 題 17：cos x / (2 + sin x)
f = lambda x: math.cos(x) / (2 + math.sin(x))
p = Plot((-PI - 0.4, 4 * PI), (-1, 1), width=460, height=220, equal=False)
p.axes(xticks=pi_ticks(-1, 3), yticks=[(0.5, "1/2"), -0.5])
p.func(f, color=BLUE, n=1600)
for k in (0, 1):
    p.point(7 * PI / 6 + 2 * k * PI, -1 / math.sqrt(3), color=GREEN, r=3.5)
    p.point(11 * PI / 6 + 2 * k * PI, 1 / math.sqrt(3), color=RED, r=3.5)
    p.point(PI / 2 + 2 * k * PI, 0, color=ORANGE, r=3.5)
    p.point(3 * PI / 2 + 2 * k * PI, 0, color=ORANGE, r=3.5)
p.save(out("fig-ex17.svg"))

# 9. 題 18：2x²/(x² − 1)
f = lambda x: 2 * x * x / (x * x - 1)
p = Plot((-4, 4), (-4, 7), width=400, height=320, equal=False)
p.axes(xticks=[-3, -2, -1, 1, 2, 3], yticks=[-2, 2, 4, 6])
p.segment(-4, 2, 4, 2, color=GRAY, width=1.2, dash=True)
p.vline(-1, color=GRAY, width=1.2, dash=True)
p.vline(1, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=2000)
p.point(0, 0, color=RED)
p.text(3.9, 2, "y = 2", color=GRAY, anchor="end", dy=-8)
p.save(out("fig-ex18.svg"))

# 10. 題 19：(x + 1)³/(x² + 2x)
f = lambda x: (x + 1) ** 3 / (x * x + 2 * x)
r3 = math.sqrt(3)
p = Plot((-6, 4), (-8, 8), width=400, height=360, equal=False)
p.axes(xticks=[-5, -4, -3, -2, -1, 1, 2, 3], yticks=[-6, -4, -2, 2, 4, 6])
p.line(1, 0, 1, color=GRAY, width=1.2, dash=True)
p.vline(-2, color=GRAY, width=1.2, dash=True)
p.vline(0, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=3000)
p.point(-1 - r3, -1.5 * r3, color=RED)
p.point(-1 + r3, 1.5 * r3, color=GREEN)
p.point(-1, 0, color=ORANGE)
p.text(-1 - r3, -1.5 * r3, "極大", color=RED, anchor="end", dx=-8, dy=-6)
p.text(-1 + r3, 1.5 * r3, "極小", color=GREEN, dx=8, dy=18)
p.text(3.9, 2.0, "y = x + 1", color=GRAY, anchor="end", italic=True)
p.save(out("fig-ex19.svg"))

# 11. 題 20：x²/√(x + 1)
f = lambda x: x * x / math.sqrt(x + 1)
p = Plot((-1.6, 5), (-1, 9), width=360, height=320, equal=False)
p.axes(xticks=[-1, 1, 2, 3, 4], yticks=[2, 4, 6, 8])
p.vline(-1, color=GRAY, width=1.2, dash=True)
p.func(f, xr=(-0.9995, 5), color=BLUE, n=3000)
p.point(0, 0, color=GREEN)
p.text(0.4, 7.6, "y = " + sup("x", "2") + "/√(x+1)", color=BLUE, italic=True)
p.save(out("fig-ex20.svg"))

# 12. 題 21：e^(sin x)
f = lambda x: math.exp(math.sin(x))
al = math.asin((math.sqrt(5) - 1) / 2)
p = Plot((-PI - 0.4, 4 * PI), (-0.3, 3.2), width=460, height=230, equal=False)
p.axes(xticks=pi_ticks(-1, 3), yticks=[(1 / math.e, "1/e"), 1, (math.e, "e")])
p.func(f, color=BLUE, n=1600)
for k in (-1, 0, 1):
    for x0 in (al + 2 * k * PI, PI - al + 2 * k * PI):
        if -PI - 0.4 < x0 < 4 * PI:
            p.point(x0, f(x0), color=ORANGE, r=3.5)
p.save(out("fig-ex21.svg"))

# 13. 題 22：y² = x³ − 4x + 3
g = lambda x: x ** 3 - 4 * x + 3
up = lambda x: math.sqrt(g(x)) if g(x) >= 0 else None
dn = lambda x: -math.sqrt(g(x)) if g(x) >= 0 else None
r1, r2 = (-1 - math.sqrt(13)) / 2, (-1 + math.sqrt(13)) / 2
p = Plot((-3.2, 3.2), (-4.2, 4.2), width=360)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-2, 2])
for lo, hi in ((r1, 1), (r2, 3.2)):
    xs = [lo + (hi - lo) * (1 - math.cos(PI * i / 600)) / 2 for i in range(601)]
    top = [(x, math.sqrt(max(g(x), 0))) for x in xs]
    curve(p, [(x, -y) for x, y in reversed(top)] + top)
p.point(1, 0, color=RED, r=3.5)
p.point(r2, 0, color=RED, r=3.5)
p.point(r1, 0, color=RED, r=3.5)
p.save(out("fig-ex22.svg"))

# 14. 題 23：(x + y)(x − y)² = 8，令 u = (x+y)/√2、v = (x−y)/√2，即 u v² = 2√2
S2 = math.sqrt(2)
p = Plot((-6, 8), (-5, 8), width=420)
p.axes(xticks=[-4, -2, 2, 4, 6], yticks=[-4, -2, 2, 4, 6])
p.line(1, 0, 0, color=GRAY, width=1.2, dash=True)
p.line(-1, 0, 0, color=GRAY, width=1.2, dash=True)
for sgn, col in ((-1, BLUE), (1, GREEN)):
    pts = []
    for i in range(1, 1601):
        v = sgn * 0.05 * (300 ** (i / 1600))
        u = 2 * S2 / (v * v)
        pts.append(((u + v) / S2, (u - v) / S2))
    curve(p, pts, color=col)
P = (-(2 ** (-2 / 3)), 3 * 2 ** (-2 / 3))
p.point(*P, color=RED)
p.point(0, 2)
p.point(2, 0)
p.text(*P, "P", color=RED, italic=True, anchor="end", dx=-8, dy=-6)
p.text(-5.8, 3.6, "y = −x", color=GRAY, italic=True)
p.text(6.0, 7.6, "y = x", color=GRAY, italic=True, anchor="end")
p.save(out("fig-ex23.svg"))

# 15. 題 24 (a)(b)(c)
p = Plot((-1.6, 1.6), (-1.6, 1.6), width=300)
p.axes(xticks=[-1, 1], yticks=[-1, 1])
xs = [-1 + 2.6 * (1 - math.cos(PI * i / 1200)) / 2 for i in range(1201)]
xs = [x for x in xs if x <= 1.6]
top = [(x, x * math.sqrt(x + 1)) for x in xs]
curve(p, [(x, -y) for x, y in reversed(top)] + top)
p.point(-2 / 3, -2 * math.sqrt(3) / 9, color=RED, r=3)
p.point(-2 / 3, 2 * math.sqrt(3) / 9, color=RED, r=3)
p.text(-1.55, 1.3, "(a)", color=GRAY)
p.save(out("fig-ex24a.svg"))

p = Plot((-8, 14), (-5, 5), width=360, height=300, equal=False)
p.axes(xticks=[-5, 5, 10], yticks=[-4, -2, 2, 4])
for lo, hi in ((0.25, 4.5), (-4.5, -0.25)):
    ys = [lo + (hi - lo) * i / 1200 for i in range(1201)]
    curve(p, [(y * y + 6 / y, y) for y in ys])
p.point(3 ** (5 / 3), 3 ** (1 / 3), color=RED, r=3.5)
p.point(0, -(6 ** (1 / 3)), color=ORANGE, r=3.5)
p.text(-7.8, 4.2, "(b)", color=GRAY)
p.save(out("fig-ex24b.svg"))

p = Plot((-4, 4), (-4, 4), width=300)
p.axes(xticks=[-2, 2], yticks=[-2, 2])
p.line(-1, 0, 0, color=GRAY, width=1.2, dash=True)
p.func(lambda x: cbrt(6 - x ** 3), color=BLUE, n=2000)
c6 = 6 ** (1 / 3)
p.point(0, c6, color=ORANGE, r=3.5)
p.point(c6, 0, color=ORANGE, r=3.5)
p.text(2.4, 3.3, "(c)", color=GRAY)
p.save(out("fig-ex24c.svg"))

# 16. 梯度下降：t = 0.2 收斂、t = 1.1 發散
for name, t, xr, yr, n in (("fig-gd-good.svg", 0.2, (-12, 12), (-10, 130), 6),
                           ("fig-gd-bad.svg", 1.1, (-20, 20), (-20, 330), 4)):
    p = Plot(xr, yr, width=300, height=260, equal=False)
    p.axes(xticks=[-10, 10], yticks=[100] if t < 1 else [100, 200, 300])
    p.func(lambda x: x * x, color=BLUE)
    x = 10.0
    for k in range(n):
        nx = x - t * 2 * x
        p.segment(x, x * x, nx, nx * nx, color=RED, width=1.4)
        p.point(x, x * x, color=RED, r=3)
        x = nx
    p.point(x, x * x, color=RED, r=3)
    p.text(xr[1] * 0.1, yr[1] * 0.92, f"t = {t}", color=RED)
    p.save(out(name))

print("ok")
