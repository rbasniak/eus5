"""Extract readable educational content from Systime Vue HTML dumps."""
from __future__ import annotations

import html
import re
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

DECOMPOSE_TAGS = {"script", "style", "svg", "button", "noscript"}
DECOMPOSE_CLASS_SUBSTR = (
    "breadcrumbs",
    "page-title__utils",
    "ce-header__utils",
    "section-index-list",
    "markdown-editor",
    "writing-task-no-contextmenu",
    "meta-data-content",
    "meta-data-image",
    "ce-media-image__overlay-btn",
    "expansion-chevron",
    "v-expansion-panel__shadow",
    "v-expansion-panel-title__overlay",
)

SKIP_HEADER_PREFIXES = (
    "lærertip",
    "laerertip",
    "download",
)

YEAR_SUFFIX = re.compile(r"\s*\(20\d{2}-20\d{2}\)\s*$")


def class_str(el: Tag) -> str:
    if not isinstance(el, Tag) or el.attrs is None:
        return ""
    c = el.get("class") or []
    if isinstance(c, str):
        return c
    return " ".join(c)


def should_decompose(el: Tag) -> bool:
    if el.name in DECOMPOSE_TAGS:
        return True
    classes = class_str(el)
    return any(part in classes for part in DECOMPOSE_CLASS_SUBSTR)


