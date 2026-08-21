"""Annotate bilingual chapter HTML with curated subject vocabulary."""
from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag


KEY_TERMS_DIR = Path(__file__).resolve().parent / "key_terms"
SKIP_PARENTS = {"script", "style", "button", "a"}


def load_key_terms(chapter_num: int) -> list[dict]:
    path = KEY_TERMS_DIR / f"chapter-{chapter_num:02d}.json"
    if not path.exists():
        return []
    terms = json.loads(path.read_text(encoding="utf-8"))
    for term in terms:
        term.setdefault("da_forms", [term["da"]])
        term.setdefault("en_forms", [term["en"]])
    return terms


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def term_attributes(term: dict, visible_text: str, lang: str) -> dict:
    opposite = term["en"] if lang == "da" else term["da"]
    opposite_language = "English" if lang == "da" else "Danish"
    return {
        "class": "term vocab-term",
        "data-da": term["da"],
        "data-en": term["en"],
        "data-tts": term["da"],
        "tabindex": "0",
        "role": "button",
        "aria-expanded": "false",
        "aria-label": f"{visible_text}. {opposite_language}: {opposite}. Play Danish pronunciation",
    }


def term_by_surface(terms: list[dict], text: str, lang: str) -> dict | None:
    target = normalized(text)
    key = f"{lang}_forms"
    for term in terms:
        surfaces = [term[lang], *term.get(key, [])]
        if any(normalized(surface) == target for surface in surfaces):
            return term
    return None


def build_pattern(terms: list[dict], lang: str) -> tuple[re.Pattern | None, dict[str, dict]]:
    by_surface: dict[str, dict] = {}
    key = f"{lang}_forms"
    for term in terms:
        for surface in [term[lang], *term.get(key, [])]:
            clean = re.sub(r"\s+", " ", surface).strip()
            if clean:
                by_surface.setdefault(clean.casefold(), term)
    if not by_surface:
        return None, {}
    alternatives = sorted(by_surface, key=len, reverse=True)
    escaped = [re.escape(surface).replace(r"\ ", r"\s+") for surface in alternatives]
    pattern = re.compile(r"(?<![\wæøå])(" + "|".join(escaped) + r")(?![\wæøå])", re.IGNORECASE)
    return pattern, by_surface


def is_inside_term(node: NavigableString) -> bool:
    return any(
        isinstance(parent, Tag) and "term" in (parent.get("class") or [])
        for parent in node.parents
    )


def should_skip(node: NavigableString) -> bool:
    return any(
        isinstance(parent, Tag) and parent.name in SKIP_PARENTS
        for parent in node.parents
    )


def root_soup(node: NavigableString) -> BeautifulSoup:
    current = node
    while getattr(current, "parent", None) is not None:
        current = current.parent
    return current  # type: ignore[return-value]


def annotate_text_node(
    node: NavigableString,
    pattern: re.Pattern,
    by_surface: dict[str, dict],
    lang: str,
    occurrence_counts: dict[str, int],
) -> int:
    text = str(node)
    matches = list(pattern.finditer(text))
    if not matches:
        return 0
    soup = root_soup(node)
    replacements = []
    cursor = 0
    wrapped = 0
    for match in matches:
        if match.start() > cursor:
            replacements.append(NavigableString(text[cursor : match.start()]))
        visible = match.group(0)
        term = by_surface[normalized(visible)]
        term_id = term["da"]
        limit = term.get("max_occurrences")
        if limit is not None and occurrence_counts.get(term_id, 0) >= limit:
            replacements.append(NavigableString(visible))
            cursor = match.end()
            continue
        term_span = soup.new_tag("span", attrs=term_attributes(term, visible, lang))
        term_span.string = visible
        replacements.append(term_span)
        occurrence_counts[term_id] = occurrence_counts.get(term_id, 0) + 1
        wrapped += 1
        cursor = match.end()
    if cursor < len(text):
        replacements.append(NavigableString(text[cursor:]))
    for replacement in reversed(replacements):
        node.insert_after(replacement)
    node.extract()
    return wrapped


def enrich_existing_terms(article: Tag, terms: list[dict]) -> int:
    count = 0
    for term_span in article.select(".term"):
        if not isinstance(term_span, Tag):
            continue
        language_parent = term_span.find_parent(attrs={"lang": True})
        lang = language_parent.get("lang") if language_parent else "da"
        if lang not in {"da", "en"}:
            lang = "da"
        term = term_by_surface(terms, term_span.get_text(" ", strip=True), lang)
        if term is None:
            continue
        visible = term_span.get_text(" ", strip=True)
        term_span.attrs.update(term_attributes(term, visible, lang))
        count += 1
    return count


def annotate_language(article: Tag, terms: list[dict], lang: str) -> int:
    pattern, by_surface = build_pattern(terms, lang)
    if pattern is None:
        return 0
    count = 0
    occurrence_counts: dict[str, int] = {}
    containers = article.select(f'[lang="{lang}"]')
    for container in containers:
        if not isinstance(container, Tag):
            continue
        nodes = list(container.find_all(string=True))
        for node in nodes:
            if not isinstance(node, NavigableString):
                continue
            if not node.strip() or is_inside_term(node) or should_skip(node):
                continue
            count += annotate_text_node(node, pattern, by_surface, lang, occurrence_counts)
    return count


def annotate_key_terms(article: Tag, chapter_num: int) -> dict[str, int]:
    terms = load_key_terms(chapter_num)
    if not terms:
        return {"terms": 0, "existing": 0, "da": 0, "en": 0}
    existing = enrich_existing_terms(article, terms)
    da_count = annotate_language(article, terms, "da")
    en_count = annotate_language(article, terms, "en")
    return {
        "terms": len(terms),
        "existing": existing,
        "da": da_count,
        "en": en_count,
    }
