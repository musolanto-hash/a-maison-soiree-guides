# -*- coding: utf-8 -*-
"""Builds the two PDFs of the free mini mystery, on the shop's own print engine.

  the-wet-half-hour.pdf         the whole game, and no answer anywhere in it
  the-wet-half-hour-answer.pdf  the sealed reveal, behind a full-page STOP

Same rules as the paid products: union canvas so US Letter and A4 come out of one
layout at 100%, live vector text in embedded fonts, nothing below 11 pt, pure black
body ink on white, no text over an image (there are no images).
"""
from __future__ import annotations

import sys
from pathlib import Path

PROD = Path(r"C:\Users\musol\Vault\01_Projects\Ecommerce_10K\products")
sys.path.insert(0, str(PROD))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import fitz
import ams_print as AP
from ams_print import (Book, Theme, CANVAS_W, X0, X1, Y0, Y1, tw, F,
                       EMERALD, GOLD, GOLD_LIGHT, CREAM, INK, INK_SOFT, BLACK, _c)
import game_text as T

FONTS = Path(r"C:\Users\musol\Vault\01_Projects\Ecommerce_10K\Product_Advent\fonts")
AP.FONT_FILES.update({
    "type":   FONTS / "CourierPrime-Regular.ttf",
    "type_b": FONTS / "CourierPrime-Bold.ttf",
    "hand":   FONTS / "Kalam-Regular.ttf",
    "hand_b": FONTS / "Kalam-Bold.ttf",
})

GREY = _c(120, 120, 120)
HAIR = _c(165, 165, 165)
RULE = _c(95, 95, 95)

MYST = Theme("Mystery", EMERALD, CREAM, EMERALD, GOLD, HAIR, INK, INK_SOFT, _c(246, 244, 238), False)

L = X0 + 20          # 56
R = X1 - 20          # 539.28
W = R - L            # 483.28
TOP = Y0 + 22        # 58
BOT = Y1 - 40        # 716  (body must stop here)

SITE = "amaisonsoiree.github.io"   # replaced at build time with the real host
FOOT = "The Wet Half-Hour \u00b7 a free mini mystery from A Maison Soir\u00e9e"


# --------------------------------------------------------------------- page helpers
MINPT = 11.0          # nothing printed may be smaller than this


def footer(sh, note=None):
    y = Y1 - 30
    sh.line(L, y, R, y, HAIR, 0.6)
    sh.text(L, y + 15, FOOT, "gara_i", MINPT, GREY)
    if note:
        sh.text(R, y + 15, note, "sans", MINPT, GREY, "r")


def kicker(sh, x, y, s, color, track=2.0, align="l", maxw=None, size=MINPT, key="sans_sb"):
    """Letter-spaced small caps that never outgrow the column: the tracking gives way, not the size."""
    maxw = maxw or W
    while track > 0.3 and sum(tw(c, key, size) for c in s) + track * (len(s) - 1) > maxw:
        track -= 0.1
    return sh.tracked(x, y, s, key, size, color, track, align)


