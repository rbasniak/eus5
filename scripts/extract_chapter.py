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


def extract_img(img: Tag) -> str:
    src = (img.get("src") or "").strip()
    if not src:
        return ""
    alt = clean_text(img.get("alt") or img.get("title") or "")
    cap = f"<figcaption>{html.escape(alt)}</figcaption>" if alt else ""
    return f'<figure class="figure"><img src="{html.escape(src)}" alt="{html.escape(alt)}" loading="lazy">{cap}</figure>'


def extract_iframe(iframe: Tag) -> str:
    src = (iframe.get("src") or "").strip()
    if not src:
        return ""
    title = clean_text(iframe.get("title") or "Embedded content")
    return (
        f'<div class="embed"><iframe src="{html.escape(src)}" '
        f'title="{html.escape(title)}" loading="lazy" allowfullscreen></iframe></div>'
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
            elif href.startswith("http"):
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
        inner = extract_flow(li)
        if inner.strip():
            items.append(f"<li>{inner}</li>")
    if not items:
        return ""
    return f"<{lst.name}>{''.join(items)}</{lst.name}>"


def extract_table(table: Tag) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"], recursive=False):
            inner = extract_flow(cell)
            cells.append(f"<{cell.name}>{inner}</{cell.name}>")
        if cells:
            rows.append("<tr>" + "".join(cells) + "</tr>")
    if not rows:
        return ""
    return '<div class="table-wrap"><table>' + "".join(rows) + "</table></div>"


def extract_flow(el: Tag) -> str:
    parts: list[str] = []
    for child in el.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            t = clean_text(str(child))
            if t:
                parts.append(html.escape(t))
            continue
        if not isinstance(child, Tag):
            continue
        if child.name == "p":
            inner = extract_inline(child)
            if inner:
                parts.append(f"<p>{inner}</p>")
        elif child.name in {"ul", "ol"}:
            lst = extract_list(child)
            if lst:
                parts.append(lst)
        elif child.name == "blockquote":
            inner = extract_flow(child)
            if inner:
                parts.append(f"<blockquote>{inner}</blockquote>")
        elif child.name == "table":
            parts.append(extract_table(child))
        elif child.name == "img":
            parts.append(extract_img(child))
        elif child.name == "iframe":
            parts.append(extract_iframe(child))
        elif child.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            continue
        else:
            nested = extract_flow(child)
            if nested:
                parts.append(nested)
    return "\n".join(p for p in parts if p)


def extract_file(path: Path) -> dict:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    to_drop = [el for el in soup.find_all(True) if should_decompose(el)]
    for el in to_drop:
        if el.parent is not None:
            el.decompose()

    title_el = soup.select_one(".page-title__header")
    title = clean_text(title_el.get_text(" ", strip=True)) if title_el else path.stem

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
            text = clean_text(el.get_text(" ", strip=True))
            if text and text != title:
                add(f"<h3>{html.escape(text)}</h3>")
        elif "ce-gallery-text" in classes:
            add(extract_flow(el))
        elif el.name == "table" and "contenttable" in classes:
            add(extract_table(el))
        elif el.name == "img" and "responsive-image" in classes:
            add(extract_img(el))
        elif el.name == "iframe":
            add(extract_iframe(el))

    return {"title": title, "html": "\n\n".join(pieces), "file": path.name}


def main() -> None:
    src = Path(r"g:\Repositories\Pessoal\afsætning-f-c-til-eudeux\raw\Kapitel 1")
    files = sorted(src.glob("*.html"), key=lambda p: p.name)
    out_dir = Path(r"g:\Repositories\Pessoal\afsætning-f-c-til-eudeux\scripts\extracted")
    out_dir.mkdir(parents=True, exist_ok=True)

    combined = []
    for f in files:
        data = extract_file(f)
        slug = re.sub(r"[^\w.-]+", "_", data["file"])
        (out_dir / f"{slug}.html").write_text(
            f"<h2>{html.escape(data['title'])}</h2>\n{data['html']}",
            encoding="utf-8",
        )
        combined.append(
            f"<!-- {data['file']} -->\n<section>\n<h2>{html.escape(data['title'])}</h2>\n{data['html']}\n</section>"
        )
        print(f"{data['file']}: title={data['title']!r} chars={len(data['html'])}")

    (out_dir / "_combined.html").write_text("\n\n".join(combined), encoding="utf-8")
    print("Wrote", out_dir / "_combined.html")


if __name__ == "__main__":
    main()
