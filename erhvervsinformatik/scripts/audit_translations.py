"""Audit bilingual HTML for untranslated DA/EN pairs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_all import looks_danish  # noqa: E402

PAGE_GLOBS = ["introduktion.html", "kapitel-*.html", "erhvervsinformatik.html"]
HOSTS = {"p", "h1", "h2", "h3", "h4", "li", "td", "th", "figcaption", "a", "blockquote", "summary"}

ALLOW_SAME = re.compile(
    r"^(?:"
    r"[A-Z0-9][A-Za-z0-9&.\-® ]{0,60}(?:\.com|\.dk|\.org|\.html)?"
    r"|(?:MobilePay|Google Trends|OneNote|iBog|Ahlsell|e-conomic|Party-app|SQL|HTML|CSS|API|VPN|AI|IoT|USB|PDF|CSV|JSON|XML|HTTP|HTTPS|DNS|TCP|IP|GDPR|CSR|SEM|SEO|USB|B2B|B2C|C#|Java|Python|JavaScript|PHP|MySQL|Excel|PowerPoint|Word|Windows|Linux|Android|iOS|GitHub|YouTube|Facebook|Instagram|LinkedIn|Twitter|Bluetooth|Wi-Fi|EUD|EUX)"
    r")$",
    re.I,
)


def page_files() -> list[Path]:
    files: list[Path] = []
    for pattern in PAGE_GLOBS:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


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

    return issues


def main() -> None:
    files = page_files()
    all_issues: list[dict] = []
    for path in files:
        all_issues.extend(audit_file(path))

    seen = set()
    unique = []
    for item in all_issues:
        key = (item["file"], item["text"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)

    print(f"Files scanned: {len(files)}")
    print(f"Issues found: {len(unique)}")
    for item in unique:
        print(f"  {item['file']}: {item['text'][:120]}")

    if unique:
        out = ROOT / "scripts" / "audit_remaining.txt"
        out.write_text(
            "\n".join(f"{item['file']}\t{item['text']}" for item in unique),
            encoding="utf-8",
        )
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
