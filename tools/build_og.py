# -*- coding: utf-8 -*-
"""One 1200x630 Open Graph card, drawn with PyMuPDF. No stock art, no AI images."""
import sys
from pathlib import Path

PROD = Path(r"C:\Users\musol\Vault\01_Projects\Ecommerce_10K\products")
sys.path.insert(0, str(PROD))

import fitz
from ams_print import FONT_FILES, EMERALD, GOLD_LIGHT, CREAM, _c

W, H = 1200, 630
doc = fitz.open()
p = doc.new_page(width=W, height=H)

sh = p.new_shape()
sh.draw_rect(fitz.Rect(0, 0, W, H))
sh.finish(fill=EMERALD)
sh.commit()

sh = p.new_shape()
sh.draw_rect(fitz.Rect(40, 40, W - 40, H - 40))
sh.finish(color=GOLD_LIGHT, width=1.6)
sh.commit()


def txt(x, y, s, key, size, col, align="l"):
    f = fitz.Font(fontfile=str(FONT_FILES[key]))
    w = f.text_length(s, fontsize=size)
    if align == "c":
        x -= w / 2
    p.insert_text((x, y), s, fontname=f"f_{key}", fontfile=str(FONT_FILES[key]),
                  fontsize=size, color=col)
    return w


def tracked(cx, y, s, key, size, col, track):
    f = fitz.Font(fontfile=str(FONT_FILES[key]))
    total = sum(f.text_length(c, fontsize=size) for c in s) + track * (len(s) - 1)
    x = cx - total / 2
    for c in s:
        p.insert_text((x, y), c, fontname=f"f_{key}", fontfile=str(FONT_FILES[key]),
                      fontsize=size, color=col)
        x += f.text_length(c, fontsize=size) + track


tracked(W / 2, 200, "A MAISON SOIREE", "sans_sb", 26, GOLD_LIGHT, 7)
txt(W / 2, 300, "Guides", "gara_b", 82, CREAM, "c")
txt(W / 2, 358, "Notes from building printable party games", "sans", 26, CREAM, "c")

sh = p.new_shape()
sh.draw_line(fitz.Point(W / 2 - 160, 400), fitz.Point(W / 2 + 160, 400))
sh.finish(color=GOLD_LIGHT, width=1.2)
sh.commit()

txt(W / 2, 452, "Murder mysteries \u00b7 advent calendars \u00b7 mahjong", "sans", 22, _c(214, 205, 188), "c")
txt(W / 2, 508, "and a free four-player mystery to print", "gara_i", 26, GOLD_LIGHT, "c")

out = Path(__file__).resolve().parent.parent / "site" / "og.png"
p.get_pixmap(dpi=72, alpha=False).save(str(out))
print(out, out.stat().st_size, "bytes")