class Flow:
    """Auto-paginating block renderer."""

    def __init__(self, book, cont_title=None):
        self.book = book
        self.cont = cont_title
        self.sh = None
        self.y = 0
        self.page_no = 0

    def newpage(self, first=False):
        self.sh = self.book.page()
        self.page_no += 1
        self.y = TOP
        if not first and self.cont:
            self.sh.text(L, self.y + 11, f"{self.cont} (continued)", "sans_i", MINPT, GREY)
            self.y += 28
        return self.sh

    def need(self, h):
        if self.sh is None:
            self.newpage(first=True)
        if self.y + h > BOT:
            footer(self.sh)
            self.newpage()

    # ---- primitives -------------------------------------------------
    def para(self, s, key="serif", size=12, lead=None, color=INK, indent=0, maxw=None, keep=True):
        lead = lead or size * 1.46
        maxw = maxw or (W - indent)
        if self.sh is None:
            self.newpage(first=True)
        lines = self.sh.wrap(s, key, size, maxw)
        if keep and len(lines) <= 6:
            self.need(len(lines) * lead)          # short blocks are never split across a page break
        for ln in lines:
            self.need(lead)
            self.sh.text(L + indent, self.y + size, ln, key, size, color)
            self.y += lead

    def reserve(self, s, key, size, maxw, extra=0.0, lead=None):
        """Make room for a whole short block before anything is drawn for it."""
        if self.sh is None:
            self.newpage(first=True)
        lead = lead or size * 1.46
        n = len(self.sh.wrap(s, key, size, maxw))
        self.need(min(n, 6) * lead + extra)

    def block(self, kind, payload):
        if kind == "h":
            self.need(34 + 56)          # keep-with-next: a heading never ends a page alone
            self.y += 10
            self.need(24)
            kicker(self.sh, L, self.y + 11, payload.upper(), EMERALD, 1.8, key="sans_b")
            self.y += 17
            self.sh.line(L, self.y, R, self.y, GOLD, 0.9)
            self.y += 9
        elif kind == "sub":
            self.need(28)
            self.y += 7
            self.para(payload, "sans_sb", 11.5, color=EMERALD)
            self.y += 2
        elif kind == "p":
            self.para(payload)
            self.y += 5
        elif kind == "note":
            self.reserve(payload, "sans_i", 11, W - 22, extra=10)
            self.y += 4
            y0 = self.y
            self.para(payload, "sans_i", 11, indent=14, maxw=W - 22)
            self.sh.line(L + 3, y0 + 2, L + 3, self.y - 3, GOLD, 2.0)
            self.y += 6
        elif kind == "cue":
            self.reserve(payload, "serif", 11.5, W - 26, extra=12)
            self.y += 5
            y0 = self.y
            self.para(payload, "serif", 11.5, indent=16, maxw=W - 26)
            self.sh.rect(L, y0, L + 5, self.y - 4, fill=EMERALD)
            self.y += 7
        elif kind == "li":
            self.reserve(payload, "serif", 12, W - 16)   # the bullet never strands on the page before
            self.sh.circle(L + 4, self.y + 7, 2.1, fill=GOLD)
            self.para(payload, "serif", 12, indent=16, maxw=W - 16)
            self.y += 4
        elif kind == "list":
            for it in payload:
                self.para(it, "serif", 12, indent=14, maxw=W - 14)
                self.y += 4
        elif kind == "hand":
            self.para(payload, "hand", 13.5, lead=18.5)
            self.y += 6
        elif kind == "pin":
            self.reserve(payload, "type", 11, W - 32, extra=20)
            self.y += 4
            y0 = self.y
            self.para(payload, "type", 11, indent=16, maxw=W - 32)
            self.sh.rect(L + 4, y0 - 4, R - 4, self.y + 2, stroke=HAIR, width=0.8)
            self.y += 12
        elif kind == "rule":
            self.need(18)
            self.y += 6
            self.sh.line(L + 120, self.y, R - 120, self.y, GOLD, 0.8)
            self.y += 10
        elif kind == "kv":
            for k, v in payload:
                self.need(22)
                self.sh.text(L, self.y + 12, k.upper(), "sans_sb", MINPT, GREY)
                self.sh.text(L + 148, self.y + 12, v, "type", 11.5, INK)
                self.y += 20
            self.y += 4
        elif kind == "table":
            self.table(payload)
        else:
            raise ValueError(kind)

    def table(self, rows):
        cols = [106, 164, 74, 139]       # sums to 483
        heads = ["Whose", "What they had on", "Length", "The sole"]
        sz, lead = MINPT, 15.2

        def head_row():
            x = L
            self.sh.line(L, self.y, R, self.y, RULE, 1.0)
            for c, h in zip(cols, heads):
                self.sh.text(x + 4, self.y + 14, h.upper(), "sans_sb", sz, EMERALD)
                x += c
            self.y += 20
            self.sh.line(L, self.y, R, self.y, HAIR, 0.6)
            self.y += 4

        self.need(36 + 40)               # a column head never sits alone at the foot of a page
        self.y += 4
        head_row()
        for row in rows:
            cells = [self.sh.wrap(t, "sans" if i else "sans_sb", sz, cols[i] - 10)
                     for i, t in enumerate(row)]
            h = max(len(c) for c in cells) * lead + 8
            was = self.page_no
            self.need(h + 4)
            if self.page_no != was:      # the table carries its own heads onto the next page
                head_row()
            x, y0 = L, self.y
            for i, lines in enumerate(cells):
                for j, ln in enumerate(lines):
                    self.sh.text(x + 4, y0 + 12 + j * lead, ln, "sans" if i else "sans_sb", sz, INK)
                x += cols[i]
            self.y = y0 + h
            self.sh.line(L, self.y, R, self.y, HAIR, 0.5)
        self.y += 8

    def run(self, blocks):
        for b in blocks:
            self.block(b[0], b[1] if len(b) > 1 else None)

    def close(self, note=None):
        if self.sh:
            footer(self.sh, note)


