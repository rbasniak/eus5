"""Build bilingual chapter HTML pages for Virksomhedsøkonomi F-C."""
from __future__ import annotations

import html
import json
import re
import sys
import time
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag
from deep_translator import GoogleTranslator

from extract import extract_chapter
from key_terms import annotate_key_terms

ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = ROOT.parent
RAW = ROOT / "raw"
CACHE = ROOT / "scripts" / "cache" / "i18n.json"
EXTRACTED = ROOT / "scripts" / "extracted"
BOOK_SLUG = "virksomhedsokonomi-fc"
BOOK_INDEX = f"{BOOK_SLUG}.html"
BOOK_TITLE_DA = "Virksomhedsøkonomi F–C til EUD/EUX"
BOOK_TITLE_EN = "Business Economics F–C for EUD/EUX"
BOOK_SHORT = "Virksomhedsøkonomi"
BOOK_COVER = "https://frontpage-images-production.systime.dk/generated/9788761695079/highres.webp"

TRANSLATABLE = {"p", "h1", "h2", "h3", "h4", "li", "th", "td", "figcaption"}
NESTED = {"ul", "ol", "table", "div"}

CHAPTER_SOURCES = [
    {"folder": "Introduktion", "num": 0, "file": "introduktion.html"},
    {"folder": "Kapitel 1", "num": 1, "file": "kapitel-01.html"},
    {"folder": "Kapitel 2", "num": 2, "file": "kapitel-02.html"},
    {"folder": "Kapitel 3", "num": 3, "file": "kapitel-03.html"},
    {"folder": "Kapitel 4", "num": 4, "file": "kapitel-04.html"},
    {"folder": "Kapitel 5", "num": 5, "file": "kapitel-05.html"},
    {"folder": "Kapitel 6", "num": 6, "file": "kapitel-06.html"},
    {"folder": "Kapitel 7", "num": 7, "file": "kapitel-07.html"},
]

UI = {
    "Indhold": "Contents",
    "Kapitel": "Chapter",
    "Introduktion": "Introduction",
    "Ordforklaringer": "Glossary",
    "Alle kapitler": "All chapters",
    "Forrige": "Previous",
    "Næste": "Next",
    BOOK_TITLE_DA: BOOK_TITLE_EN,
    "Tre facts": "Three facts",
    "Par-aktivitet": "Pair activity",
    "Gruppe-aktivitet": "Group activity",
    "Opgaver til kapitel 1": "Tasks for chapter 1",
    "Opgaver til kapitel 2": "Tasks for chapter 2",
    "Opgaver til kapitel 3": "Tasks for chapter 3",
    "Opgaver til kapitel 4": "Tasks for chapter 4",
    "Opgaver til kapitel 5": "Tasks for chapter 5",
    "Opgaver til kapitel 6": "Tasks for chapter 6",
    "Opgaver til kapitel 7": "Tasks for chapter 7",
    "Caseopgaver til kapitel 1": "Case tasks for chapter 1",
    "Caseopgaver til kapitel 2": "Case tasks for chapter 2",
    "Caseopgaver til kapitel 3": "Case tasks for chapter 3",
    "Caseopgaver til kapitel 4": "Case tasks for chapter 4",
    "Caseopgaver til kapitel 5": "Case tasks for chapter 5",
    "Caseopgaver til kapitel 6": "Case tasks for chapter 6",
    "Caseopgaver til kapitel 7": "Case tasks for chapter 7",
    "Virksomheden": "The company",
    "Regnskab": "Accounts",
    "Budget": "Budget",
    "Omkostninger": "Costs",
    "Logistik": "Logistics",
    "Økonomisystem": "Financial system",
    "Økonomisk effektivitet": "Economic efficiency",
    "1. Virksomheden": "1. The company",
    "2. Regnskab": "2. Accounts",
    "3. Budget": "3. Budget",
    "4. Omkostninger": "4. Costs",
    "5. Logistik": "5. Logistics",
    "6. Økonomisystem": "6. Financial system",
    "7. Økonomisk effektivitet": "7. Economic efficiency",
    "Tips til læsning på skærm": "Tips for reading on screen",
    "Tour de iBog": "Tour of the iBook",
    "Virksomhedsøkonomi": "Business economics",
    "Debet": "Debit",
    "Kredit": "Credit",
    "Aktiver": "Assets",
    "Passiver": "Liabilities",
    "Resultatopgørelse": "Income statement",
    "Balance": "Balance sheet",
    "Likviditet": "Liquidity",
    "Soliditet": "Solvency",
    "Rentabilitet": "Profitability",
}

