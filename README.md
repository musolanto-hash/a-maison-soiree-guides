# A Maison Soirée — Guides

A small static content site: ten long guides about hosting murder mystery parties, adult advent
calendars and American mahjong nights, plus a complete free four-player murder mystery as a PDF.

**Live:** <https://musolanto-hash.github.io/a-maison-soiree-guides/>

## What this is, and what it is not

This is a **content site**. It publishes free articles and a free printable game, and where it is
relevant it links out to our own products on Etsy, clearly marked. There is **no shop, no basket,
no checkout and no payment of any kind on this site**, and nothing here is transacted.

That distinction matters because **GitHub Pages' terms discourage running a business on it** — Pages
is not intended to be used as a commercial hosting or e-commerce platform. A site that links out to
a shop elsewhere is a grey area rather than a clear yes, so the rule we hold ourselves to is:

* Every page must be worth reading on its own, with or without the links.
* No checkout, no cart, no payment processing, no order fulfilment, no customer data collection.
* No email capture, no tracking scripts, no analytics, no cookies. There is no JavaScript at all.
* Product links are contextual, honest, and confined to one clearly-labelled block per page.

If GitHub ever reads it the other way, the site moves to ordinary web hosting and the URLs are
redirected. Nothing here depends on Pages specifically.

## Layout

```
docs/                     everything that is published (Pages serves this folder)
  index.html              homepage
  guides.html             index of the ten guides
  free-murder-mystery-game.html   the lead magnet landing page
  *.html                  the ten articles
  files/*.pdf             the free game: US Letter and A4, game and sealed answer
  og.png                  one 1200x630 social card, drawn with PyMuPDF
  sitemap.xml, robots.txt, <indexnow key>.txt
tools/                    the generator (not published)
  build_site.py           template, JSON-LD, sitemap, robots
  content.py              page registry: slug, metadata, target searches, internal links
  art_*.py                the article bodies
  build_mini_game.py      builds the free game PDFs on the shop's own print engine
  game_text.py            the whole game: cards, 11 case documents, the sealed reveal
  build_og.py             the social card
  verify.py               checks the build, locally or against the live site
  submit.py               sitemap ping + IndexNow submission
```

## Rebuilding

```bash
python tools/build_mini_game.py     # the PDFs
python tools/build_og.py            # the social card
python tools/build_site.py          # the HTML, sitemap and robots.txt
python tools/verify.py              # local checks
python tools/verify.py https://musolanto-hash.github.io/a-maison-soiree-guides  # live checks
```

`verify.py` fails on: more or fewer than one `<h1>`, a missing or out-of-range title or meta
description, missing canonical/Open Graph/viewport tags, invalid JSON-LD, a broken internal link, or
a sitemap that does not match the files on disk.

## Technical notes

* No frameworks, no JavaScript, no external fonts, no web requests of any kind from the page. One
  inline stylesheet, system font stack, semantic HTML.
* One `<h1>` per page, `Article` JSON-LD on every article, `FAQPage` JSON-LD where the page answers
  real questions, `WebSite` + `Organization` on the homepage.
* Mobile-first: 43rem measure, tables wrapped in horizontal scroll containers, nothing with a
  minimum width wider than a phone.
* A project page cannot serve the host root, so `robots.txt` and the IndexNow key also live in a
  second tiny repo, `musolanto-hash/musolanto-hash.github.io`, which publishes
  <https://musolanto-hash.github.io/robots.txt> pointing at this sitemap. A copy of both stays in
  `docs/` as well, and IndexNow is submitted with `keyLocation` so either copy satisfies it.

## Indexing, and what actually still works

Run `python tools/submit.py`. Results as of 21 September 2026:

| Endpoint | Result |
|---|---|
| `google.com/ping?sitemap=` | **HTTP 404** — Google retired sitemap ping in June 2023 and the endpoint now serves a deprecation notice |
| `bing.com/ping?sitemap=` | **HTTP 410 Gone** — also retired |
| `api.indexnow.org/IndexNow` | **HTTP 200**, all 13 URLs accepted |
| `bing.com/indexnow` | **HTTP 200**, all 13 URLs accepted |

So IndexNow (Bing, Yandex, Seznam, Naver) is the only push channel that still exists without an
account. **Google now has no account-free submission route at all**: discovery there depends on the
host-root `robots.txt` above, the sitemap it points to, and inbound links. If the shop owner ever
verifies the property in Google Search Console, the sitemap can be submitted there directly, which
is the only thing that would speed it up.

## The free game

`The Wet Half-Hour` is a complete four-player murder mystery written for this site: four suspect
cards, eleven printed case documents, a spoiler-free host sheet, accusation slips, and a sealed
answer in a separate file. It is built to the same five rules as the paid games — nothing memorised,
nothing read aloud in character, nobody lies, nobody knows they are the culprit, and the printed
documents carry the whole solution — and the build script refuses to put anything from the reveal
into the game file.

It is free for personal use. Please do not resell it or put it behind a paywall.
