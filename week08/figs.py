"""產生 Week 8 的圖：python week08/figs.py"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from svgplot import Plot, BLUE, RED, GREEN, GRAY  # noqa: E402


def out(name):
    return HERE / name


# 1. 羅必達的直覺：f, g 在 a 都是 0，放大後都像直線，比值 ≈ 斜率比
a = 1.0
f = lambda x: math.exp(x - a) - 1 + 0.15 * (x - a) ** 2   # f(a)=0, f'(a)=1
g = lambda x: 0.5 * math.sin(x - a) * 1.0 - 0.1 * (x - a) ** 3  # g(a)=0, g'(a)=0.5
p = Plot((-0.3, 2.6), (-1.1, 1.9), width=420)
p.axes(xticks=[(a, "a")], yticks=[])
p.line(1.0, a, 0, color=BLUE, width=1.2, dash=True)
p.line(0.5, a, 0, color=GREEN, width=1.2, dash=True)
p.func(f, xr=(-0.2, 2.5), color=BLUE)
p.func(g, xr=(-0.3, 2.6), color=GREEN)
p.point(a, 0, color=RED)
p.text(2.0, f(2.0), "y = f(x)", color=BLUE, italic=True, dx=-14, dy=-6, anchor="end")
p.text(2.5, g(2.5), "y = g(x)", color=GREEN, italic=True, dy=-10, anchor="end")
p.text(0.0, 1.7, "虛線：切線，斜率 f′(a)", color=BLUE, dx=8)
p.text(0.0, 1.45, "虛線：切線，斜率 g′(a)", color=GREEN, dx=8)
p.save(out("fig-idea.svg"))

# 2. 題 7：(x+cos x)/(x−cos x) → 1，但 (1−sin x)/(1+sin x) 一直亂跳
h = lambda x: (x + math.cos(x)) / (x - math.cos(x))
p = Plot((0, 40), (0, 2.2), width=400, height=240, equal=False)
p.axes(xticks=[10, 20, 30, 40], yticks=[1, 2])
p.segment(0, 1, 40, 1, color=GRAY, width=1.2, dash=True)
p.func(h, xr=(2.2, 40), color=BLUE, n=2000)
p.text(39, 1.75, "y = (x + cos x)/(x − cos x)", color=BLUE, italic=True, anchor="end", size=13)
p.save(out("fig-misuse2-a.svg"))

k = lambda x: min((1 - math.sin(x)) / (1 + math.sin(x)), 60)
p = Plot((0, 40), (0, 12), width=400, height=240, equal=False)
p.axes(xticks=[10, 20, 30, 40], yticks=[1, 5, 10])
p.func(k, xr=(0, 40), color=RED, n=6000)
p.text(39, 11, "y = (1 − sin x)/(1 + sin x)", color=RED, italic=True, anchor="end", size=13)
p.save(out("fig-misuse2-b.svg"))