TERMS = [
    ("virksomhedsøkonomi", "business economics"),
    ("regnskab", "accounts"),
    ("regnskabet", "the accounts"),
    ("budget", "budget"),
    ("budgetter", "budgets"),
    ("omkostninger", "costs"),
    ("omkostning", "cost"),
    ("logistik", "logistics"),
    ("økonomisystem", "financial system"),
    ("økonomisystemer", "financial systems"),
    ("økonomisk effektivitet", "economic efficiency"),
    ("likviditet", "liquidity"),
    ("soliditet", "solvency"),
    ("rentabilitet", "profitability"),
    ("resultatopgørelse", "income statement"),
    ("balance", "balance sheet"),
    ("aktiver", "assets"),
    ("passiver", "liabilities"),
    ("debet", "debit"),
    ("kredit", "credit"),
    ("indtægter", "revenue"),
    ("indtægt", "revenue"),
    ("dækningsbidrag", "contribution margin"),
    ("nøgletal", "key figures"),
    ("lager", "inventory"),
    ("leverandør", "supplier"),
    ("leverandører", "suppliers"),
]

DANISH_HINT = re.compile(
    r"[æøåÆØÅ]|"
    r"\b(?:og|er|det|til|med|for|som|virksomhed\w*|kapitel\w*|elever\w*|"
    r"opgaver\w*|afsnit\w*|regnskab\w*|budget\w*|omkostning\w*|"
    r"økonomi\w*|likviditet\w*|aktiv\w*|passiv\w*|indtægt\w*|"
    r"design\w*|teknologi\w*|digital\w*|system\w*|opgave\w*|begreb\w*)\b",
    re.IGNORECASE,
)


def looks_danish(text: str) -> bool:
    return bool(DANISH_HINT.search(text))


def purge_failed_translations(cache: dict[str, str]) -> int:
    remove = [
        key
        for key, value in cache.items()
        if key == value and len(key) > 4 and looks_danish(key)
    ]
    for key in remove:
        del cache[key]
    return len(remove)


