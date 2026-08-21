"""Re-translate bilingual spans where EN still equals DA."""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_all import Translator, looks_danish, purge_failed_translations  # noqa: E402
from key_terms import annotate_key_terms  # noqa: E402

MANUAL: dict[str, str] = {
    "Introduktion": "Introduction",
    "Tour de iBog": "Tour of the iBook",
    "Tips til læsning på skærm": "Tips for reading on screen",
    "Ordforklaringer": "Glossary",
    "Virksomheden": "The company",
    "Regnskab": "Accounts",
    "Budget": "Budget",
    "Omkostninger": "Costs",
    "Logistik": "Logistics",
    "Økonomisystem": "Financial system",
    "Økonomisk effektivitet": "Economic efficiency",
    "Kapitler": "Chapters",
    "Indhold": "Contents",
}

PAGE_GLOBS = ["introduktion.html", "kapitel-*.html"]
HOSTS = {
    "p", "h1", "h2", "h3", "h4", "li", "td", "th", "figcaption",
    "a", "blockquote", "summary",
}

SKIP_SAME = re.compile(
    r"^(?:"
    r"\d+(?:\.\d+)*\s*(?:AI|SQL|HTML|CSS|API|VPN|IoT|C\)|B2B|B2C)?"
    r"|MobilePay|Google Trends|OneNote|iBog|Ahlsell|e-conomic|Party-app"
    r"|GitHub|YouTube|Facebook|Instagram|LinkedIn|Bluetooth|Wi-Fi"
    r"|[A-Za-z0-9\-]+\.(?:dk|com|org)$"
    r")$",
    re.I,
)


def page_files() -> list[Path]:
    files: list[Path] = []
    for pattern in PAGE_GLOBS:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


def needs_translation(text: str) -> bool:
    if text in MANUAL:
        return True
    if len(text) <= 3:
        return False
    if SKIP_SAME.match(text):
        return False
    if looks_danish(text):
        return True
    return bool(re.search(r"\b(?:og|er|det|til|med|for|som|kapitel|opgave|data|program|sikkerhed)\b", text, re.I))


def collect_pairs(soup: BeautifulSoup) -> list[tuple]:
    fixes = []
    seen = set()
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
        if not needs_translation(da_t):
            continue
        if da_t in seen:
            continue
        seen.add(da_t)
        fixes.append((spans[0], spans[1], da_t))
    return fixes


def apply_fixes(soup: BeautifulSoup, translations: dict[str, str]) -> int:
    changed = 0
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
        new_en = translations.get(da_t)
        if not new_en or new_en == da_t:
            continue
        en_span = spans[1]
        en_span.clear()
        en_span.append(new_en)
        changed += 1
    return changed


def restore_key_terms(soup: BeautifulSoup, path: Path) -> None:
    match = re.match(r"kapitel-(\d+)\.html$", path.name)
    if not match:
        return
    article = soup.select_one("main.article")
    if article is not None:
        annotate_key_terms(article, int(match.group(1)))


def purge_identity_cache(tr: Translator) -> int:
    remove = []
    for key, value in tr.cache.items():
        if key != value:
            continue
        if key in MANUAL:
            remove.append(key)
            continue
        if SKIP_SAME.match(key):
            continue
        if needs_translation(key):
            remove.append(key)
    for key in remove:
        del tr.cache[key]
    return len(remove)


def translate_with_backoff(tr: Translator, texts: list[str]) -> dict[str, str]:
    translations: dict[str, str] = {}
    for index, text in enumerate(texts, start=1):
        tr.cache.pop(text, None)
        for attempt in range(6):
            tr.translate_many([text])
            result = MANUAL.get(text) or tr.cache.get(text) or tr.translate(text)
            if result and result != text:
                translations[text] = result
                break
            time.sleep(2.0 * (attempt + 1))
        else:
            translations[text] = translations.get(text, text)
        if index % 10 == 0:
            print(f"  translated {index}/{len(texts)}", flush=True)
            tr.save()
        time.sleep(0.5)
    tr.save()
    return translations


def main() -> None:
    tr = Translator()
    removed = purge_failed_translations(tr.cache) + purge_identity_cache(tr)
    tr.save()
    print(f"Purged {removed} cache entries", flush=True)

    all_pairs: dict[str, list] = {}
    for path in page_files():
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        for item in collect_pairs(soup):
            all_pairs.setdefault(item[2], []).append((path, item))

    texts = sorted(all_pairs)
    print(f"Unique untranslated strings: {len(texts)}", flush=True)
    if not texts:
        print("Nothing to fix.", flush=True)
        return

    translations = translate_with_backoff(tr, texts)

    total = 0
    touched = set()
    for path in page_files():
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        changed = apply_fixes(soup, translations)
        if changed:
            restore_key_terms(soup, path)
            path.write_text(soup.decode(formatter="html"), encoding="utf-8")
            print(f"{path.name}: fixed {changed}", flush=True)
            total += changed
            touched.add(path.name)

    tr.save()
    print(f"Done. Fixed {total} spans in {len(touched)} files.", flush=True)


if __name__ == "__main__":
    main()
