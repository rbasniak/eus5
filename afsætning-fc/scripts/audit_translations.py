"""Audit bilingual HTML for untranslated DA/EN pairs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_all import looks_danish  # noqa: E402

HOSTS = {"p", "h1", "h2", "h3", "h4", "li", "td", "th", "figcaption", "a", "blockquote", "summary"}

# Same in both languages by design (brands, URLs, proper names, English citations)
ALLOW_SAME = re.compile(
    r"^(?:"
    r"[A-Z0-9][A-Za-z0-9&.\- ]{0,40}(?:\.com|\.dk|\.org|\.html)?"
    r"|(?:IKEA|Boozt|Airtox|JYSK|Zalando|Wikipedia|Airbnb|Amazon|Pandora|REMA 1000|Too Good To Go|JOE & THE JUICE|ed A/S|Søstrene Grene|Søstrene Grene plans to Open.*)"
    r")$",
    re.I,
)


def en_sibling(da_span):
    sib = da_span.find_next_sibling("span")
    return sib if sib is not None and sib.get("lang") == "en" else None


def audit_file(path: Path) -> list[dict]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    issues = []

    for host in soup.find_all(HOSTS):
        spans = host.find_all("span", attrs={"lang": True}, recursive=False)
        if len(spans) < 2:
            continue
        if spans[0].get("lang") != "da" or spans[1].get("lang") != "en":
            continue
        da_t = spans[0].get_text(" ", strip=True)
        en_t = spans[1].get_text(" ", strip=True)
        if not da_t or da_t != en_t:
            continue
        if len(da_t) <= 3:
            continue
        if ALLOW_SAME.match(da_t):
            continue
        if not looks_danish(da_t):
            continue
        issues.append({"file": path.name, "text": da_t})

    for da_span in soup.select("span[lang=da]"):
        en_span = en_sibling(da_span)
        if not en_span:
            continue
        da_t = da_span.get_text(" ", strip=True)
        en_t = en_span.get_text(" ", strip=True)
        if not da_t or da_t == en_t or len(da_t) <= 3:
            continue
        if ALLOW_SAME.match(da_t):
            continue
        if looks_danish(en_t) and len(en_t) > 12:
            ratio = len(set(en_t.lower().split()) & set(da_t.lower().split())) / max(
                len(set(da_t.lower().split())), 1
            )
            if ratio > 0.85:
                issues.append({"file": path.name, "text": da_t, "en": en_t[:120]})

    return issues


def main() -> None:
    all_issues: list[dict] = []
    for path in sorted(ROOT.glob("kapitel*.html")):
        all_issues.extend(audit_file(path))

    seen = set()
    unique = []
    for item in all_issues:
        key = (item["file"], item["text"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)

    print(f"Files scanned: {len(list(ROOT.glob('kapitel*.html')))}")
    print(f"Issues found: {len(unique)}")
    for item in unique:
        extra = f" | EN: {item['en']}" if "en" in item else ""
        print(f"  {item['file']}: {item['text'][:100]}{extra}")


if __name__ == "__main__":
    main()