class Translator:
    def __init__(self) -> None:
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        self.cache: dict[str, str] = {}
        if CACHE.exists():
            self.cache = json.loads(CACHE.read_text(encoding="utf-8"))
        self.gt = GoogleTranslator(source="da", target="en")
        self.dirty = 0

    def save(self) -> None:
        CACHE.write_text(json.dumps(self.cache, ensure_ascii=False, indent=0), encoding="utf-8")

    def protect(self, text: str) -> str:
        out = text
        for index, (da, _en) in enumerate(TERMS):
            out = re.sub(rf"\b{re.escape(da)}\b", f"XTTERM{index}XT", out, flags=re.IGNORECASE)
        return out

    def unprotect(self, text: str) -> str:
        out = text
        for index, (_da, en) in enumerate(TERMS):
            out = re.sub(rf"XTT?ERM{index}XT", en, out, flags=re.IGNORECASE)
        return out

    def translate(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            return text
        if text in UI:
            return UI[text]
        if text in self.cache:
            return self.cache[text]
        if re.fullmatch(r"[\d\s.,:%€$+\-–—/&()]+", text):
            self.cache[text] = text
            return text
        self.translate_many([text])
        return self.cache.get(text, text)

    def should_cache(self, src: str, dst: str) -> bool:
        if not dst:
            return False
        if src != dst:
            return True
        if len(src) <= 4 or not looks_danish(src):
            return True
        return False

    def translate_batch_with_retry(self, chunk: list[str]) -> list[str]:
        protected = [self.protect(item) for item in chunk]
        for attempt in range(4):
            try:
                translated = self.gt.translate_batch(protected)
                if translated and len(translated) == len(chunk):
                    return [self.unprotect(item or src) for item, src in zip(translated, chunk)]
            except Exception as exc:
                print(f"  batch retry {attempt + 1}: {str(exc)[:80]}", flush=True)
            time.sleep(2.0 * (attempt + 1))
        translated = []
        for src in chunk:
            try:
                out = self.unprotect(self.gt.translate(self.protect(src)) or "")
                translated.append(out or src)
            except Exception:
                translated.append(src)
            time.sleep(0.75)
        return translated

    def translate_many(self, texts: list[str]) -> None:
        missing = []
        seen = set()
        for text in texts:
            text = re.sub(r"\s+", " ", text).strip()
            if not text or text in self.cache or text in seen:
                continue
            if text in UI or re.fullmatch(r"[\d\s.,:%€$+\-–—/&()]+", text):
                self.cache[text] = UI.get(text, text)
                continue
            seen.add(text)
            missing.append(text)
        if not missing:
            return
        print(f"  translating {len(missing)} new strings ({len(self.cache)} cached)", flush=True)
        batch_size = 5
        for index in range(0, len(missing), batch_size):
            chunk = missing[index : index + batch_size]
            translated = self.translate_batch_with_retry(chunk)
            for src, dst in zip(chunk, translated):
                if self.should_cache(src, dst):
                    self.cache[src] = dst
            self.save()
            print(f"  ... {min(index + batch_size, len(missing))}/{len(missing)}", flush=True)
            time.sleep(1.0)


def get_soup(el: Tag) -> BeautifulSoup:
    cur: Tag | BeautifulSoup = el
    while getattr(cur, "parent", None) is not None:
        cur = cur.parent
    return cur  # type: ignore[return-value]


def wrap_pair(host: Tag, da_html: str, en_text: str) -> list:
    soup = get_soup(host)
    da_span = soup.new_tag("span", attrs={"lang": "da"})
    da_frag = BeautifulSoup(da_html, "html.parser")
    for child in list(da_frag.contents):
        da_span.append(child)
    en_span = soup.new_tag("span", attrs={"lang": "en"})
    en_span.append(NavigableString(en_text))
    return [da_span, en_span]


def wrap_element(el: Tag, tr: Translator) -> None:
    plain = el.get_text(" ", strip=True)
    if not plain:
        return
    da_html = el.decode_contents()
    en = tr.translate(plain)
    el.clear()
    for node in wrap_pair(el, da_html, en):
        el.append(node)


def wrap_direct_strings(el: Tag, tr: Translator) -> None:
    soup = get_soup(el)
    for child in list(el.children):
        if isinstance(child, NavigableString) and child.strip():
            da = re.sub(r"\s+", " ", str(child)).strip()
            en = tr.translate(da)
            da_span = soup.new_tag("span", attrs={"lang": "da"})
            da_span.string = da
            en_span = soup.new_tag("span", attrs={"lang": "en"})
            en_span.string = en
            child.replace_with(da_span)
            da_span.insert_after(en_span)


def collect_strings(article: Tag) -> list[str]:
    out: list[str] = []
    els = [el for el in article.find_all(TRANSLATABLE) if isinstance(el, Tag)]
    els.sort(key=lambda element: len(list(element.parents)), reverse=True)
    for el in els:
        if el.find(list(TRANSLATABLE | NESTED), recursive=False):
            for child in el.children:
                if isinstance(child, NavigableString) and child.strip():
                    out.append(re.sub(r"\s+", " ", str(child)).strip())
        else:
            plain = el.get_text(" ", strip=True)
            if plain:
                out.append(plain)
    return out


def bilingualize(article: Tag, tr: Translator) -> None:
    els = [el for el in article.find_all(TRANSLATABLE) if isinstance(el, Tag)]
    els.sort(key=lambda element: len(list(element.parents)), reverse=True)
    for el in els:
        if el.find(list(TRANSLATABLE | NESTED), recursive=False):
            wrap_direct_strings(el, tr)
        else:
            wrap_element(el, tr)


def add_boxes(article: Tag) -> None:
    for h3 in list(article.find_all("h3")):
        text = h3.get_text(" ", strip=True)
        low = text.lower()
        kind = None
        label_da = None
        label_en = None
        if low.startswith("tre facts"):
            kind, label_da, label_en = "facts", "Tre facts", "Three facts"
        elif low.startswith("par-aktivitet"):
            kind, label_da, label_en = "exercise", "Par-aktivitet", "Pair activity"
        elif low.startswith("gruppe-aktivitet"):
            kind, label_da, label_en = "exercise", "Gruppe-aktivitet", "Group activity"
        if not kind:
            continue
        soup = get_soup(article)
        box = soup.new_tag("div", attrs={"class": f"box {kind}"})
        label = soup.new_tag("div", attrs={"class": "label"})
        da_span = soup.new_tag("span", attrs={"lang": "da"})
        da_span.string = label_da
        en_span = soup.new_tag("span", attrs={"lang": "en"})
        en_span.string = label_en
        label.append(da_span)
        label.append(en_span)
        h3.insert_before(box)
        box.append(label)
        box.append(h3.extract())
        nxt = box.next_sibling
        moved = 0
        while nxt is not None and moved < 12:
            current = nxt
            nxt = current.next_sibling
            if isinstance(current, NavigableString) and not str(current).strip():
                continue
            if isinstance(current, Tag) and current.name in {"h2", "h3"}:
                break
            if isinstance(current, Tag):
                box.append(current.extract())
                moved += 1


def toc_html(article: Tag) -> str:
    links = []
    for h2 in article.find_all("h2"):
        anchor = h2.get("id") or ""
        inner = h2.decode_contents()
        links.append(f'<a href="#{anchor}">{inner}</a>')
    nav = "\n".join(links)
    return f"""<details class="toc">
  <summary><span lang="da">Indhold</span><span lang="en">Contents</span></summary>
  <nav>{nav}</nav>
</details>"""


def chapter_nav_label(num: int) -> tuple[str, str]:
    if num == 0:
        return "Introduktion", "Introduction"
    return f"Kapitel {num}", f"Chapter {num}"


def chapter_label(ch: dict) -> tuple[str, str]:
    num = ch["num"]
    da = ch["title_da"]
    en = ch["title_en"]
    if num == 0:
        return "Introduktion", "Introduction"
    da = re.sub(rf"^{num}\.\s*", "", da).strip()
    en = re.sub(rf"^{num}\.\s*", "", en).strip()
    return da, en


def render_page(
    *,
    num: int,
    title_da: str,
    title_en: str,
    article_html: str,
    toc: str,
    prev_ch: dict | None,
    next_ch: dict | None,
) -> str:
    nav_da, nav_en = chapter_nav_label(num)
    prev_html = ""
    next_html = ""
    if prev_ch:
        prev_html = (
            f'<a class="prev" href="{prev_ch["file"]}">'
            f'<span lang="da">← {html.escape(prev_ch["title_da"])}</span>'
            f'<span lang="en">← {html.escape(prev_ch["title_en"])}</span></a>'
        )
    if next_ch:
        next_html = (
            f'<a class="next" href="{next_ch["file"]}">'
            f'<span lang="da">{html.escape(next_ch["title_da"])} →</span>'
            f'<span lang="en">{html.escape(next_ch["title_en"])} →</span></a>'
        )
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title_da)} – {BOOK_SHORT}</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><a href="{BOOK_INDEX}">{BOOK_SHORT}</a> · <span lang="da">{nav_da}</span><span lang="en">{nav_en}</span></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap">
    {toc}
    <main class="article">
      <p class="kicker"><span lang="da">{html.escape(BOOK_TITLE_DA)}</span><span lang="en">{html.escape(BOOK_TITLE_EN)}</span></p>
      <h1 id="s0"><span lang="da">{html.escape(title_da)}</span><span lang="en">{html.escape(title_en)}</span></h1>
      {article_html}
      <nav class="chapter-nav">{prev_html}{next_html}</nav>
    </main>
  </div>
  <script src="assets/i18n.js"></script>