# --------------------------------------------------------------------- page types
def band(sh, kick, title, sub=None, y=TOP):
    h = 86 if sub else 68
    sh.rect(L, y, R, y + h, fill=EMERALD)
    sh.rect(L + 5, y + 5, R - 5, y + h - 5, stroke=GOLD_LIGHT, width=0.6)
    cx = CANVAS_W / 2
    kicker(sh, cx, y + 25, kick.upper(), GOLD_LIGHT, 2.6, "c", maxw=W - 40)
    ts = 30.0
    while ts > 15 and tw(title, "gara_b", ts) > W - 60:
        ts -= 0.5
    sh.text(cx, y + (52 if sub else 54), title, "gara_b", ts, CREAM, "c")
    if sub:
        sh.text(cx, y + 74, sub, "sans", 11.5, CREAM, "c")
    return y + h + 22


def doc_head(sh, num, head, title, meta, y=TOP):
    """Letterhead block for one case document."""
    sh.rect(L, y, R, y + 3, fill=EMERALD)
    y += 14
    sh.text(R, y + 22, num, "gara_b", 24, GOLD, "r")
    kicker(sh, L, y + 11, head, EMERALD, 2.0, maxw=W - 70)
    sh.text(L, y + 34, title, "gara_b", 19, INK)
    y += 44
    sh.line(L, y, R, y, HAIR, 0.6)
    y += 6
    for ln in sh.wrap(meta, "sans_i", MINPT, W - 70):
        sh.text(L, y + 12, ln, "sans_i", MINPT, GREY)
        y += 15
    y += 6
    sh.line(L, y, R, y, RULE, 1.2)
    return y + 12


def round_tag(sh, n, y):
    labels = {1: "ROUND ONE \u00b7 THE SCENE", 2: "ROUND TWO \u00b7 THE PAPERS", 3: "ROUND THREE \u00b7 THE MEASUREMENTS"}
    t = labels[n]
    w = sum(tw(c, "sans_sb", MINPT) for c in t) + 1.2 * (len(t) - 1) + 16
    sh.rect(R - w, y, R, y + 18, fill=_c(238, 236, 228))
    sh.tracked(R - w + 8, y + 12.5, t, "sans_sb", MINPT, EMERALD, 1.2)


CARD_H = 315.0
CARD_GAP = 28.0


def card_page(book, pair):
    sh = book.page()
    foot_lines = sh.wrap(T.CARD_FOOT, "sans_i", MINPT, W - 28)
    foot_h = len(foot_lines) * 15.0 + 20
    body_h = CARD_H - 44 - foot_h - 6      # 44 = header band + the gap above the first line
    for i, (sid, name, meta, paras) in enumerate(pair):
        top = TOP + i * (CARD_H + CARD_GAP)
        # auto-fit: never let a card's body reach its own footer rule
        for size in (12.0, 11.5, MINPT):
            lead, gap = size * 1.43, 6.0
            need = sum(len(sh.wrap(p, "serif", size, W - 28)) for p in paras) * lead + gap * (len(paras) - 1)
            if need <= body_h:
                break
        else:
            raise SystemExit(f"card {sid} does not fit: needs {need:.0f} pt of {body_h:.0f}")
        sh.rect(L, top, R, top + CARD_H, stroke=RULE, width=1.0)
        sh.rect(L, top, R, top + 34, fill=EMERALD)
        sh.text(L + 12, top + 23, sid, "gara_b", 17, GOLD)
        sh.text(L + 46, top + 23, name, "gara_b", 17, CREAM)
        sh.text(R - 12, top + 23, meta, "sans", MINPT, CREAM, "r")
        y = top + 44
        for p in paras:
            for ln in sh.wrap(p, "serif", size, W - 28):
                sh.text(L + 14, y + size, ln, "serif", size, INK)
                y += lead
            y += gap
        fy = top + CARD_H - foot_h
        sh.line(L + 14, fy, R - 14, fy, HAIR, 0.6)
        for j, ln in enumerate(foot_lines):
            sh.text(L + 14, fy + 15 + j * 15.0, ln, "sans_i", MINPT, INK_SOFT)
        if i == 0:
            yy = top + CARD_H + CARD_GAP / 2
            sh.line(L - 14, yy, R + 14, yy, HAIR, 0.6, dashes="[3 3] 0")
            sh.text(CANVAS_W / 2, yy - 7, "cut here", "sans", MINPT, GREY, "c")
    return sh


