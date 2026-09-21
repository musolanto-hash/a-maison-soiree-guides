# -*- coding: utf-8 -*-
"""Generates the static site: one HTML file per page, sitemap.xml, robots.txt.

No frameworks, no build chain, no external fonts, no JavaScript. One inline
stylesheet, semantic HTML, one <h1> per page, JSON-LD on every page.
"""
from __future__ import annotations

import html
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
sys.path.insert(0, str(Path(__file__).resolve().parent))

BASE = "https://musolanto-hash.github.io/a-maison-soiree-guides"
SITE_NAME = "A Maison Soirée Guides"
TODAY = date.today().isoformat()

CSS = """
:root{--ink:#16181a;--soft:#4d5358;--line:#dcd8cf;--em:#0a2820;--gold:#8a6a22;--bg:#fbfaf7;--card:#fff}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
 font:17px/1.65 Georgia,"Iowan Old Style","Times New Roman",serif;word-wrap:break-word}
.wrap{max-width:43rem;margin:0 auto;padding:0 1.15rem}
header.site{background:var(--em);color:#f4e9d7}
header.site .wrap{display:flex;flex-wrap:wrap;gap:.35rem 1rem;align-items:baseline;
 padding-top:.95rem;padding-bottom:.95rem}
header.site a{color:#f4e9d7;text-decoration:none}
header.site .brand{font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.83rem}
header.site nav{font:400 .83rem/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
 margin-left:auto;display:flex;gap:1rem;flex-wrap:wrap}
header.site nav a{border-bottom:1px solid rgba(244,233,215,.35);padding-bottom:1px}
main{padding:1.6rem 0 2.5rem}
h1{font-size:1.95rem;line-height:1.18;margin:.2rem 0 .5rem;letter-spacing:-.01em}
h2{font-size:1.28rem;line-height:1.3;margin:2.3rem 0 .6rem;letter-spacing:-.005em}
h3{font-size:1.05rem;margin:1.6rem 0 .4rem;
 font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
p,li{font-size:1.02rem}
ul,ol{padding-left:1.15rem}
li{margin:.4rem 0}
a{color:#0d3b2e}
.lede{font-size:1.12rem;color:var(--soft)}
.meta{font:400 .8rem/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--soft);
 margin:0 0 1.3rem;padding-bottom:1rem;border-bottom:1px solid var(--line)}
blockquote{margin:1.3rem 0;padding:.1rem 0 .1rem 1rem;border-left:3px solid var(--gold);color:var(--soft)}
table{border-collapse:collapse;width:100%;
 font:400 .92rem/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.scroll{overflow-x:auto;margin:1.2rem 0}
th,td{border-bottom:1px solid var(--line);padding:.5rem .55rem;text-align:left;vertical-align:top}
th{color:var(--em);font-size:.78rem;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap}
.box{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:1rem 1.1rem;margin:1.6rem 0}
.box p:first-child{margin-top:0}.box p:last-child{margin-bottom:0}
.shop{background:#f4f1e8;border-left:4px solid var(--gold)}
.shop .k{font:700 .72rem/1.4 system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;
 color:var(--gold);display:block;margin-bottom:.3rem}
.cta{display:inline-block;background:var(--em);color:#f4e9d7;text-decoration:none;
 padding:.62rem 1.1rem;border-radius:3px;font:600 .95rem/1.3 system-ui,sans-serif;margin:.3rem .3rem .3rem 0}
.cta.alt{background:transparent;color:var(--em);border:1px solid var(--em)}
.cards{list-style:none;padding:0;margin:1.2rem 0}
.cards li{border-top:1px solid var(--line);padding:.9rem 0;margin:0}
.cards a{font-weight:700;text-decoration:none;font-size:1.06rem}
.cards a:hover{text-decoration:underline}
.cards p{margin:.25rem 0 0;color:var(--soft);font-size:.95rem}
.next{margin-top:2.6rem;border-top:1px solid var(--line);padding-top:.6rem}
.next h2{font-size:1rem;letter-spacing:.06em;text-transform:uppercase;
 font-family:system-ui,sans-serif;margin:.8rem 0 .2rem}
footer.site{border-top:1px solid var(--line);background:#f4f1e8;
 font:400 .85rem/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--soft)}
footer.site .wrap{padding-top:1.4rem;padding-bottom:2rem}
footer.site a{color:#0d3b2e}
@media (max-width:480px){h1{font-size:1.62rem}body{font-size:16px}}
"""
CSS = re.sub(r"\n\s*", "\n", CSS).strip()