</body>
</html>
"""


def render_index(chapters: list[dict]) -> str:
    items = []
    for ch in chapters:
        da, en = chapter_label(ch)
        num = ch["num"]
        items.append(
            f'<a class="chapter-card" href="{ch["file"]}">'
            f'<img src="assets/chapters/ch{num:02d}.svg" alt="" width="320" height="180" loading="lazy">'
            f'<div class="chapter-card-body">'
            f'<span class="chapter-num">{num if num > 0 else "i"}</span>'
            f'<h2><span lang="da">{html.escape(da)}</span>'
            f'<span lang="en">{html.escape(en)}</span></h2>'
            f"</div></a>"
        )
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(BOOK_TITLE_DA)}</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><a href="../index.html">{BOOK_SHORT}</a></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap wrap-wide">
    <main class="article">
      <p class="kicker"><span lang="da">{html.escape(BOOK_TITLE_DA)}</span><span lang="en">{html.escape(BOOK_TITLE_EN)}</span></p>
      <h1><span lang="da">Kapitler</span><span lang="en">Chapters</span></h1>
      <div class="chapter-grid">
        {"".join(items)}
      </div>
    </main>
  </div>
  <script src="assets/i18n.js"></script>
</body>
</html>
"""


def render_book_picker() -> str:
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bøger</title>
  <link rel="stylesheet" href="afsætning-fc/assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><span lang="da">EUD/EUX</span><span lang="en">EUD/EUX</span></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap wrap-wide">
    <main class="article">
      <h1><span lang="da">Vælg bog</span><span lang="en">Choose a book</span></h1>
      <div class="book-grid">
        <a class="book-card" href="afsætning-fc/afsætning-fc.html">
          <img src="afsætning-fc/assets/book1.webp" alt="" width="240" height="340" loading="lazy">
          <h2><span lang="da">Afsætning F–C til EUD/EUX</span><span lang="en">Marketing F–C for EUD/EUX</span></h2>
        </a>
        <a class="book-card" href="virksomhedsokonomi-fc/{BOOK_INDEX}">
          <img src="{BOOK_COVER}" alt="" width="240" height="340" loading="lazy">
          <h2><span lang="da">{html.escape(BOOK_TITLE_DA)}</span><span lang="en">{html.escape(BOOK_TITLE_EN)}</span></h2>
        </a>
        <a class="book-card" href="erhvervsinformatik/erhvervsinformatik.html">
          <img src="https://frontpage-images-production.systime.dk/generated/9788761696670/highres.webp" alt="" width="240" height="340" loading="lazy">
          <h2><span lang="da">Erhvervsinformatik til EUD/EUX</span><span lang="en">Business Informatics for EUD/EUX</span></h2>
        </a>
      </div>
    </main>
  </div>
  <script src="afsætning-fc/assets/i18n.js"></script>
