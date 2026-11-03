"""講義用的小型 SVG 函數繪圖工具。

用法（在 weekNN/figs.py 裡）：

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
    from svgplot import Plot, BLUE, RED

    p = Plot((-2, 2), (-1, 2))
    p.axes()
    p.func(lambda x: abs(x), color=BLUE)
    p.text(1.2, 1.5, "y = |x|", color=BLUE)
    p.save("fig-abs.svg")

座標一律用數學座標，工具負責換算成像素。曲線超出範圍的部分會被裁掉，
函數回傳 None 或 NaN 的地方會斷開。圖內建深色模式配色。
"""
import math
from pathlib import Path

BLUE = "#2f6fe4"
RED = "#e0483c"
GREEN = "#1f9d61"
ORANGE = "#e08a1e"
GRAY = "#8a93a3"

_STYLE = """<style>
.ax{stroke:#6b7280;stroke-width:1.2;fill:none}
.ah{fill:#6b7280}
.tk{stroke:#6b7280;stroke-width:1}
.tl{font:12px system-ui,sans-serif;fill:#6b7280}
.lb{font:15px "Times New Roman","Microsoft JhengHei",serif;fill:#1f2328}
.lb.it{font-style:italic}
.pt-open{fill:#fff}
@media (prefers-color-scheme:dark){
.ax{stroke:#9aa2ae}.ah{fill:#9aa2ae}.tk{stroke:#9aa2ae}.tl{fill:#9aa2ae}
.lb{fill:#e4e6ea}.pt-open{fill:#17191d}
}
</style>"""