NAV = [("index.html", "Home"),
       ("free-murder-mystery-game.html", "Free mini mystery"),
       ("guides.html", "All guides")]


def head(p):
    url = f"{BASE}/{p['slug']}"
    desc = html.escape(p["desc"], quote=True)
    title = html.escape(p["meta_title"], quote=True)
    ld = p["ld"]
    nav = "".join(f'<a href="{s}">{html.escape(t)}</a>' for s, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%274%27 fill=%27%230a2820%27/%3E%3Ctext x=%2716%27 y=%2722%27 font-family=%27Georgia,serif%27 font-size=%2716%27 font-weight=%27bold%27 fill=%27%23c9a961%27 text-anchor=%27middle%27%3EA%3C/text%3E%3C/svg%3E">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{p.get('og_type', 'article')}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:image" content="{BASE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/og.png">
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="site"><div class="wrap"><a class="brand" href="{BASE}/">A Maison Soirée &middot; Guides</a>
<nav>{nav}</nav></div></header>
<main><div class="wrap">
"""


FOOTER = f"""</div></main>
<footer class="site"><div class="wrap">
<p><strong>{SITE_NAME}</strong> &mdash; notes from building printable party games. Written by the people who
draw the pages, run the print tests and read the competitor reviews.</p>
<p>Everything here is free to read. Some pages link to our own printable games on Etsy, and those links are
marked. There is no shop, no basket and no checkout on this site.</p>
<p><a href="{BASE}/">Home</a> &middot; <a href="{BASE}/guides.html">All guides</a> &middot;
<a href="{BASE}/free-murder-mystery-game.html">Free four-player mystery</a> &middot;
<a href="https://www.etsy.com/shop/AMaisonSoiree">Our Etsy shop</a></p>
</div></footer>
</body>
</html>
"""


def article_ld(p):
    import json
    d = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": p["h1"][:110],
        "description": p["desc"],
        "datePublished": p.get("published", TODAY),
        "dateModified": TODAY,
        "inLanguage": "en",
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{BASE}/{p['slug']}"},
        "author": {"@type": "Organization", "name": "A Maison Soirée"},
        "publisher": {"@type": "Organization", "name": "A Maison Soirée",
                      "url": f"{BASE}/"},
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": f"{BASE}/"},
    }
    if p.get("about"):
        d["about"] = [{"@type": "Thing", "name": a} for a in p["about"]]
    if p.get("faq"):
        return json.dumps([d, {
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]
        }], ensure_ascii=False)
    return json.dumps(d, ensure_ascii=False)


def site_ld():
    import json
    return json.dumps([
        {"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME,
         "url": f"{BASE}/", "inLanguage": "en",
         "publisher": {"@type": "Organization", "name": "A Maison Soirée"}},
        {"@context": "https://schema.org", "@type": "Organization",
         "name": "A Maison Soirée", "url": f"{BASE}/",
         "description": "A small studio that draws and prints party games — murder mysteries, "
                        "advent calendars and mahjong reference sheets.",
         "sameAs": ["https://www.etsy.com/shop/AMaisonSoiree"]},
    ], ensure_ascii=False)


def related_block(p, pages):
    by_slug = {q["slug"]: q for q in pages}
    rel = [by_slug[s] for s in p.get("related", []) if s in by_slug]
    if not rel:
        return ""
    items = "".join(
        f'<li><a href="{r["slug"]}">{html.escape(r["h1"])}</a><p>{html.escape(r["desc"])}</p></li>'
        for r in rel)
    return f'<section class="next"><h2>Read next</h2><ul class="cards">{items}</ul></section>'


def build(pages):
    OUT.mkdir(parents=True, exist_ok=True)
    for p in pages:
        p["ld"] = site_ld() if p["slug"] == "index.html" else article_ld(p)
        body = p["body"]
        if p["slug"] not in ("index.html", "guides.html"):
            body += related_block(p, pages)
        (OUT / p["slug"]).write_text(head(p) + body + FOOTER, encoding="utf-8")

    urls = []
    for p in pages:
        pri = "1.0" if p["slug"] == "index.html" else ("0.9" if p.get("hub") else "0.8")
        urls.append(f"  <url>\n    <loc>{BASE}/{p['slug']}</loc>\n"
                    f"    <lastmod>{TODAY}</lastmod>\n"
                    f"    <changefreq>monthly</changefreq>\n    <priority>{pri}</priority>\n  </url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    return len(pages)


if __name__ == "__main__":
    import content
    n = build(content.PAGES)
    print(f"{n} pages written to {OUT}")
