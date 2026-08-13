"""Build bilingual chapter HTML pages from Systime dumps."""
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

ROOT = Path(r"g:\Repositories\Pessoal\afsætning-f-c-til-eudeux")
RAW = ROOT / "raw"
CACHE = ROOT / "scripts" / "cache" / "i18n.json"
EXTRACTED = ROOT / "scripts" / "extracted"

TRANSLATABLE = {"p", "h1", "h2", "h3", "h4", "li", "th", "td", "figcaption"}
NESTED = {"ul", "ol", "table", "div"}

UI = {
    "Indhold": "Contents",
    "Kapitel": "Chapter",
    "Alle kapitler": "All chapters",
    "Forrige": "Previous",
    "Næste": "Next",
    "Afsætning F–C til EUD/EUX": "Marketing F–C for EUD/EUX",
    "Tre facts": "Three facts",
    "Par-aktivitet": "Pair activity",
    "Gruppe-aktivitet": "Group activity",
    "7.1 Forbrugernes behov": "7.1 Consumer needs",
    "Kulturbestemte behov": "Culturally determined needs",
    "Forbrugerens behov": "The consumer's needs",
    "Fysiske behov": "Physical needs",
    "Sociale behov": "Social needs",
    "Købstyper": "Purchase types",
    "Købscenter": "Shopping centre",
    "9.5 Mærke": "9.5 Brand",
    "Mærkevare": "Brand-name product",
}

TERMS = [
    ("forretningsmodeller", "business models"),
    ("forretningsmodellen", "the business model"),
    ("forretningsmodel", "business model"),
    ("forretningskonceptet", "the business concept"),
    ("forretningskoncept", "business concept"),
    ("værditilbud", "value proposition"),
    ("handelsvirksomheder", "trading companies"),
    ("handelsvirksomhed", "trading company"),
    ("produktionsvirksomheder", "manufacturing companies"),
    ("produktionsvirksomhed", "manufacturing company"),
    ("servicevirksomheder", "service companies"),
    ("servicevirksomhed", "service company"),
    ("serviceydelsen", "the service"),
    ("serviceydelse", "service"),
    ("grossister", "wholesalers"),
    ("grossist", "wholesaler"),
    ("detailhandlen", "retail"),
    ("detailhandel", "retail"),
    ("målgruppen", "the target group"),
    ("målgruppe", "target group"),
    ("købsadfærd", "buying behaviour"),
    ("købsadfærden", "buying behaviour"),
    ("segmentering", "segmentation"),
    ("sortimentet", "the assortment"),
    ("sortiment", "assortment"),
    ("cirkulær økonomi", "circular economy"),
    ("abonnementsordninger", "subscription models"),
    ("abonnementsordning", "subscription model"),
]

DANISH_HINT = re.compile(
    r"[æøåÆØÅ]|"
    r"\b(?:og|er|det|til|med|for|som|virksomhed\w*|kapitel\w*|elever\w*|markedsføring\w*|"
    r"opgaver\w*|afsnit\w*|kunder\w*|produkt\w*|lærer\w*|eleven\w*|interne\w*|eksterne\w*|"
    r"styrker\w*|svagheder\w*|muligheder\w*|trusler\w*|forbruger\w*|behov\w*|"
    r"anvendelse\w*|geografi\w*|konsument\w*|producent\w*|sortiment\w*|"
    r"organisation\w*|placering\w*|priser\w*|marked\w*|opgave\w*|begreb\w*)\b",
    re.IGNORECASE,
)


def looks_danish(text: str) -> bool:
    return bool(DANISH_HINT.search(text))


