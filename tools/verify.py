# -*- coding: utf-8 -*-
"""Checks the built site. `python verify.py` for the local files,
`python verify.py https://host/path` to check what is actually published."""
import json
import re
import sys
import urllib.request
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "docs"
fails, warns = [], []


def fail(p, m):
    fails.append(f"{p}: {m}")


def check_html(name, text):
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if len(h1) != 1:
        fail(name, f"{len(h1)} <h1> tags")
    for pat, what in [(r"<title>(.{10,70})</title>", "title"),
                      (r'<meta name="description" content="(.{60,175})"', "description"),
                      (r'<link rel="canonical" href="https://', "canonical"),
                      (r'<meta property="og:title"', "og:title"),
                      (r'<meta property="og:description"', "og:description"),
                      (r'<meta property="og:url"', "og:url"),
                      (r'<meta property="og:image"', "og:image"),
                      (r'<meta name="viewport"', "viewport")]:
        if not re.search(pat, text, re.S):
            fail(name, f"missing or out-of-range {what}")
    ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)
    if not ld:
        fail(name, "no JSON-LD")
    for block in ld:
        try:
            json.loads(block)
        except Exception as e:
            fail(name, f"bad JSON-LD: {e}")
    body = re.sub(r"<[^>]+>", " ", text.split("<main>")[-1].split("<footer")[0])
    words = len(body.split())
    return words, set(re.findall(r'href="([^"#]+)"', text))


def local():
    pages = sorted(p.name for p in SITE.glob("*.html"))
    sm = (SITE / "sitemap.xml").read_text(encoding="utf-8")
    listed = set(re.findall(r"<loc>[^<]*/([^/<]+)</loc>", sm))
    if listed != set(pages):
        fail("sitemap.xml", f"missing {set(pages) - listed} / extra {listed - set(pages)}")
    print(f"sitemap lists {len(listed)} URLs, {len(pages)} html files present")
    for name in pages:
        text = (SITE / name).read_text(encoding="utf-8")
        words, hrefs = check_html(name, text)
        if name not in ("index.html", "guides.html") and not 900 <= words <= 1700:
            warns.append(f"{name}: {words} words")
        for h in hrefs:
            if h.startswith(("http://", "https://", "mailto:")):
                continue
            if not (SITE / h).exists():
                fail(name, f"broken internal link -> {h}")
        print(f"  {name:52s} {words:5d} words  {len(hrefs):2d} links")


def live(base):
    base = base.rstrip("/")
    sm = urllib.request.urlopen(base + "/sitemap.xml", timeout=30).read().decode()
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
    print(f"sitemap.xml: 200, {len(urls)} URLs")
    for u in urls:
        try:
            r = urllib.request.urlopen(u, timeout=30)
            text = r.read().decode("utf-8", "replace")
        except Exception as e:
            fail(u, f"fetch failed: {e}")
            continue
        code = r.getcode()
        words, hrefs = check_html(u.rsplit("/", 1)[-1], text)
        print(f"  {code} {words:5d}w  {u}")
        for h in hrefs:
            if h.startswith(("http://", "https://", "mailto:")):
                continue
            tgt = base + "/" + h
            try:
                req = urllib.request.Request(tgt, method="HEAD")
                c = urllib.request.urlopen(req, timeout=30).getcode()
            except Exception as e:
                fail(u, f"internal link {h} -> {e}")
                continue
            if c != 200:
                fail(u, f"internal link {h} -> HTTP {c}")
    for extra in ("/robots.txt", "/og.png",
                  "/files/the-wet-half-hour-USLetter.pdf",
                  "/files/the-wet-half-hour-A4.pdf",
                  "/files/the-wet-half-hour-answer-USLetter.pdf",
                  "/files/the-wet-half-hour-answer-A4.pdf"):
        try:
            r = urllib.request.urlopen(base + extra, timeout=60)
            data = r.read()
            print(f"  {r.getcode()} {len(data):8d} bytes  {extra}")
            if extra.endswith(".pdf") and not data.startswith(b"%PDF"):
                fail(extra, "not a PDF")
        except Exception as e:
            fail(extra, str(e))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        live(sys.argv[1])
    else:
        local()
    for w in warns:
        print("WARN  " + w)
    for f in fails:
        print("FAIL  " + f)
    print(("ALL CHECKS PASSED" if not fails else f"{len(fails)} FAILURES"))
    sys.exit(1 if fails else 0)
