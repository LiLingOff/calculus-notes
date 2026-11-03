"""產生考古題詳解的圖：python exams/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, _f, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


# ---------------- 112 期中 ----------------

# 第 5 題：(x−1)³/(x+1)²
f = lambda x: (x - 1) ** 3 / (x + 1) ** 2
p = Plot((-14, 8), (-26, 6), width=440, height=360, equal=False)
p.axes(xticks=[-10, -5, 5], yticks=[-20, -10])
p.line(1, 0, -5, color=GRAY, width=1.2, dash=True)
p.vline(-1, color=GRAY, width=1.2, dash=True)
p.func(f, color=BLUE, n=3000)
p.point(-5, -13.5, color=RED)
p.point(1, 0, color=ORANGE)
p.point(0, -1)
p.point(-1 / 3, -16 / 3, color=GREEN, r=3.5)
p.text(-5, -13.5, "極大 (−5, −27/2)", color=RED, anchor="middle", dy=-12)
p.text(1, 0, "反曲點", color=ORANGE, dx=-4, dy=-14)
p.text(-13.6, -11.5, "y = x − 5", color=GRAY)
p.text(-1, 4.6, "x = −1", color=GRAY, anchor="end", dx=-6, dy=4)
p.save(out("fig-112-q5.svg"))

# 第 6 題：h(t) = f(t) + g(4 − t)
fw = lambda t: -t ** 3 + 6 * t * t + 15 * t
gw = lambda t: -t ** 3 / 3 + t * t + 23 * t
h = lambda t: fw(t) + gw(4 - t)
p = Plot((-0.3, 4.4), (80, 100), width=400, height=260, equal=False)
p.axes(xticks=[1, 2, 3, 4], yticks=[85, 90, 95])
p.func(h, xr=(0, 4), color=BLUE)
for t, c in ((0, GRAY), (3, RED), (4, GRAY)):
    p.point(t, h(t), color=c)
p.text(3, h(3), "最大 h(3) = 287/3", color=RED, anchor="middle", dy=-12)
p.text(0, h(0), "h(0) = 260/3", color=GRAY, dx=8, dy=14)
p.text(4, h(4), "h(4) = 92", color=GRAY, anchor="end", dx=-8, dy=16)
p.save(out("fig-112-q6.svg"))

# ---------------- 1101 期中（13-16 班） ----------------

# 第 5 題：收益 R 與利潤 Π
R = lambda x: 96 * math.sqrt(x) - x * x / 9
P = lambda x: R(x) - (0.001 * x ** 3 - 0.105 * x * x + 300)
xm = 46.4563
p = Plot((-4, 96), (-220, 500), width=420, height=300, equal=False)
p.axes(xticks=[20, 36, 60, 80], yticks=[-200, 200, 400])
p.func(R, xr=(1, 90), color=BLUE)
p.func(P, xr=(1, 90), color=GREEN)
p.segment(36, 0, 36, R(36), color=GRAY, width=1.2, dash=True)
p.point(36, R(36), color=BLUE)
p.point(36, P(36), color=GREEN, r=3.5)
p.point(xm, P(xm), color=RED)
p.text(36, R(36), "收益最大 (36, 432)", color=BLUE, anchor="middle", dy=-12)
p.text(xm, P(xm), "利潤最大 x ≈ 46.5", color=RED, dx=8, dy=-10)
p.text(88, R(88), "R(x)", color=BLUE, italic=True, anchor="end", dy=-10)
p.text(88, P(88), "Π(x)", color=GREEN, italic=True, anchor="end", dy=22)
p.save(out("fig-1101a-q5.svg"))

# 第 6 題：√(x² + x)，雙曲線的上半
f = lambda x: math.sqrt(x * x + x) if x * x + x >= 0 else None
p = Plot((-5, 4), (-1, 5), width=420)
p.axes(xticks=[-4, -3, -2, -1, 1, 2, 3], yticks=[1, 2, 3, 4])
p.line(1, 0, 0.5, color=GRAY, width=1.2, dash=True)
p.line(-1, 0, -0.5, color=GRAY, width=1.2, dash=True)
p.func(f, xr=(-5, -1), color=BLUE, n=2000)
p.func(f, xr=(0, 4), color=BLUE, n=2000)
p.point(-1, 0)
p.point(0, 0)
p.text(3.9, 4.4, "y = x + ½", color=GRAY, anchor="end", dy=-6)
p.text(-4.9, 4.4, "y = −x − ½", color=GRAY, dy=-6)
p.save(out("fig-1101a-q6.svg"))

# ---------------- 1101 期中（17-19 班） ----------------

# 第 6 題：6x − x² − 4 ln x，全貌與 [0.5, 3] 放大
f = lambda x: 6 * x - x * x - 4 * math.log(x) if x > 0 else None
r2 = math.sqrt(2)
p = Plot((-0.6, 7), (-9, 12), width=320, height=320, equal=False)
p.axes(xticks=[1, 2, 4, 6], yticks=[-5, 5, 10])
p.func(f, xr=(0.005, 7), color=BLUE, n=2000)
p.point(1, 5, color=GREEN, r=3.5)
p.point(2, f(2), color=RED, r=3.5)
p.text(0.15, 11, "x = 0 為垂直漸近線", color=GRAY, size=12)
p.save(out("fig-1101b-q6.svg"))
p = Plot((0.4, 3.1), (4.75, 5.45), width=320, height=320, equal=False)
p.axes(xticks=[1, (r2, "√2"), 2, 3], yticks=[5, (5.2, "5.2"), (5.4, "5.4")])
p.func(f, xr=(0.4, 3.1), color=BLUE)
p.point(1, 5, color=GREEN)
p.point(2, f(2), color=RED)
p.point(r2, f(r2), color=ORANGE)
p.text(1, 5, "極小 (1, 5)", color=GREEN, anchor="middle", dy=22)
p.text(2, f(2), "極大 (2, 8 − 4ln2)", color=RED, anchor="middle", dy=-12)
p.text(r2, f(r2), "反曲點", color=ORANGE, dx=6, dy=20)
p.save(out("fig-1101b-q6-zoom.svg"))

# 第 7 題：拋物線 y = x² 與 y = 2 之間的長方形
a = math.sqrt(2 / 3)
p = Plot((-2, 2), (-0.4, 2.6), width=360)
p.axes(xticks=[(-a, "−x"), (a, "x")], yticks=[2])
p.func(lambda x: x * x, color=BLUE)
p.segment(-2, 2, 2, 2, color=GRAY, width=1.4)
for x1, y1, x2, y2 in ((-a, a * a, a, a * a), (a, a * a, a, 2), (-a, a * a, -a, 2)):
    p.segment(x1, y1, x2, y2, color=RED, width=2)
p.segment(-a, 0, -a, a * a, color=GRAY, width=1, dash=True)
p.segment(a, 0, a, a * a, color=GRAY, width=1, dash=True)
p.point(a, a * a, color=RED, r=3.5)
p.text(a, a * a, sup("(x, x", "2") + ")", color=RED, dx=8, dy=14)
p.text(1.95, 2, "y = 2", color=GRAY, anchor="end", dy=-8)
p.text(1.2, 0.9, sup("y = x", "2"), color=BLUE, italic=True)
p.save(out("fig-1101b-q7.svg"))

# ---------------- 1091 期中 ----------------

# 第 7 題：ln|(2x+1)/(x−1)|
def f(x):
    v = abs((2 * x + 1) / (x - 1))
    return math.log(v) if v > 0 else None


L2 = math.log(2)
p = Plot((-8, 8), (-4, 5), width=440, height=300, equal=False)
p.axes(xticks=[-6, -4, -2, 2, 4, 6], yticks=[-2, 2, 4])
p.segment(-8, L2, 8, L2, color=GRAY, width=1.2, dash=True)
p.vline(-0.5, color=GRAY, width=1.2, dash=True)
p.vline(1, color=GRAY, width=1.2, dash=True)
p.func(f, xr=(-8, -0.5001), color=BLUE, n=3000)
p.func(f, xr=(-0.4999, 0.9999), color=BLUE, n=3000)
p.func(f, xr=(1.0001, 8), color=BLUE, n=3000)
p.point(-2, 0)
p.point(0, 0)
p.point(0.25, L2, color=ORANGE)
p.text(0.25, L2, "反曲點", color=ORANGE, dx=8, dy=18)
p.text(7.9, L2, "y = ln 2", color=GRAY, anchor="end", dy=-8)
p.text(-0.5, 4.6, "x = −½", color=GRAY, anchor="end", dx=-6, dy=4)
p.text(1, 4.6, "x = 1", color=GRAY, dx=6, dy=4)
p.save(out("fig-1091-q7.svg"))