def _f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Plot:
    def __init__(self, xr, yr, width=420, height=None, pad=26, equal=True):
        """xr, yr：數學座標範圍。equal=True 時 x、y 同比例（height 自動算）。"""
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr
        self.pad = pad
        self.w = width
        if height is None:
            if equal:
                inner = width - 2 * pad
                height = inner * (self.y1 - self.y0) / (self.x1 - self.x0) + 2 * pad
            else:
                height = width * 0.75
        self.h = height
        self.items = []

    # 座標換算
    def X(self, x):
        return self.pad + (x - self.x0) / (self.x1 - self.x0) * (self.w - 2 * self.pad)

    def Y(self, y):
        return self.h - self.pad - (y - self.y0) / (self.y1 - self.y0) * (self.h - 2 * self.pad)

    def axes(self, xticks=(), yticks=(), xlabel="x", ylabel="y"):
        """畫 x、y 軸（在 0 處，若 0 不在範圍則貼邊），可加刻度。"""
        ay = min(max(0, self.y0), self.y1)
        ax = min(max(0, self.x0), self.x1)
        L, R = self.pad - 8, self.w - self.pad + 8
        T, B = self.pad - 8, self.h - self.pad + 8
        Yp, Xp = self.Y(ay), self.X(ax)
        out = [
            f'<line class="ax" x1="{_f(L)}" y1="{_f(Yp)}" x2="{_f(R)}" y2="{_f(Yp)}"/>',
            f'<path class="ah" d="M{_f(R + 6)},{_f(Yp)} l-9,-4 v8 z"/>',
            f'<line class="ax" x1="{_f(Xp)}" y1="{_f(B)}" x2="{_f(Xp)}" y2="{_f(T)}"/>',
            f'<path class="ah" d="M{_f(Xp)},{_f(T - 6)} l-4,9 h8 z"/>',
            f'<text class="lb it" x="{_f(R + 2)}" y="{_f(Yp + 18)}" text-anchor="end">{xlabel}</text>',
            f'<text class="lb it" x="{_f(Xp - 8)}" y="{_f(T + 4)}" text-anchor="end">{ylabel}</text>',
        ]
        for t in xticks:
            v, s = (t if isinstance(t, tuple) else (t, _f(t)))
            px = self.X(v)
            out.append(f'<line class="tk" x1="{_f(px)}" y1="{_f(Yp - 3)}" x2="{_f(px)}" y2="{_f(Yp + 3)}"/>')
            out.append(f'<text class="tl" x="{_f(px)}" y="{_f(Yp + 16)}" text-anchor="middle">{_esc(s)}</text>')
        for t in yticks:
            v, s = (t if isinstance(t, tuple) else (t, _f(t)))
            py = self.Y(v)
            out.append(f'<line class="tk" x1="{_f(Xp - 3)}" y1="{_f(py)}" x2="{_f(Xp + 3)}" y2="{_f(py)}"/>')
            out.append(f'<text class="tl" x="{_f(Xp - 6)}" y="{_f(py + 4)}" text-anchor="end">{_esc(s)}</text>')
        self.items.extend(out)
        return self

    def func(self, f, xr=None, color=BLUE, width=2.2, dash=False, n=800):
        """畫 y=f(x)。f 回傳 None/NaN 或相鄰點跳太大時斷開。"""
        a, b = xr if xr else (self.x0, self.x1)
        jump = (self.y1 - self.y0) * 1.5
        segs, cur, prev = [], [], None
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError, OverflowError):
                y = None
            if y is None or (isinstance(y, float) and math.isnan(y)) or (prev is not None and abs(y - prev) > jump):
                if len(cur) > 1:
                    segs.append(cur)
                cur = [] if y is None or (isinstance(y, float) and math.isnan(y)) else [(x, y)]
                prev = None if not cur else y
                continue
            cur.append((x, y))
            prev = y
        if len(cur) > 1:
            segs.append(cur)
        d = " ".join(
            "M" + " L".join(f"{_f(self.X(x))},{_f(self.Y(y))}" for x, y in s) for s in segs
        )
        self.items.append(self._path(d, color, width, dash))
        return self

    def segment(self, x1, y1, x2, y2, color=GRAY, width=1.6, dash=False):
        d = f"M{_f(self.X(x1))},{_f(self.Y(y1))} L{_f(self.X(x2))},{_f(self.Y(y2))}"
        self.items.append(self._path(d, color, width, dash))
        return self

    def line(self, slope, x0, y0, color=RED, width=1.8, dash=False):
        """過 (x0, y0)、斜率 slope 的直線，延伸到整個 x 範圍。"""
        return self.segment(self.x0, y0 + slope * (self.x0 - x0),
                            self.x1, y0 + slope * (self.x1 - x0), color, width, dash)

    def vline(self, x, color=RED, width=1.8, dash=False):
        return self.segment(x, self.y0, x, self.y1, color, width, dash)

    def point(self, x, y, color=BLUE, open=False, r=4):
        cls = ' class="pt-open"' if open else f' fill="{color}"'
        self.items.append(
            f'<circle cx="{_f(self.X(x))}" cy="{_f(self.Y(y))}" r="{r}"{cls} stroke="{color}" stroke-width="2"/>'
        )
        return self

    def text(self, x, y, s, color=None, anchor="start", italic=False, dx=0, dy=0, size=None):
        """在 (x, y) 寫字。s 可含 <tspan> 標記，例如 sup('x', '1/5')。"""
        cls = "lb it" if italic else "lb"
        css = ";".join(([f"fill:{color}"] if color else []) + ([f"font-size:{size}px"] if size else []))
        style = f' style="{css}"' if css else ""
        self.items.append(
            f'<text class="{cls}" x="{_f(self.X(x) + dx)}" y="{_f(self.Y(y) + dy)}" text-anchor="{anchor}"{style}>{s}</text>'
        )
        return self

    def _path(self, d, color, width, dash):
        da = ' stroke-dasharray="6 5"' if dash else ""
        return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
                f'stroke-linejoin="round" stroke-linecap="round"{da} clip-path="url(#clip)"/>')

    def svg(self):
        W, H = _f(self.w), _f(self.h)
        cx, cy = _f(self.pad - 2), _f(self.pad - 2)
        cw, ch = _f(self.w - 2 * self.pad + 4), _f(self.h - 2 * self.pad + 4)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f"{_STYLE}"
            f'<defs><clipPath id="clip"><rect x="{cx}" y="{cy}" width="{cw}" height="{ch}"/></clipPath></defs>'
            + "".join(self.items)
            + "</svg>\n"
        )

    def save(self, path):
        Path(path).write_text(self.svg(), encoding="utf-8")
        return self


def sup(base, exp):
    """上標文字，例如 sup('x', '1/5') → x^(1/5)。"""
    return f'{base}<tspan dy="-7" font-size="11">{_esc(exp)}</tspan><tspan dy="7"> </tspan>'