</body>
</html>
"""


def build_chapter(folder: Path, output_file: str, num: int, tr: Translator) -> dict:
    data = extract_chapter(folder)
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    slug = output_file.replace(".html", "")
    (EXTRACTED / f"{slug}.da.html").write_text(data["html"], encoding="utf-8")
    soup = BeautifulSoup(f'<article class="article">{data["html"]}</article>', "html.parser")
    article = soup.article
    first_h2 = article.find("h2")
    if first_h2 and first_h2.get_text(" ", strip=True) == data["title"]:
        first_h2.decompose()
    tr.translate_many(collect_strings(article) + [data["title"]])
    bilingualize(article, tr)
    add_boxes(article)
    toc = toc_html(article)
    vocabulary = annotate_key_terms(article, num)
    if vocabulary["terms"]:
        print(
            "  vocabulary:"
            f" {vocabulary['terms']} terms,"
            f" {vocabulary['existing']} source glossary,"
            f" {vocabulary['da']} Danish matches,"
            f" {vocabulary['en']} English matches",
            flush=True,
        )
    inner = article.decode_contents()
    title_en = tr.translate(data["title"])
    return {
        "num": num,
        "title_da": data["title"],
        "title_en": title_en,
        "file": output_file,
        "inner": inner,
        "toc": toc,
    }


def write_chapter_page(ch: dict, prev_ch: dict | None, next_ch: dict | None) -> None:
    page = render_page(
        num=ch["num"],
        title_da=ch["title_da"],
        title_en=ch["title_en"],
        article_html=ch["inner"],
        toc=ch["toc"],
        prev_ch=prev_ch,
        next_ch=next_ch,
    )
    out = ROOT / ch["file"]
    out.write_text(page, encoding="utf-8")
    print("Wrote", out.name, "chars=", out.stat().st_size, flush=True)


def nav_entry(ch: dict) -> dict:
    da, en = chapter_label(ch)
    if ch["num"] > 0:
        prefix_da = f'{ch["num"]}. '
        prefix_en = f'{ch["num"]}. '
        return {
            "file": ch["file"],
            "title_da": prefix_da + da,
            "title_en": prefix_en + en,
        }
    return {"file": ch["file"], "title_da": da, "title_en": en}


def main() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    only = None
    if "--only" in sys.argv:
        only = int(sys.argv[sys.argv.index("--only") + 1])
    tr = Translator()
    if "--retranslate" in sys.argv:
        removed = purge_failed_translations(tr.cache)
        tr.save()
        print(f"Purged {removed} failed cache entries", flush=True)

    sources = CHAPTER_SOURCES
    if only is not None:
        sources = [item for item in sources if item["num"] == only]

    built: list[dict] = []
    try:
        for source in sources:
            folder = RAW / source["folder"]
            print(f"=== {source['folder']} ===", flush=True)
            if not folder.exists():
                print(f"  SKIP missing folder: {folder}", flush=True)
                continue
            ch = build_chapter(folder, source["file"], source["num"], tr)
            tr.save()
            built.append(ch)
            print(f"  extracted+translated: {ch['title_da']}", flush=True)

        built.sort(key=lambda ch: ch["num"])
        for index, ch in enumerate(built):
            prev_ch = nav_entry(built[index - 1]) if index > 0 else None
            next_ch = nav_entry(built[index + 1]) if index + 1 < len(built) else None
            write_chapter_page(ch, prev_ch, next_ch)

        if built and only is None:
            (ROOT / BOOK_INDEX).write_text(render_index(built), encoding="utf-8")
    finally:
        tr.save()
        if only is None and built:
            (ROOT / BOOK_INDEX).write_text(render_index(built), encoding="utf-8")
            (SITE_ROOT / "index.html").write_text(render_book_picker(), encoding="utf-8")
            print(f"Wrote index.html and {BOOK_INDEX}")


if __name__ == "__main__":
    main()
