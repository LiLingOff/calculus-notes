"""產生 Week 1 的圖：python week01/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402

PI = math.pi


def out(name):
    return HERE / name


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


# 1. 題 1：y = sin x
p = Plot((-7, 7), (-1.6, 1.6), width=460, height=170, equal=False)
p.axes(xticks=[(-2 * PI, "−2π"), (-PI, "−π"), (PI, "π"), (2 * PI, "2π")], yticks=[-1, 1])
p.func(math.sin, color=BLUE)
p.text(PI / 2, 1, "y = sin x", color=BLUE, italic=True, anchor="middle", dy=-8)
p.save(out("fig-sin.svg"))

# 2. 題 2：分段函數
p = Plot((-3.2, 3.2), (-4.2, 3.2), width=320)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-3, -2, -1, 1, 2])
p.func(lambda x: 1 / x if x > 0 else None, xr=(0.01, 3.2), color=BLUE)
p.func(lambda x: x - 1, xr=(-3.2, 0), color=BLUE)
p.point(0, -1, color=BLUE)
p.text(0.75, 2.4, "y = 1/x", color=BLUE, italic=True)
p.text(-1.4, -1.6, "y = x − 1", color=BLUE, italic=True, anchor="end")
p.save(out("fig-piecewise.svg"))

# 3. 題 3：y = |x|
p = Plot((-2.2, 2.2), (-0.6, 2.4), width=320)
p.axes(xticks=[-2, -1, 1, 2], yticks=[1, 2])
p.func(abs, color=BLUE)
p.text(0.9, 0.3, "y = |x|", color=BLUE, italic=True)
p.save(out("fig-abs.svg"))

# 4. 指數函數在 (0, 1) 的切線：2ˣ、eˣ、3ˣ
p = Plot((-2.2, 1.8), (-0.6, 4.4), width=380)
p.axes(xticks=[-2, -1, 1], yticks=[1, 2, 3, 4])
for base, col in ((2, GREEN), (math.e, BLUE), (3, ORANGE)):
    p.func(lambda x, b=base: b ** x, color=col, width=1.8)
p.line(1, 0, 1, color=RED, width=1.6, dash=True)
p.point(0, 1, color=RED)
p.text(-0.25, 4.0, "y = " + sup("3", "x"), color=ORANGE, italic=True, anchor="end")
p.text(-0.25, 3.5, "y = " + sup("e", "x"), color=BLUE, italic=True, anchor="end")
p.text(-0.25, 3.0, "y = " + sup("2", "x"), color=GREEN, italic=True, anchor="end")
p.text(0.15, 0.55, "斜率 1", color=RED)
p.save(out("fig-exp-tangent.svg"))

# 5. 題 4：比較 a, b, c, d（重畫講義的圖，底取 a=1/2, b=1/6, c=3, d=1.6）
p = Plot((-3, 3), (-0.6, 4.6), width=360)
p.axes()
p.func(lambda x: 0.5 ** x, color=GREEN)
p.func(lambda x: (1 / 6) ** x, color=BLUE)
p.func(lambda x: 3 ** x, color=RED)
p.func(lambda x: 1.6 ** x, color=GRAY)
p.text(-2.0, 2.4, "y = " + sup("a", "x"), color=GREEN, italic=True, anchor="end")
p.text(-1.45, 4.3, "y = " + sup("b", "x"), color=BLUE, italic=True, anchor="middle")
p.text(1.45, 4.2, "y = " + sup("c", "x"), color=RED, italic=True)
p.text(2.95, 2.3, "y = " + sup("d", "x"), color=GRAY, italic=True, anchor="end")
p.save(out("fig-exp-compare.svg"))

# 6. 題 5：比較對數的底（照講義的圖：a=1/2, b=2/3, c=2）
p = Plot((-0.3, 3.3), (-2.2, 2.2), width=320)
p.axes(xticks=[1, 2, 3], yticks=[-2, -1, 1, 2])
p.func(lambda x: math.log(x) / math.log(0.5) if x > 0 else None, xr=(0.005, 3.3), color=GREEN)
p.func(lambda x: math.log(x) / math.log(2 / 3) if x > 0 else None, xr=(0.005, 3.3), color=BLUE)
p.func(lambda x: math.log(x, 2) if x > 0 else None, xr=(0.005, 3.3), color=RED)
p.point(0.8, math.log(0.8) / math.log(2 / 3), color=BLUE)
p.point(4 / 3, math.log(4 / 3) / math.log(0.5), color=GREEN)
p.point(1 / 3, math.log(1 / 3, 2), color=RED)
p.text(0.8, 0.55, "(0.8, 0.55)", color=BLUE, dx=8, dy=-2, size=12)
p.text(4 / 3, -0.415, "(1.333, −0.415)", color=GREEN, dx=8, dy=4, size=12)
p.text(1 / 3, -1.585, "(0.333, −1.585)", color=RED, dx=8, dy=4, size=12)
p.save(out("fig-log-compare.svg"))

# 7. 1.3.2：f(x) = x³ + 1 與反函數
p = Plot((-3.2, 3.2), (-3.2, 3.2), width=340)
p.axes(xticks=[-2, -1, 1, 2], yticks=[-2, -1, 1, 2])
p.func(lambda x: x, color=GRAY, width=1.2, dash=True)
p.func(lambda x: x ** 3 + 1, color=GREEN)
p.func(lambda x: cbrt(x - 1), color=BLUE)
p.text(-0.35, 2.7, "y = " + sup("x", "3") + "+ 1", color=GREEN, italic=True, anchor="end")
p.text(3.1, 0.25, "y = ∛(x − 1)", color=BLUE, italic=True, anchor="end")
p.text(2.3, 3.0, "y = x", color=GRAY, italic=True, anchor="end")
p.save(out("fig-inverse.svg"))

# 8. 題 10：y = x² 被水平線切兩次
p = Plot((-2.2, 2.2), (-0.6, 3.2), width=320)
p.axes(xticks=[-2, -1, 1, 2], yticks=[1, 2, 3])
p.func(lambda x: x * x, color=BLUE)
p.segment(-2.2, 1, 2.2, 1, color=RED, width=1.6, dash=True)
p.point(-1, 1, color=RED)
p.point(1, 1, color=RED)
p.text(1.55, 2.4, "y = " + sup("x", "2"), color=BLUE, italic=True, anchor="end")
p.text(2.1, 1, "y = 1", color=RED, italic=True, anchor="end", dy=-8)
p.save(out("fig-x2-hlt.svg"))

# 9. 題 12：一對一但不單調
p = Plot((-0.4, 2.4), (-0.4, 2.4), width=300)
p.axes(xticks=[1, 2], yticks=[1, 2])
p.func(lambda x: 1 - x, xr=(0, 1), color=BLUE)
p.func(lambda x: x, xr=(1, 2), color=BLUE)
p.point(0, 1, color=BLUE)
p.point(1, 0, color=BLUE)
p.point(1, 1, color=BLUE, open=True)
p.point(2, 2, color=BLUE)
p.save(out("fig-1to1.svg"))

# 10. 1.5：sin 限制在 [−π/2, π/2]，與 arcsin
p = Plot((-3.6, 3.6), (-1.9, 1.9), width=400)
p.axes(xticks=[(-PI / 2, "−π/2"), (PI / 2, "π/2"), (-PI, "−π"), (PI, "π")], yticks=[-1, 1])
p.func(lambda x: x, color=GRAY, width=1.2, dash=True)
p.func(math.sin, color=GRAY, width=1.4)
p.func(math.sin, xr=(-PI / 2, PI / 2), color=GREEN, width=2.6)
p.func(lambda x: math.asin(x) if abs(x) <= 1 else None, xr=(-1, 1), color=BLUE, n=2000)
p.text(-2.65, -1.55, "y = sin x", color=GREEN, italic=True, anchor="middle")
p.text(-0.3, 1.45, "y = arcsin x", color=BLUE, italic=True, anchor="end")
p.save(out("fig-arcsin.svg"))

# 11. 題 13：cos 限制在 [0, π]，與 arccos
p = Plot((-1.6, 3.6), (-1.6, 3.6), width=360)
p.axes(xticks=[-1, 1, (PI / 2, "π/2"), (PI, "π")], yticks=[-1, 1, (PI / 2, "π/2"), (PI, "π")])
p.func(lambda x: x, color=GRAY, width=1.2, dash=True)
p.func(math.cos, xr=(0, PI), color=GREEN)
p.func(lambda x: math.acos(x) if abs(x) <= 1 else None, xr=(-1, 1), color=BLUE, n=2000)
p.point(-1, PI, color=BLUE)
p.point(1, 0, color=BLUE)
p.text(-1, PI, "(−1, π)", color=BLUE, anchor="middle", dy=-12)
p.text(2.6, -1, "y = cos x", color=GREEN, italic=True, anchor="middle", dy=22)
p.text(-0.55, 1.2, "y = arccos x", color=BLUE, italic=True, anchor="end", size=13)
p.save(out("fig-arccos.svg"))

print("ok")