def board_page(book):
    sh = book.page()
    y = band(sh, "keep this one in the middle of the table", "What We Know",
             "Fill it in together. Everybody writes on it.")
    rows = [sh.wrap(row, "sans_sb", 11.5, W) for row in T.BOARD_ROWS]
    head_h = sum(len(r) for r in rows) * 16.0 + len(rows) * 6.0
    slack = (BOT - 12 - y - head_h) / (len(rows) * 2)     # the writing lines share whatever is left
    assert slack >= 16.0, f"board page: only {slack:.1f} pt per writing line"
    for lines in rows:
        for ln in lines:
            sh.text(L, y + 12, ln, "sans_sb", 11.5, EMERALD)
            y += 16.0
        y += 6.0
        for _ in range(2):
            y += slack
            sh.line(L, y - 5, R, y - 5, HAIR, 0.6)
    footer(sh)
    return sh


def ballot_page(book):
    sh = book.page()
    y = band(sh, "cut into four \u00b7 one each", "The Accusation Slip",
             "Fill it in before anybody opens the answer. You may name yourself.")
    slot_h = (BOT - y - 10) / 4.0
    for i in range(4):
        top = y + i * slot_h
        sh.rect(L, top, R, top + slot_h - 12, stroke=HAIR, width=0.8)
        sh.text(L + 12, top + 20, "THE JUNIPER INN \u00b7 4 NOVEMBER", "sans_sb", MINPT, EMERALD)
        box_bottom = top + slot_h - 12
        yy = top + 27
        step = (box_bottom - 8 - yy) / len(T.BALLOT_LINES)
        assert step >= 17, f"accusation slip: only {step:.1f} pt a line"
        for lab in T.BALLOT_LINES:
            sh.text(L + 12, yy + 12, lab, "sans", MINPT, GREY)
            sh.line(L + 12 + tw(lab, "sans", MINPT) + 8, yy + 14, R - 14, yy + 14, HAIR, 0.6)
            yy += step
        if i < 3:
            sh.line(L - 14, top + slot_h - 6, R + 14, top + slot_h - 6, HAIR, 0.6, dashes="[3 3] 0")
    footer(sh)
    return sh


# --------------------------------------------------------------------- build
def build_game(out: Path, site: str):
    book = Book(MYST)

    # 1 cover
    sh = book.page()
    y = band(sh, "a free mini mystery from a maison soir\u00e9e", T.TITLE, T.SUB)
    f = Flow(book)
    f.sh, f.y = sh, y
    f.run(T.COVER)
    f.sh.text(CANVAS_W / 2, BOT - 6, site, "sans_sb", 11, EMERALD, "c")
    footer(f.sh)

    # 2 how to play
    sh = book.page()
    y = band(sh, "guest sheet \u00b7 read this one out loud", "How To Play")
    f = Flow(book, "How To Play"); f.sh, f.y = sh, y
    f.run(T.HOWTO); f.close()

    # 3 host page
    sh = book.page()
    y = band(sh, "host sheet \u00b7 contains no spoilers", "For Whoever Is Printing",
             "You can read every word of this and still play.")
    f = Flow(book, "For Whoever Is Printing"); f.sh, f.y = sh, y
    f.run(T.HOST); f.close()

    # 4-5 cards
    for pair in (T.CARDS[:2], T.CARDS[2:]):
        sh = card_page(book, pair)
        footer(sh, "cut along the dashed line")

    # documents
    for d in T.DOCS:
        sh = book.page()
        y = doc_head(sh, d["num"], d["head"], d["title"], d["meta"])
        round_tag(sh, d["round"], Y0 + 2)
        f = Flow(book, f"{d['num']} \u00b7 {d['title']}")
        f.sh, f.y = sh, y
        f.run(d["blocks"])
        f.close()

    ballot_page(book)
    board_page(book)

    n = book.doc.page_count
    book.save(out.with_name(out.stem + "-USLetter.pdf"), "USLetter", T.TITLE, T.SUB)
    book.save(out.with_name(out.stem + "-A4.pdf"), "A4", T.TITLE, T.SUB)
    return n


