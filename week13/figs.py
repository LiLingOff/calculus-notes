"""產生 Week 13 的圖：python week13/figs.py"""
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


# 1. 分部積分的面積意義：∫v du + ∫u dv = 大矩形 − 小矩形
g = lambda u: u * u / 4 + 0.75          # 曲線 v = g(u)，u 從 1 到 3，v 從 1 到 3
U1, U2 = 1, 3
V1, V2 = g(U1), g(U2)
n = 120
curve = [(U1 + (U2 - U1) * i / n, g(U1 + (U2 - U1) * i / n)) for i in range(n + 1)]
p = Plot((-0.3, 3.8), (-0.3, 3.6), width=380)
region(p, [(U1, 0)] + curve + [(U2, 0)], BLUE, 0.22)
region(p, [(0, V1)] + curve + [(0, V2)], RED, 0.22)
p.segment(U1, 0, U1, V1, color=GRAY, dash=True, width=1.2)
p.segment(U2, 0, U2, V2, color=GRAY, dash=True, width=1.2)
p.segment(0, V1, U1, V1, color=GRAY, dash=True, width=1.2)
p.segment(0, V2, U2, V2, color=GRAY, dash=True, width=1.2)
p.axes(xticks=[(U1, "u(a)"), (U2, "u(b)")], yticks=[(V1, "v(a)"), (V2, "v(b)")], xlabel="u", ylabel="v")
p.func(g, xr=(U1, U2), color=GRAY, width=2.4)
p.text(2.05, 0.75, "∫ v du", color=BLUE, anchor="middle", italic=True)
p.text(0.75, 2.35, "∫ u dv", color=RED, anchor="middle", italic=True)
p.save(out("fig-ibp.svg"))


# 2. 三角代換的三種三角形
def tri(p, ox, base, height, labels, theta_at_left=True):
    """直角在右下的三角形：左下角 (ox,0)，右下 (ox+base,0)，右上 (ox+base,height)。"""
    A, B, C = (ox, 0), (ox + base, 0), (ox + base, height)
    for (x1, y1), (x2, y2) in [(A, B), (B, C), (C, A)]:
        p.segment(x1, y1, x2, y2, color=BLUE, width=2)
    s = 0.18
    p.segment(B[0] - s, 0, B[0] - s, s, color=GRAY, width=1.2)
    p.segment(B[0] - s, s, B[0], s, color=GRAY, width=1.2)
    hyp, opp, adj, title = labels
    p.text(ox + 0.42, 0.12, "θ", color=RED, italic=True)
    p.text(ox + base / 2 - 0.15, height / 2 + 0.12, hyp, anchor="end", size=13)
    p.text(B[0] + 0.1, height / 2, opp, size=13, dy=4)
    p.text(ox + base / 2, -0.32, adj, anchor="middle", size=13)
    p.text(ox + base / 2, height + 0.45, title, anchor="middle", color=GRAY, size=13)


p = Plot((-0.3, 11.6), (-0.7, 2.9), width=640)
tri(p, 0.0, 2.2, 1.6, ("a", "x", "√(a²−x²)", "x = a sin θ"))
tri(p, 4.2, 2.2, 1.6, ("√(a²+x²)", "x", "a", "x = a tan θ"))
tri(p, 8.2, 2.2, 1.6, ("x", "√(x²−a²)", "a", "x = a sec θ"))
p.save(out("fig-trig.svg"))
