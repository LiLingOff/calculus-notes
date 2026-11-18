"""產生 Week 15 的圖：python week15/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, _f, BLUE, RED, GREEN, ORANGE, GRAY  # noqa: E402


def out(name):
    return HERE / name


def slope_field(p, F, xs, ys, L=0.32, color=GRAY):
    """在格點畫斜率場的小線段；L 是線段在像素比例下的長度（數學單位，粗略）。"""
    sx = (p.w - 2 * p.pad) / (p.x1 - p.x0)
    sy = (p.h - 2 * p.pad) / (p.y1 - p.y0)
    for x in xs:
        for y in ys:
            m = F(x, y)
            # 讓每段在畫面上一樣長
            dx = 1 / math.hypot(sx, m * sy)
            h = L * sx * dx / 2
            p.segment(x - h, y - m * h, x + h, y + m * h, color=color, width=1.1)


def arrow(p, x, y, direction, color):
    """在 (x, y) 畫一個水平小箭頭，direction=+1 向右、-1 向左。"""
    X, Y = p.X(x), p.Y(y)
    d = f"M{_f(X + 7 * direction)},{_f(Y)} l{_f(-12 * direction)},-6 v12 z"
    p.items.append(f'<path d="{d}" fill="{color}"/>')


def varrow(p, x, y, direction, color):
    """在 (x, y) 畫一個垂直小箭頭，direction=+1 向上、-1 向下。"""
    X, Y = p.X(x), p.Y(y)
    d = f"M{_f(X)},{_f(Y - 7 * direction)} l-6,{_f(12 * direction)} h12 z"
    p.items.append(f'<path d="{d}" fill="{color}"/>')


# 1. y' = y 的解族 y = c e^x，加上初值 y(0)=6 只剩一條
p = Plot((-3, 2.2), (-4.5, 8.5), width=400, height=300, equal=False)
p.axes(yticks=[6])
for c in (-2, -1, 1, 2, 3, 4):
    p.func(lambda x, c=c: c * math.exp(x), color=GRAY, width=1.4)
p.func(lambda x: 6 * math.exp(x), color=BLUE, width=2.6)
p.point(0, 6, color=BLUE)
p.text(-2.9, 7.4, "y = 6eˣ（過 (0, 6)）", color=BLUE, size=14)
p.text(1.5, -3.6, "c &lt; 0", color=GRAY, size=13)
p.save(out("fig-family.svg"))

# 2. 相平面：w = y² − 3y + 2，y 軸上標出 y 的移動方向
p = Plot((-0.6, 3.6), (-0.8, 2.6), width=380, height=280, equal=False)
p.axes(xticks=[1, 2, 3], yticks=[2], xlabel="y", ylabel="w = y′")
p.func(lambda y: y * y - 3 * y + 2, color=BLUE)
p.point(1, 0, color=RED)
p.point(2, 0, color=RED)
for x, d in ((0.2, 1), (0.65, 1), (1.6, -1), (2.45, 1), (3.35, 1)):
    arrow(p, x, 0, d, ORANGE)
p.text(3.3, 2.2, "w = y² − 3y + 2", color=BLUE, anchor="end", size=14)
p.text(1.5, -0.55, "w &lt; 0：y 變小", color=ORANGE, anchor="middle", size=13)
p.save(out("fig-phase.svg"))

# 3. 同一方程不同初值的解 y(t)
p = Plot((-0.3, 4.2), (-0.6, 3.8), width=380, height=280, equal=False)
p.axes(xticks=[(math.log(2), "ln2"), 2, 4], yticks=[1, 2, 3], xlabel="t", ylabel="y")
p.segment(0, 1, 4.2, 1, color=RED, width=2)
p.segment(0, 2, 4.2, 2, color=RED, width=1.6, dash=True)
p.vline(math.log(2), color=GRAY, dash=True, width=1.1)
p.func(lambda t: (2 + math.exp(t)) / (1 + math.exp(t)), xr=(0, 4.2), color=BLUE)
p.func(lambda t: (2 * math.exp(t) - 2) / (2 * math.exp(t) - 1), xr=(0, 4.2), color=GREEN)
p.func(lambda t: (4 - math.exp(t)) / (2 - math.exp(t)), xr=(0, math.log(2) - 0.004), color=ORANGE)
p.text(2.5, 1.18, "y(0)=3/2", color=BLUE, size=13)
p.text(2.5, 0.55, "y(0)=0", color=GREEN, size=13)
p.text(0.9, 3.4, "y(0)=3", color=ORANGE, size=13)
p.text(4.1, 2.12, "y ≡ 2", color=RED, anchor="end", size=13)
p.save(out("fig-phase-sol.svg"))

# 4. Interval of validity：y' = −y² 的斜率場，過 (1,1) 的解只有右支
p = Plot((-3.2, 3.2), (-3.2, 3.2), width=380)
F = lambda x, y: -y * y
grid = [i * 0.5 for i in range(-6, 7)]
slope_field(p, F, grid, grid, L=0.34)
p.axes(xticks=[1], yticks=[1])
p.func(lambda x: 1 / x, xr=(-3.2, -0.01), color=BLUE, width=1.8, dash=True)
p.func(lambda x: 1 / x, xr=(0.01, 3.2), color=BLUE, width=2.6)
p.point(1, 1, color=RED)
p.text(1.1, 1.25, "P(1, 1)", color=RED, size=13)
p.text(3.1, 1.5, "y = 1/x, x &gt; 0", color=BLUE, anchor="end", size=13)
p.text(-3.0, 2.75, "左支不是這題的解", color=BLUE, size=13)
p.save(out("fig-validity.svg"))

print("ok")