def purge_failed_translations(cache: dict[str, str]) -> int:
    remove = [
        k
        for k, v in cache.items()
        if k == v and len(k) > 4 and looks_danish(k)
    ]
    for k in remove:
        del cache[k]
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
        for i, (da, _en) in enumerate(TERMS):
            out = re.sub(rf"\b{re.escape(da)}\b", f"XTTERM{i}XT", out, flags=re.IGNORECASE)
        return out

    def unprotect(self, text: str) -> str:
        out = text
        for i, (_da, en) in enumerate(TERMS):
            out = re.sub(rf"XTTERM{i}XT", en, out, flags=re.IGNORECASE)
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
        protected = [self.protect(t) for t in chunk]
        for attempt in range(4):
            try:
                translated = self.gt.translate_batch(protected)
                if translated and len(translated) == len(chunk):
                    return [self.unprotect(t or s) for t, s in zip(translated, chunk)]
            except Exception as exc:
                print(f"  batch retry {attempt + 1}: {str(exc)[:80]}", flush=True)
            time.sleep(1.5 * (attempt + 1))
        translated = []
        for src in chunk:
            try:
                out = self.unprotect(self.gt.translate(self.protect(src)) or "")
                translated.append(out or src)
            except Exception:
                translated.append(src)
            time.sleep(0.15)
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
        batch_size = 15
        for i in range(0, len(missing), batch_size):
            chunk = missing[i : i + batch_size]
            translated = self.translate_batch_with_retry(chunk)
            for src, dst in zip(chunk, translated):
                if self.should_cache(src, dst):
                    self.cache[src] = dst
            self.save()
            print(f"  ... {min(i + batch_size, len(missing))}/{len(missing)}", flush=True)
            time.sleep(0.35)


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
    els.sort(key=lambda e: len(list(e.parents)), reverse=True)
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
    els.sort(key=lambda e: len(list(e.parents)), reverse=True)
    for el in els:
        if el.find(list(TRANSLATABLE | NESTED), recursive=False):
            wrap_direct_strings(el, tr)
        else:
            wrap_element(el, tr)


def add_boxes(article: Tag) -> None:
    soup = article
    for h3 in list(article.find_all("h3")):
        text = h3.get_text(" ", strip=True)
        low = text.lower()
        kind = None
        label_da = None
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
        en_span.string = "Three facts" if kind == "facts" else (
            "Pair activity" if "par-" in low else "Group activity"
        )
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


CH14_SLUGS = [
    "ed-as",
    "ikea",
    "airtox-b2b",
    "boozt",
    "lakrids-bulow-b2b",
    "too-good-to-go",
    "jysk-b2c",
    "jysk-b2b",
    "soestrene-grene",
    "joe-the-juice",
]


def add_heading_ids(article: Tag) -> None:
    for i, h in enumerate(article.find_all("h3"), start=1):
        if not h.get("id"):
            h["id"] = f"s{i}"


def toc_html_h3(article: Tag) -> str:
    headings = article.find_all("h3")
    if not headings:
        return ""
    links = []
    for h in headings:
        anchor = h.get("id") or ""
        inner = h.decode_contents()
        links.append(f'<a href="#{anchor}">{inner}</a>')
    nav = "\n".join(links)
    return f"""<details class="toc">
  <summary><span lang="da">Indhold</span><span lang="en">Contents</span></summary>
  <nav>{nav}</nav>
</details>"""


def first_image(html_content: str, fallback: str = "assets/chapters/ch14.svg") -> str:
    m = re.search(r'src="([^"]+)"', html_content)
    return m.group(1) if m else fallback


def render_case_index(cases: list[dict], prev_ch: dict | None) -> str:
    items = []
    for i, case in enumerate(cases):
        items.append(
            f'<a class="chapter-card" href="{case["file"]}">'
            f'<img src="{html.escape(case["image"])}" alt="" width="320" height="180" loading="lazy">'
            f'<div class="chapter-card-body">'
            f'<span class="chapter-num">{i + 1}</span>'
            f'<h2><span lang="da">{html.escape(case["title_da"])}</span>'
            f'<span lang="en">{html.escape(case["title_en"])}</span></h2>'
            f"</div></a>"
        )
    prev_html = ""
    if prev_ch:
        prev_html = (
            f'<a class="prev" href="{prev_ch["file"]}">'
            f'<span lang="da">← {html.escape(prev_ch["title_da"])}</span>'
            f'<span lang="en">← {html.escape(prev_ch["title_en"])}</span></a>'
        )
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>14. Casevirksomheder – Afsætning F-C</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><a href="afsætning-fc.html">Afsætning F–C</a> · <span lang="da">Kapitel 14</span><span lang="en">Chapter 14</span></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap wrap-wide">
    <main class="article">
      <p class="kicker"><span lang="da">Afsætning F–C til EUD/EUX</span><span lang="en">Marketing F–C for EUD/EUX</span></p>
      <h1><span lang="da">14. Casevirksomheder</span><span lang="en">14. Case companies</span></h1>
      <div class="chapter-grid">
        {"".join(items)}
      </div>
      <nav class="chapter-nav">{prev_html}</nav>
    </main>
  </div>
  <script src="assets/i18n.js"></script>