def clean_text(s: str) -> str:
    s = html.unescape(s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def clean_title(s: str) -> str:
    return YEAR_SUFFIX.sub("", clean_text(s)).strip()


def extract_img(img: Tag) -> str:
    src = (img.get("src") or "").strip()
    if not src or src.startswith("data:"):
        return ""
    alt = clean_text(img.get("alt") or img.get("title") or "")
    cap = f"<figcaption>{html.escape(alt)}</figcaption>" if alt else ""
    return (
        f'<figure class="figure"><img src="{html.escape(src)}" alt="{html.escape(alt)}" '
        f'loading="lazy">{cap}</figure>'
    )


def extract_inline(el: Tag) -> str:
    parts: list[str] = []
    for child in el.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            raw = str(child)
            if not raw:
                continue
            if raw.strip():
                parts.append(html.escape(clean_text(raw)))
            elif parts:
                parts.append(" ")
            continue
        if not isinstance(child, Tag):
            continue
        if child.name == "br":
            parts.append("<br>")
        elif child.name in {"strong", "b"}:
            inner = extract_inline(child)
            if inner:
                parts.append(f"<strong>{inner}</strong>")
        elif child.name in {"em", "i"}:
            inner = extract_inline(child)
            if inner:
                parts.append(f"<em>{inner}</em>")
        elif child.name == "a":
            href = child.get("href") or ""
            inner = extract_inline(child)
            classes = class_str(child)
            if "glossary-term" in classes:
                parts.append(f'<span class="term">{inner}</span>')
            elif href.startswith("http") and "systime.dk" not in href:
                parts.append(
                    f'<a href="{html.escape(href)}" target="_blank" rel="noopener">{inner}</a>'
                )
            else:
                parts.append(inner)
        elif child.name in {"ul", "ol"}:
            parts.append(extract_list(child))
        else:
            parts.append(extract_inline(child))
    return "".join(parts).strip()


def extract_list(lst: Tag) -> str:
    items = []
    for li in lst.find_all("li", recursive=False):
        has_block = any(
            isinstance(c, Tag) and c.name in {"p", "ul", "ol", "table", "blockquote"}
            for c in li.children
        )
        inner = extract_flow(li) if has_block else extract_inline(li)
        inner = inner.strip()
        if inner:
            items.append(f"<li>{inner}</li>")
    if not items:
        return ""
    return f"<{lst.name}>{''.join(items)}</{lst.name}>"


def extract_table(table: Tag) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"], recursive=False):
            has_block = any(
                isinstance(c, Tag) and c.name in {"p", "ul", "ol", "table"}
                for c in cell.children
            )
            inner = extract_flow(cell) if has_block else extract_inline(cell)
            cells.append(f"<{cell.name}>{inner}</{cell.name}>")
        if cells:
            rows.append("<tr>" + "".join(cells) + "</tr>")
    if not rows:
        return ""
    return '<div class="table-wrap"><table>' + "".join(rows) + "</table></div>"


def extract_flow(el: Tag) -> str:
    blocks: list[str] = []
    inlines: list[str] = []

    def flush_inlines() -> None:
        text = " ".join(p for p in inlines if p).strip()
        inlines.clear()
        if text:
            blocks.append(text)

    for child in el.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            t = clean_text(str(child))
            if t:
                inlines.append(html.escape(t))
            continue
        if not isinstance(child, Tag):
            continue
        if child.name == "p":
            flush_inlines()
            inner = extract_inline(child)
            if inner:
                blocks.append(f"<p>{inner}</p>")
        elif child.name in {"ul", "ol"}:
            flush_inlines()
            lst = extract_list(child)
            if lst:
                blocks.append(lst)
        elif child.name == "blockquote":
            flush_inlines()
            inner = extract_flow(child)
            if inner:
                blocks.append(f"<blockquote>{inner}</blockquote>")
        elif child.name == "table":
            flush_inlines()
            blocks.append(extract_table(child))
        elif child.name == "img":
            flush_inlines()
            img_html = extract_img(child)
            if img_html:
                blocks.append(img_html)
        elif child.name == "iframe":
            continue
        elif child.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            continue
        elif child.name == "br":
            inlines.append("<br>")
        else:
            nested = extract_flow(child)
            if nested:
                if nested.startswith("<"):
                    flush_inlines()
                    blocks.append(nested)
                else:
                    inlines.append(nested)
    flush_inlines()
    return "\n".join(p for p in blocks if p)


def extract_file(path: Path) -> dict:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    to_drop = [el for el in soup.find_all(True) if should_decompose(el)]
    for el in to_drop:
        if el.parent is not None:
            el.decompose()

    title_el = soup.select_one(".page-title__header")
    title = clean_title(title_el.get_text(" ", strip=True)) if title_el else path.stem

    root = soup.select_one(".page-content-elements") or soup
    pieces: list[str] = []
    seen: set[str] = set()

    def add(chunk: str) -> None:
        chunk = chunk.strip()
        if not chunk or chunk in seen:
            return
        seen.add(chunk)
        pieces.append(chunk)

    for el in root.find_all(True):
        if el.parent is None:
            continue
        classes = class_str(el)
        if "ce-header__primary" in classes:
            text = clean_title(el.get_text(" ", strip=True))
            if not text or text == title:
                continue
            if text.lower().startswith(SKIP_HEADER_PREFIXES):
                continue
            add(f"<h3>{html.escape(text)}</h3>")
        elif "ce-gallery-text" in classes:
            add(extract_flow(el))
        elif el.name == "table" and "contenttable" in classes:
            add(extract_table(el))
        elif el.name == "img" and "responsive-image" in classes:
            add(extract_img(el))

    return {"title": title, "html": "\n\n".join(pieces), "file": path.name}


def chapter_sort_key(path: Path) -> tuple:
    m = re.match(r"^(\d+(?:\.\d+)*)", path.name)
    if not m:
        return (0, 0, 0, 0, path.name)
    parts = [int(part) for part in m.group(1).split(".")]
    while len(parts) < 4:
        parts.append(0)
    return tuple(parts[:4]) + (path.name,)


def extract_chapter(folder: Path) -> dict:
    files = sorted(folder.glob("*.html"), key=chapter_sort_key)
    sections = []
    for f in files:
        data = extract_file(f)
        if not data["html"].strip() and not data["title"]:
            continue
        sections.append(data)
    chapter_title = sections[0]["title"] if sections else folder.name
    parts = [f'<h2 id="s{i}">{html.escape(s["title"])}</h2>\n{s["html"]}' for i, s in enumerate(sections)]
    return {"title": chapter_title, "sections": sections, "html": "\n\n".join(parts)}
