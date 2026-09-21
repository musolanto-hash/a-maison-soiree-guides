# -*- coding: utf-8 -*-
"""Tells search engines the site exists.

  1. Google's sitemap ping endpoint (no account needed).
  2. Bing's sitemap ping endpoint (no account needed).
  3. IndexNow, which Bing, Yandex, Seznam and Naver share. Needs a key file hosted
     on the site; because this is a GitHub project page the key cannot sit at the host
     root, so we pass keyLocation, which the spec allows as long as the key file is in
     a parent directory of every URL submitted.

Prints the HTTP status of everything. Run after the site is live.
"""
import json
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import quote

BASE = "https://musolanto-hash.github.io/a-maison-soiree-guides"
KEY = "addbc343c604f1cea3800c50d6895b69"
UA = "Mozilla/5.0 (compatible; AMaisonSoireeBot/1.0)"


def get(url, method="GET", data=None, ctype=None):
    req = urllib.request.Request(url, data=data, method=method, headers={"User-Agent": UA})
    if ctype:
        req.add_header("Content-Type", ctype)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.getcode(), r.read()[:400].decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:400].decode("utf-8", "replace")
    except Exception as e:
        return None, repr(e)


def main():
    sm = f"{BASE}/sitemap.xml"
    code, body = get(sm)
    print(f"[sitemap] {sm} -> HTTP {code}")
    if code != 200:
        sys.exit("sitemap is not live yet")
    full = urllib.request.urlopen(
        urllib.request.Request(sm, headers={"User-Agent": UA}), timeout=60).read().decode()
    urls = re.findall(r"<loc>([^<]+)</loc>", full)
    print(f"[sitemap] {len(urls)} URLs")

    kc, kb = get(f"{BASE}/{KEY}.txt")
    print(f"[indexnow key] {BASE}/{KEY}.txt -> HTTP {kc} body={kb.strip()[:40]!r}")

    for name, ping in [("google", f"https://www.google.com/ping?sitemap={quote(sm, safe='')}"),
                       ("bing", f"https://www.bing.com/ping?sitemap={quote(sm, safe='')}")]:
        c, b = get(ping)
        print(f"[ping {name}] HTTP {c} :: {' '.join(b.split())[:160]}")

    payload = json.dumps({
        "host": "musolanto-hash.github.io",
        "key": KEY,
        "keyLocation": f"{BASE}/{KEY}.txt",
        "urlList": urls,
    }).encode()
    for ep in ("https://api.indexnow.org/IndexNow",
               "https://www.bing.com/indexnow"):
        c, b = get(ep, method="POST", data=payload, ctype="application/json; charset=utf-8")
        print(f"[indexnow {ep}] HTTP {c} :: {' '.join(b.split())[:200]}")


if __name__ == "__main__":
    main()