</body>
</html>
"""


def render_case_page(
    *,
    title_da: str,
    title_en: str,
    article_html: str,
    toc: str,
    prev_nav: dict | None,
    next_nav: dict | None,
) -> str:
    prev_html = ""
    next_html = ""
    if prev_nav:
        prev_html = (
            f'<a class="prev" href="{prev_nav["file"]}">'
            f'<span lang="da">← {html.escape(prev_nav["title_da"])}</span>'
            f'<span lang="en">← {html.escape(prev_nav["title_en"])}</span></a>'
        )
    if next_nav:
        next_html = (
            f'<a class="next" href="{next_nav["file"]}">'
            f'<span lang="da">{html.escape(next_nav["title_da"])} →</span>'
            f'<span lang="en">{html.escape(next_nav["title_en"])} →</span></a>'
        )
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title_da)} – Afsætning F-C</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><a href="afsætning-fc.html">Afsætning F–C</a> · <a href="kapitel-14.html"><span lang="da">Kapitel 14</span><span lang="en">Chapter 14</span></a></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap">
    {toc}
    <main class="article">
      <p class="kicker"><span lang="da">Afsætning F–C til EUD/EUX</span><span lang="en">Marketing F–C for EUD/EUX</span></p>
      <h1 id="s0"><span lang="da">{html.escape(title_da)}</span><span lang="en">{html.escape(title_en)}</span></h1>
      {article_html}
      <nav class="chapter-nav">{prev_html}{next_html}</nav>
    </main>
  </div>
  <script src="assets/i18n.js"></script>
</body>
</html>
"""


def build_chapter_14(folder: Path, tr: Translator, prev_ch: dict | None) -> dict:
    if prev_ch is None:
        prev_ch = {
            "file": "kapitel-13.html",
            "title_da": "13. Kundeservice og -betjening",
            "title_en": "13. Customer service",
        }
    data = extract_chapter(folder)
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    cases: list[dict] = []

    for i, section in enumerate(data["sections"]):
        slug = CH14_SLUGS[i] if i < len(CH14_SLUGS) else f"case-{i + 1:02d}"
        filename = f"kapitel-14-{slug}.html"
        soup = BeautifulSoup(f'<article class="article">{section["html"]}</article>', "html.parser")
        article = soup.article
        add_heading_ids(article)
        tr.translate_many(collect_strings(article) + [section["title"]])
        bilingualize(article, tr)
        add_boxes(article)
        inner = article.decode_contents()
        toc = toc_html_h3(article)
        title_en = tr.translate(section["title"])
        case = {
            "slug": slug,
            "title_da": section["title"],
            "title_en": title_en,
            "file": filename,
            "image": first_image(section["html"]),
            "inner": inner,
            "toc": toc,
        }
        cases.append(case)

    for i, case in enumerate(cases):
        prev_nav = cases[i - 1] if i > 0 else prev_ch
        next_nav = cases[i + 1] if i + 1 < len(cases) else None
        page = render_case_page(
            title_da=case["title_da"],
            title_en=case["title_en"],
            article_html=case["inner"],
            toc=case["toc"],
            prev_nav=prev_nav,
            next_nav=next_nav,
        )
        out = ROOT / case["file"]
        out.write_text(page, encoding="utf-8")
        print("Wrote", out.name, flush=True)

    index = render_case_index(cases, prev_ch)
    (ROOT / "kapitel-14.html").write_text(index, encoding="utf-8")
    print("Wrote kapitel-14.html (case index)", flush=True)

    return {
        "num": 14,
        "title_da": "Casevirksomheder",
        "title_en": "Case companies",
        "file": "kapitel-14.html",
    }


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
    prev_html = ""
    next_html = ""
    if prev_ch:
        prev_html = (
            f'<a class="prev" href="{prev_ch["file"]}">'
            f'<span lang="da">← {prev_ch["title_da"]}</span>'
            f'<span lang="en">← {html.escape(prev_ch["title_en"])}</span></a>'
        )
    if next_ch:
        next_html = (
            f'<a class="next" href="{next_ch["file"]}">'
            f'<span lang="da">{next_ch["title_da"]} →</span>'
            f'<span lang="en">{html.escape(next_ch["title_en"])} →</span></a>'
        )
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title_da)} – Afsætning F-C</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><a href="afsætning-fc.html">Afsætning F–C</a> · <span lang="da">Kapitel {num}</span><span lang="en">Chapter {num}</span></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap">
    {toc}
    <main class="article">
      <p class="kicker"><span lang="da">Afsætning F–C til EUD/EUX</span><span lang="en">Marketing F–C for EUD/EUX</span></p>
      <h1 id="s0"><span lang="da">{html.escape(title_da)}</span><span lang="en">{html.escape(title_en)}</span></h1>
      {article_html}
      <nav class="chapter-nav">{prev_html}{next_html}</nav>
    </main>
  </div>
  <script src="assets/i18n.js"></script>
