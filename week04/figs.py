"""產生 Week 4 的圖：python week04/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, BLUE, RED, GREEN, GRAY  # noqa: E402


def out(name):
    return HERE / name


# 1. 割線逼近切線
f = lambda x: 0.3 * x * x + 0.5
a = 1
p = Plot((-0.6, 4), (-0.4, 4.2), width=440)
p.axes(xticks=[(a, "a")])
p.func(f, color=BLUE)
for b, op in ((3.2, 1), (2.2, 0.75)):
    s = (f(b) - f(a)) / (b - a)
    p.line(s, a, f(a), color=GRAY, width=1.4, dash=True)
    p.point(b, f(b), color=GRAY)
p.line(0.6, a, f(a), color=RED, width=2)
p.point(a, f(a), color=RED)
p.segment(a, f(a), 3.2, f(a), color=GREEN, width=1.2, dash=True)
p.segment(3.2, f(a), 3.2, f(3.2), color=GREEN, width=1.2, dash=True)
p.text(2.1, f(a), "h", color=GREEN, italic=True, anchor="middle", dy=18)
p.text(3.2, 1.35, "f(a+h) − f(a)", color=GREEN, dx=6, size=13)
p.text(a, f(a), "P", color=RED, italic=True, dx=-6, dy=-10, anchor="end")
p.text(3.2, f(3.2), "Q", italic=True, dx=-10, dy=-2, anchor="end")
p.text(3.6, 2.55, "切線", color=RED, anchor="middle", dy=10)
p.text(2.55, 3.95, "割線（Q 往 P 靠近）", color=GRAY, anchor="middle")
p.save(out("fig-secant.svg"))

# 2. y = x^(1/5)：原點垂直切線
p = Plot((-2.2, 2.2), (-1.6, 1.6), width=380)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-1, 1])
p.vline(0, color=RED, width=2.4, dash=True)
p.func(lambda x: math.copysign(abs(x) ** 0.2, x), color=BLUE, n=2000)
p.text(1.0, 1.25, "y = " + sup("x", "1/5"), color=BLUE, italic=True)
p.text(0.12, -1.35, "切線垂直", color=RED)
p.save(out("fig-x15.svg"))

# 3. y = |x|：尖點
p = Plot((-2.2, 2.2), (-0.6, 2.4), width=380)
p.axes(xticks=[-2, -1, 1, 2], yticks=[1, 2])
p.func(abs, color=BLUE)
p.point(0, 0, color=RED)
p.text(-1.35, 1.75, "斜率 −1", color=BLUE, anchor="middle")
p.text(1.35, 1.75, "斜率 1", color=BLUE, anchor="middle")
p.text(0.9, 0.3, "y = |x|", color=BLUE, italic=True)
p.save(out("fig-abs.svg"))

# 4. x sin(1/x) 與 x² sin(1/x)
sx = lambda x: x * math.sin(1 / x) if x else 0.0
p = Plot((-0.42, 0.42), (-0.42, 0.42), width=340)
p.axes()
p.func(abs, color=GRAY, width=1.2, dash=True)
p.func(lambda x: -abs(x), color=GRAY, width=1.2, dash=True)
p.func(sx, color=BLUE, width=1.6, n=6000)
p.text(0.0, 0.42, "y = x sin(1/x)", color=BLUE, italic=True, anchor="middle", dy=14)
p.text(0.4, 0.4, "y = |x|", color=GRAY, italic=True, anchor="end", dy=22, size=13)
p.save(out("fig-xsin.svg"))

s2 = lambda x: x * x * math.sin(1 / x) if x else 0.0
p = Plot((-0.42, 0.42), (-0.15, 0.15), width=340, height=340, equal=False)
p.axes()
p.func(lambda x: x * x, color=GRAY, width=1.2, dash=True)
p.func(lambda x: -x * x, color=GRAY, width=1.2, dash=True)
p.func(s2, color=BLUE, width=1.6, n=6000)
p.text(0.0, 0.15, "y = " + sup("x", "2") + "sin(1/x)", color=BLUE, italic=True, anchor="middle", dy=14)
p.text(0.4, 0.14, "y = " + sup("x", "2"), color=GRAY, italic=True, anchor="end", dy=36, size=13)
p.save(out("fig-x2sin.svg"))

# 5. 題 15：f(x) = x⁴eˣ + 3x + 2 在 x=0 的切線與法線
g = lambda x: x ** 4 * math.exp(x) + 3 * x + 2
p = Plot((-2.2, 2.2), (-1, 4.4), width=400)
p.axes(xticks=[-2, -1, 1, 2], yticks=[1, 2, 3, 4])
p.func(g, color=BLUE)
p.line(3, 0, 2, color=RED)
p.line(-1 / 3, 0, 2, color=GREEN)
p.point(0, 2, color=BLUE)
p.text(-1.1, 3.9, "y = f(x)", color=BLUE, italic=True, anchor="middle")
p.text(0.2, 1.3, "切線 y = 3x + 2", color=RED)
p.text(-2.1, 2.95, "法線 y = −x/3 + 2", color=GREEN)
p.save(out("fig-tangent-normal.svg"))

print("ok")