def build_answer(out: Path, site: str):
    book = Book(MYST)

    sh = book.page()
    sh.rect(L, TOP, R, BOT, stroke=EMERALD, width=3.0)
    sh.text(CANVAS_W / 2, 250, "STOP", "gara_b", 120, EMERALD, "c")
    y = 300
    for ln in sh.wrap(T.STOP, "serif", 15, W - 90):
        sh.text(CANVAS_W / 2, y, ln, "serif", 15, INK, "c")
        y += 24
    sh.line(L + 90, y + 14, R - 90, y + 14, GOLD, 0.9)
    sh.text(CANVAS_W / 2, y + 48, "The Wet Half-Hour", "gara_b", 22, EMERALD, "c")
    sh.text(CANVAS_W / 2, y + 70, "The Answer", "sans", 13, INK_SOFT, "c")
    sh.text(CANVAS_W / 2, BOT - 20, site, "sans_sb", 11, EMERALD, "c")

    sh = book.page()
    y = band(sh, "read this out loud when the ballots are folded", "Who Did It")
    f = Flow(book, "Who Did It"); f.sh, f.y = sh, y
    f.run(T.REVEAL); f.close()

    sh = book.page()
    y = band(sh, "the fair-play audit", "How It Was Proved",
             "Every fact below is printed on a document the table had.")
    f = Flow(book, "How It Was Proved"); f.sh, f.y = sh, y
    f.run(T.PROOF)
    f.block("h", "And when you want a longer one")
    f.block("p", "This is a small game, built the way the big ones are built. The Christmas one runs ninety "
                 "minutes to two hours for six to twelve people around a dinner table, with twenty-two case "
                 "documents instead of eleven. The office one runs a room of sixteen to forty. Both are at "
                 f"{site}.")
    f.close()

    n = book.doc.page_count
    book.save(out.with_name(out.stem + "-USLetter.pdf"), "USLetter", T.TITLE + " \u2014 The Answer", "Sealed reveal")
    book.save(out.with_name(out.stem + "-A4.pdf"), "A4", T.TITLE + " \u2014 The Answer", "Sealed reveal")
    book.save(out, "USLetter", T.TITLE + " \u2014 The Answer", "Sealed reveal")
    return n


def assert_glyphs():
    """Every character in the game text must exist in every face that could print it."""
    chars = set()
    for name in dir(T):
        v = getattr(T, name)
        stack = [v]
        while stack:
            x = stack.pop()
            if isinstance(x, str):
                chars |= set(x)
            elif isinstance(x, (list, tuple, dict)):
                stack += list(x.values()) if isinstance(x, dict) else list(x)
    bad = []
    for key in ("serif", "sans", "sans_sb", "sans_i", "sans_b", "gara_b", "gara_i", "type", "hand"):
        f = AP.F(key)
        miss = sorted(c for c in chars if ord(c) > 126 and not f.has_glyph(ord(c)))
        if miss:
            bad.append((key, [hex(ord(c)) for c in miss]))
    if bad:
        raise SystemExit(f"missing glyphs (they print as empty boxes): {bad}")


if __name__ == "__main__":
    assert_glyphs()
    site = sys.argv[1] if len(sys.argv) > 1 else SITE
    out = Path(__file__).resolve().parent.parent / "docs" / "files"
    out.mkdir(parents=True, exist_ok=True)
    a = build_game(out / "the-wet-half-hour.pdf", site)
    b = build_answer(out / "the-wet-half-hour-answer.pdf", site)
    print(f"game {a} pages, answer {b} pages")