</body>
</html>
"""


def chapter_label(ch: dict) -> tuple[str, str]:
    n = ch["num"]
    da = re.sub(rf"^{n}\.\s*", "", ch["title_da"]).strip()
    en = re.sub(rf"^{n}\.\s*", "", ch["title_en"]).strip()
    if n == 14 and da.lower() in {"ed a/s", "ed as"}:
        da, en = "Casevirksomheder", "Case companies"
    return da, en


def render_book_picker() -> str:
    return """<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bøger</title>
  <link rel="stylesheet" href="assets/style.css">
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
  <div class="wrap">
    <main class="article">
      <h1><span lang="da">Vælg bog</span><span lang="en">Choose a book</span></h1>
      <div class="book-grid">
        <a class="book-card" href="afsætning-fc.html">
          <img src="assets/book1.webp" alt="" width="240" height="340" loading="lazy">
          <h2><span lang="da">Afsætning F–C til EUD/EUX</span><span lang="en">Marketing F–C for EUD/EUX</span></h2>
        </a>
      </div>
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
            f'<span class="chapter-num">{num}</span>'
            f'<h2><span lang="da">{html.escape(da)}</span>'
            f'<span lang="en">{html.escape(en)}</span></h2>'
            f"</div></a>"
        )
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Afsætning F–C til EUD/EUX</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand"><a href="index.html">Afsætning F–C</a></div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap wrap-wide">
    <main class="article">
      <p class="kicker"><span lang="da">Afsætning F–C til EUD/EUX</span><span lang="en">Marketing F–C for EUD/EUX</span></p>
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


def folder_num(name: str) -> int:
    m = re.search(r"(\d+)", name)
    return int(m.group(1)) if m else 99


def build_chapter(folder: Path, tr: Translator) -> dict:
    data = extract_chapter(folder)
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    num = folder_num(folder.name)
    (EXTRACTED / f"kapitel-{num:02d}.da.html").write_text(data["html"], encoding="utf-8")
    soup = BeautifulSoup(f'<article class="article">{data["html"]}</article>', "html.parser")
    article = soup.article
    # Drop duplicate first h2 if it repeats the chapter title
    first_h2 = article.find("h2")
    if first_h2 and first_h2.get_text(" ", strip=True) == data["title"]:
        first_h2.decompose()
    tr.translate_many(collect_strings(article) + [data["title"]])
    bilingualize(article, tr)
    add_boxes(article)
    # article inner without the wrapper's first h1
    inner = article.decode_contents()
    toc = toc_html(article)
    title_en = tr.translate(data["title"])
    return {
        "num": num,
        "title_da": data["title"],
        "title_en": title_en,
        "file": f"kapitel-{num:02d}.html",
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
    folders = sorted(RAW.glob("Kapitel *"), key=lambda p: folder_num(p.name))
    if only:
        folders = [p for p in folders if folder_num(p.name) == only]
    all_nums = sorted({folder_num(p.name) for p in folders} | {1})
    built: list[dict] = []
    try:
        for folder in folders:
            num = folder_num(folder.name)
            print(f"=== Kapitel {num} ===", flush=True)
            if num == 1:
                built.append(
                    {
                        "num": 1,
                        "title_da": "Forretningsmodeller",
                        "title_en": "Business models",
                        "file": "kapitel-01.html",
                    }
                )
                continue
            prev_ch = next((c for c in built if c["num"] == num - 1), None)
            if num == 14:
                ch = build_chapter_14(folder, tr, prev_ch)
                tr.save()
                built.append(ch)
                if not only:
                    (ROOT / "afsætning-fc.html").write_text(render_index(built), encoding="utf-8")
                print(f"  case index + {len(CH14_SLUGS)} cases", flush=True)
                continue
            ch = build_chapter(folder, tr)
            tr.save()
            built.append(ch)
            next_num = num + 1
            next_ch = None
            if next_num in all_nums:
                next_ch = {
                    "file": f"kapitel-{next_num:02d}.html",
                    "title_da": f"Kapitel {next_num}",
                    "title_en": f"Chapter {next_num}",
                }
            write_chapter_page(ch, prev_ch, next_ch)
            if not only:
                (ROOT / "afsætning-fc.html").write_text(render_index(built), encoding="utf-8")
            print(f"  extracted+translated: {ch['title_da']}", flush=True)
    finally:
        tr.save()
        if not only:
            (ROOT / "index.html").write_text(render_book_picker(), encoding="utf-8")
            (ROOT / "afsætning-fc.html").write_text(render_index(built), encoding="utf-8")
            print("Wrote index.html and afsætning-fc.html")


if __name__ == "__main__":
    main()
