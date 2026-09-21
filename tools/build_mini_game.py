# -*- coding: utf-8 -*-
"""Builds the two PDFs of the free mini mystery, on the shop's own print engine.

  the-wet-half-hour.pdf         the whole game, and no answer anywhere in it
  the-wet-half-hour-answer.pdf  the sealed reveal, behind a full-page STOP

Same rules as the paid products: union canvas so US Letter and A4 come out of one
layout at 100%, live vector text in embedded fonts, nothing below 10 pt, pure black
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
def footer(sh, note=None):
    y = Y1 - 26
    sh.line(L, y, R, y, HAIR, 0.6)
    sh.text(L, y + 14, FOOT, "gara_i", 10, GREY)
    if note:
        sh.text(R, y + 14, note, "sans", 10, GREY, "r")


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
            self.sh.text(L, self.y + 10, f"{self.cont} (continued)", "sans_i", 10, GREY)
            self.y += 26
        return self.sh

    def need(self, h):
        if self.sh is None:
            self.newpage(first=True)
        if self.y + h > BOT:
            footer(self.sh)
            self.newpage()

    # ---- primitives -------------------------------------------------
    def para(self, s, key="serif", size=12, lead=None, color=INK, indent=0, maxw=None):
        lead = lead or size * 1.46
        maxw = maxw or (W - indent)
        lines = self.sh.wrap(s, key, size, maxw) if self.sh else None
        if lines is None:
            self.need(lead)
            lines = self.sh.wrap(s, key, size, maxw)
        for ln in lines:
            self.need(lead)
            self.sh.text(L + indent, self.y + size, ln, key, size, color)
            self.y += lead

    def block(self, kind, payload):
        if kind == "h":
            self.need(34)
            self.y += 10
            self.need(24)
            self.sh.tracked(L, self.y + 11, payload.upper(), "sans_b", 10.5, EMERALD, 1.8)
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
            self.need(30)
            self.y += 4
            y0 = self.y
            self.para(payload, "sans_i", 11, indent=14, maxw=W - 22)
            self.sh.line(L + 3, y0 + 2, L + 3, self.y - 3, GOLD, 2.0)
            self.y += 6
        elif kind == "cue":
            self.need(34)
            self.y += 5
            y0 = self.y
            self.para(payload, "serif", 11.5, indent=16, maxw=W - 26)
            self.sh.rect(L, y0, L + 5, self.y - 4, fill=EMERALD)
            self.y += 7
        elif kind == "li":
            self.need(24)
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
            self.need(44)
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
                self.need(20)
                self.sh.text(L, self.y + 11, k.upper(), "sans_sb", 10, GREY)
                self.sh.text(L + 130, self.y + 11, v, "type", 11.5, INK)
                self.y += 18
            self.y += 4
        elif kind == "table":
            self.table(payload)
        else:
            raise ValueError(kind)

    def table(self, rows):
        cols = [128, 168, 78, 109]       # sums to 483
        heads = ["Whose", "What they had on", "Length", "The sole"]
        self.need(34)
        self.y += 4
        x = L
        self.sh.line(L, self.y, R, self.y, RULE, 1.0)
        for c, h in zip(cols, heads):
            self.sh.text(x + 4, self.y + 13, h.upper(), "sans_sb", 9.5, EMERALD)
            x += c
        self.y += 18
        self.sh.line(L, self.y, R, self.y, HAIR, 0.6)
        self.y += 4
        for row in rows:
            cells = [self.sh.wrap(t, "sans" if i else "sans_sb", 10.0, cols[i] - 10)
                     for i, t in enumerate(row)]
            h = max(len(c) for c in cells) * 12.8 + 6
            self.need(h + 4)
            x, y0 = L, self.y
            for i, lines in enumerate(cells):
                for j, ln in enumerate(lines):
                    self.sh.text(x + 4, y0 + 11 + j * 12.8, ln, "sans" if i else "sans_sb", 10.0, INK)
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
def band(sh, kicker, title, sub=None, y=TOP):
    h = 86 if sub else 68
    sh.rect(L, y, R, y + h, fill=EMERALD)
    sh.rect(L + 5, y + 5, R - 5, y + h - 5, stroke=GOLD_LIGHT, width=0.6)
    cx = CANVAS_W / 2
    sh.tracked(cx, y + 24, kicker.upper(), "sans_sb", 9.5, GOLD_LIGHT, 2.6, "c")
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
    sh.tracked(L, y + 10, head, "sans_sb", 9.5, EMERALD, 2.0)
    sh.text(L, y + 34, title, "gara_b", 19, INK)
    y += 44
    sh.line(L, y, R, y, HAIR, 0.6)
    y += 6
    for ln in sh.wrap(meta, "sans_i", 10.5, W - 70):
        sh.text(L, y + 11, ln, "sans_i", 10.5, GREY)
        y += 14
    y += 6
    sh.line(L, y, R, y, RULE, 1.2)
    return y + 12


def round_tag(sh, n, y):
    labels = {1: "ROUND ONE \u00b7 THE SCENE", 2: "ROUND TWO \u00b7 THE PAPERS", 3: "ROUND THREE \u00b7 THE MEASUREMENTS"}
    t = labels[n]
    w = sum(tw(c, "sans_sb", 8.5) for c in t) + 1.8 * (len(t) - 1) + 16
    sh.rect(R - w, y, R, y + 15, fill=_c(238, 236, 228))
    sh.tracked(R - w + 8, y + 10.5, t, "sans_sb", 8.5, EMERALD, 1.8)


CARD_H = 315.0
CARD_GAP = 28.0


def card_page(book, pair):
    sh = book.page()
    foot_lines = sh.wrap(T.CARD_FOOT, "sans_i", 9.6, W - 28)
    foot_h = len(foot_lines) * 12.0 + 20
    body_h = CARD_H - 34 - foot_h
    for i, (sid, name, meta, paras) in enumerate(pair):
        top = TOP + i * (CARD_H + CARD_GAP)
        # auto-fit: never let a card's body reach its own footer rule
        for size in (12.0, 11.5, 11.0, 10.5):
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
        sh.text(R - 12, top + 23, meta, "sans", 10.5, CREAM, "r")
        y = top + 44
        for p in paras:
            for ln in sh.wrap(p, "serif", size, W - 28):
                sh.text(L + 14, y + size, ln, "serif", size, INK)
                y += lead
            y += gap
        fy = top + CARD_H - foot_h
        sh.line(L + 14, fy, R - 14, fy, HAIR, 0.6)
        for j, ln in enumerate(foot_lines):
            sh.text(L + 14, fy + 14 + j * 12.0, ln, "sans_i", 9.6, INK_SOFT)
        if i == 0:
            yy = top + CARD_H + CARD_GAP / 2
            sh.line(L - 14, yy, R + 14, yy, HAIR, 0.6, dashes="[3 3] 0")
            sh.text(CANVAS_W / 2, yy - 4, "cut here", "sans", 8.5, GREY, "c")
    return sh


def board_page(book):
    sh = book.page()
    y = band(sh, "keep this one in the middle of the table", "What We Know",
             "Fill it in together. Everybody writes on it.")
    for row in T.BOARD_ROWS:
        for ln in sh.wrap(row, "sans_sb", 11.5, W):
            sh.text(L, y + 12, ln, "sans_sb", 11.5, EMERALD)
            y += 16
        y += 6
        for _ in range(2):
            sh.line(L, y + 12, R, y + 12, HAIR, 0.6)
            y += 22
        y += 10
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
        sh.text(L + 12, top + 20, "THE JUNIPER INN \u00b7 4 NOVEMBER", "sans_sb", 9, EMERALD)
        yy = top + 34
        for lab in T.BALLOT_LINES:
            sh.text(L + 12, yy + 11, lab, "sans", 10.5, GREY)
            sh.line(L + 12 + tw(lab, "sans", 10.5) + 8, yy + 13, R - 14, yy + 13, HAIR, 0.6)
            yy += 19
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


if __name__ == "__main__":
    site = sys.argv[1] if len(sys.argv) > 1 else SITE
    out = Path(__file__).resolve().parent.parent / "docs" / "files"
    out.mkdir(parents=True, exist_ok=True)
    a = build_game(out / "the-wet-half-hour.pdf", site)
    b = build_answer(out / "the-wet-half-hour-answer.pdf", site)
    print(f"game {a} pages, answer {b} pages")
