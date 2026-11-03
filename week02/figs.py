"""產生 Week 2 的圖：python week02/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


# 1. 分段函數的左右極限（題 4）
p = Plot((-2.2, 2.2), (-2.2, 3.2), width=360)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-2, -1, 1, 2, 3])
p.func(lambda x: x, xr=(-2.2, 0), color=BLUE)
p.func(lambda x: x * x + 1, xr=(0, 2.2), color=BLUE)
p.point(0, 0, color=BLUE, open=True)
p.point(0, 1, color=BLUE)
p.text(-1.9, -0.7, "y = x", color=BLUE, italic=True)
p.text(1.5, 3.25, "y = " + sup("x", "2") + "+ 1", color=BLUE, italic=True, anchor="end", dy=16)
p.save(out("fig-piecewise.svg"))

# 2. y = sin(x)/x，x=0 挖一個洞
p = Plot((-13, 13), (-0.5, 1.3), width=440, height=200, equal=False)
p.axes(xticks=[(-4 * math.pi, "−4π"), (-2 * math.pi, "−2π"), (2 * math.pi, "2π"), (4 * math.pi, "4π")], yticks=[1])
p.func(lambda x: math.sin(x) / x if x else None, color=BLUE, n=1600)
p.point(0, 1, color=BLUE, open=True)
p.text(5.2, 0.85, "y = sin x / x", color=BLUE, italic=True)
p.save(out("fig-sinc.svg"))

# 3. 單位圓證明 sin x ≤ x ≤ tan x
t = 0.75
c, s, tn = math.cos(t), math.sin(t), math.tan(t)
p = Plot((-0.15, 1.35), (-0.18, 1.12), width=380, pad=18)
p.func(lambda u: math.sqrt(1 - u * u) if abs(u) <= 1 else None, xr=(0, 1), color=GRAY, width=1.4)
p.func(lambda u: math.sqrt(max(0.0, 1 - u * u)), xr=(c, 1), color=ORANGE, width=3)
p.segment(0, 0, 1, 0, color=GRAY, width=1.6)
p.segment(0, 0, 1, tn, color=GRAY, width=1.6)
p.segment(c, 0, c, s, color=BLUE, width=2.4)
p.segment(1, 0, 1, tn, color=GREEN, width=2.4)
for x, y in ((0, 0), (1, 0), (c, s), (1, tn)):
    p.point(x, y, color="#6b7280", r=3)
p.text(0, 0, "A", italic=True, dx=-6, dy=16, anchor="end")
p.text(1, 0, "B", italic=True, dx=6, dy=16)
p.text(c, s, "C", italic=True, dx=-8, dy=-6, anchor="end")
p.text(1, tn, "D", italic=True, dx=8, dy=4)
p.text(0.2, 0.03, "x", italic=True, dy=-2)
p.text(c, s / 2, "sin x", color=BLUE, anchor="end", dx=-6)
p.text(1, tn / 2, "tan x", color=GREEN, dx=8)
p.text(0.5, 0, "1", dy=18, anchor="middle")
p.save(out("fig-unit-circle.svg"))

# 4. 夾擠定理示意：x² sin(1/x) 被 ±x² 夾住（標籤放在曲線右端外面）
s2 = lambda x: x * x * math.sin(1 / x) if x else 0.0
p = Plot((-0.42, 0.72), (-0.2, 0.2), width=460, height=300, equal=False)
p.axes()
X = (-0.42, 0.42)
p.func(lambda x: x * x, xr=X, color=RED, width=1.4, dash=True)
p.func(lambda x: -x * x, xr=X, color=GREEN, width=1.4, dash=True)
p.func(s2, xr=X, color=BLUE, width=1.6, n=6000)
p.text(0.44, 0.42 ** 2, "h(x) = " + sup("x", "2"), color=RED, italic=True, dy=5, size=13)
p.text(0.44, s2(0.42), "g(x) = " + sup("x", "2") + "sin(1/x)", color=BLUE, italic=True, dy=5, size=13)
p.text(0.44, -0.42 ** 2, "f(x) = −" + sup("x", "2"), color=GREEN, italic=True, dy=5, size=13)
p.save(out("fig-squeeze.svg"))

# 5. √(1−cos 2x)/x = √2 |sin x| / x：左右極限不同
g = lambda x: math.sqrt(1 - math.cos(2 * x)) / x if x else None
p = Plot((-3.3, 3.3), (-2, 2), width=380)
p.axes(xticks=[(-math.pi, "−π"), (math.pi, "π")], yticks=[(math.sqrt(2), "√2"), (-math.sqrt(2), "−√2")])
p.func(g, xr=(-3.3, -1e-6), color=BLUE)
p.func(g, xr=(1e-6, 3.3), color=BLUE)
p.point(0, math.sqrt(2), color=BLUE, open=True)
p.point(0, -math.sqrt(2), color=BLUE, open=True)
p.save(out("fig-sqrt-trap.svg"))

# 6. ln x 與 1/x² 的垂直漸近線
p = Plot((-0.6, 3.2), (-3, 3), width=300)
p.axes(xticks=[1, 2, 3], yticks=[-2, 2])
p.func(lambda x: math.log(x) if x > 0 else None, xr=(1e-4, 3.2), color=BLUE, n=2000)
p.text(1.5, -1.3, "y = ln x", color=BLUE, italic=True)
p.save(out("fig-ln.svg"))

p = Plot((-2.2, 2.2), (-0.6, 4.4), width=300, height=None)
p.axes(xticks=[-2, -1, 1, 2], yticks=[1, 2, 3, 4])
p.func(lambda x: 1 / (x * x), xr=(-2.2, -0.01), color=BLUE)
p.func(lambda x: 1 / (x * x), xr=(0.01, 2.2), color=BLUE)
p.text(0.95, 3.3, "y = 1/" + sup("x", "2"), color=BLUE, italic=True)
p.save(out("fig-inv-sq.svg"))

# 7. f(x) = (eˣ+2)/(e²ˣ−4) = 1/(eˣ−2)
L2 = math.log(2)
f = lambda x: 1 / (math.exp(x) - 2)
p = Plot((-3, 3.5), (-3, 3), width=420)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-2, -1, 1, 2])
p.vline(L2, color=RED, width=1.4, dash=True)
p.segment(-3, -0.5, 3.5, -0.5, color=GREEN, width=1.4, dash=True)
p.func(f, xr=(-3, L2 - 1e-4), color=BLUE, n=2000)
p.func(f, xr=(L2 + 1e-4, 3.5), color=BLUE, n=2000)
p.text(L2, 2.7, "x = ln 2", color=RED, anchor="end", dx=-6)
p.text(-2.9, -0.5, "y = −1/2", color=GREEN, dy=18)
p.text(3.4, 0, "y = 0", color=GRAY, anchor="end", dy=16, size=13)
p.save(out("fig-asym.svg"))

# 8. f(x) = 2/(1+e^(1/x))
def h(x):
    try:
        return 2 / (1 + math.exp(1 / x))
    except OverflowError:
        return 0.0

p = Plot((-4, 4), (-0.6, 2.6), width=420)
p.axes(xticks=[-3, -2, -1, 1, 2, 3], yticks=[1, 2])
p.segment(-4, 1, 4, 1, color=GRAY, width=1.2, dash=True)
p.func(h, xr=(-4, -1e-4), color=BLUE, n=2000)
p.func(h, xr=(1e-4, 4), color=BLUE, n=2000)
p.point(0, 2, color=BLUE, open=True)
p.point(0, 0, color=BLUE, open=True)
p.text(3.9, 1, "y = 1", color=GRAY, anchor="end", dy=-8, size=13)
p.save(out("fig-exp-jump.svg"))

print("ok")
