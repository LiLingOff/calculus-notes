"""產生 Week 16-2 的圖：python week16-2/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, sup, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


def taylor(coef, k):
    """coef(j) 為 x^j 的係數，回傳前 k+1 項的多項式（T_k）。"""
    return lambda x: sum(coef(j) * x ** j for j in range(k + 1))


# 1. e^x 與泰勒多項式 T1、T2、T3
ex = lambda j: 1 / math.factorial(j)
p = Plot((-3, 2.2), (-1.5, 7), width=420, height=320, equal=False)
p.axes(xticks=[-2, -1, 1, 2], yticks=[2, 4, 6])
p.func(taylor(ex, 1), color=GREEN, width=1.6)
p.func(taylor(ex, 2), color=ORANGE, width=1.6)
p.func(taylor(ex, 3), color=RED, width=1.6)
p.func(math.exp, color=BLUE, width=2.6)
p.text(1.1, 6.3, sup("y = e", "x"), color=BLUE, italic=True, anchor="end")
p.text(-2.9, -0.9, "T₁", color=GREEN)
p.text(-2.4, 3.2, "T₂", color=ORANGE)
p.text(-1.85, -1.2, "T₃", color=RED)
p.save(out("fig-exp.svg"))

# 2. sin x 與 T1、T3、T5、T7：項數越多，貼合的範圍越寬
def sc(j):
    if j % 2 == 0:
        return 0
    return (-1) ** ((j - 1) // 2) / math.factorial(j)

p = Plot((-7, 7), (-2.2, 2.2), width=460, height=230, equal=False)
p.axes(xticks=[(-math.pi, "−π"), (math.pi, "π"), (2 * math.pi, "2π"), (-2 * math.pi, "−2π")], yticks=[1, -1])
for k, c in [(1, GREEN), (3, ORANGE), (5, RED), (7, GRAY)]:
    p.func(taylor(sc, k), color=c, width=1.5)
p.func(math.sin, color=BLUE, width=2.6)
p.text(2.15, 1.9, "T₁", color=GREEN)
p.text(3.15, -2.0, "T₃", color=ORANGE)
p.text(4.25, 2.0, "T₅", color=RED)
p.text(5.2, -2.0, "T₇", color=GRAY)
p.text(-5.0, 1.3, "y = sin x", color=BLUE, italic=True)
p.save(out("fig-sin.svg"))

# 3. ln(1+x) 與部分和：x 超過 1 時部分和亂跳
lc = lambda j: 0 if j == 0 else (-1) ** (j - 1) / j
p = Plot((-1.3, 1.9), (-2.6, 1.6), width=420, height=300, equal=False)
p.vline(1, color=GRAY, dash=True, width=1.1)
p.vline(-1, color=GRAY, dash=True, width=1.1)
p.axes(xticks=[(-1, "−1"), 1], yticks=[1, -1, -2])
p.func(taylor(lc, 4), color=ORANGE, width=1.5)
p.func(taylor(lc, 5), color=RED, width=1.5)
p.func(taylor(lc, 12), color=GREEN, width=1.5)
p.func(lambda x: math.log(1 + x) if x > -1 else None, xr=(-0.999, 1.9), color=BLUE, width=2.6)
p.text(-0.95, 1.1, "y = ln(1+x)", color=BLUE, italic=True)
p.text(1.47, -2.3, "T₄", color=ORANGE)
p.text(1.62, 1.3, "T₅", color=RED)
p.text(1.18, -2.3, "T₁₂", color=GREEN)
p.save(out("fig-ln.svg"))

# 4. 反例 g(x) = e^(-1/x)（x>0）：在 0 附近平到所有導數都是 0
g = lambda x: math.exp(-1 / x) if x > 0 else 0.0
p = Plot((-1.5, 4), (-0.25, 1.05), width=420, height=240, equal=False)
p.segment(-1.5, 1, 4, 1, color=GRAY, dash=True, width=1)
p.axes(xticks=[1, 2, 3], yticks=[1])
p.func(g, color=BLUE, n=1200)
p.text(2.0, 0.42, sup("y = e", "−1/x"), color=BLUE, italic=True)
p.text(-1.4, 0.15, "y = 0", color=BLUE, italic=True)
p.text(0.1, 0.8, "泰勒級數 ≡ 0", color=RED, size=13)
p.save(out("fig-flat.svg"))

print("ok")
