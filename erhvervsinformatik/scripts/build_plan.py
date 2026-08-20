"""Build the page extraction plan for erhvervsinformatik.systime.dk."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TOC_FILE = SCRIPTS / "toc.json"
PLAN_FILE = SCRIPTS / "plan.json"
BASE_URL = "https://erhvervsinformatik.systime.dk/?id="

INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\n\r\t]')
PADDING_DEPTH = {"16px": 0, "38px": 1, "60px": 2, "80px": 3}


def sanitize_filename(name: str) -> str:
    cleaned = INVALID_FILENAME_CHARS.sub("-", name).strip(" .")
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned or "untitled"


def chapter_folder_name(text: str) -> str:
    match = re.match(r"^(\d+)\.\s", text)
    if match:
        return f"Kapitel {match.group(1)}"
    return sanitize_filename(text)


def split_numbered_text(text: str) -> tuple[str, str] | None:
    match = re.match(r"^(\d+(?:\.\d+)+)\s+(.+)$", text)
    if match:
        return match.group(1), match.group(2)
    return None


def split_chapter_title(text: str) -> tuple[str, str] | None:
    match = re.match(r"^(\d+)\.\s+(.+)$", text)
    if match:
        return match.group(1), match.group(2)
    return None


class PlanBuilder:
    def __init__(self) -> None:
        self.chapter_folder: str | None = None
        self.chapter_num: str | None = None
        self.prefix_by_depth: dict[int, str] = {}
        self.next_suffix_by_parent: dict[str, int] = {}

    def reset_chapter(self, text: str) -> None:
        self.chapter_folder = chapter_folder_name(text)
        chapter_title = split_chapter_title(text)
        self.chapter_num = chapter_title[0] if chapter_title else None
        self.prefix_by_depth = {}
        self.next_suffix_by_parent = {}

    def trim_depths_below(self, depth: int) -> None:
        for level in list(self.prefix_by_depth):
            if level > depth:
                del self.prefix_by_depth[level]

    def register_numbered_prefix(self, prefix: str, depth: int) -> None:
        self.prefix_by_depth[depth] = prefix
        self.trim_depths_below(depth)

        parts = prefix.split(".")
        for index in range(1, len(parts)):
            parent = ".".join(parts[:index])
            current = int(parts[index])
            existing = self.next_suffix_by_parent.get(parent, 0)
            if current > existing:
                self.next_suffix_by_parent[parent] = current

    def next_unnumbered_prefix(self, depth: int) -> str:
        parent_prefix = self.prefix_by_depth.get(depth - 1)
        if parent_prefix is None:
            if self.chapter_num is not None:
                parent_prefix = self.chapter_num
            else:
                parent_prefix = "0"

        next_suffix = self.next_suffix_by_parent.get(parent_prefix, 0) + 1
        self.next_suffix_by_parent[parent_prefix] = next_suffix
        prefix = f"{parent_prefix}.{next_suffix}"
        self.prefix_by_depth[depth] = prefix
        self.trim_depths_below(depth)
        return prefix

    def filename_for(self, text: str, depth: int) -> str:
        numbered = split_numbered_text(text)
        if numbered is not None:
            prefix, title = numbered
            self.register_numbered_prefix(prefix, depth)
            return sanitize_filename(f"{prefix} {title}") + ".html"

        chapter_title = split_chapter_title(text)
        if chapter_title is not None and depth == 0:
            chapter_num, title = chapter_title
            prefix = f"{chapter_num}.0"
            self.register_numbered_prefix(prefix, 1)
            return sanitize_filename(f"{prefix} {title}") + ".html"

        if depth == 0 and self.chapter_num is None:
            return sanitize_filename(f"{text}.html")

        prefix = self.next_unnumbered_prefix(max(depth, 1))
        return sanitize_filename(f"{prefix} {text}") + ".html"


def build_page_plan(toc_items: list[dict]) -> list[dict]:
    plan: list[dict] = []
    builder = PlanBuilder()

    for item in toc_items:
        text = item["text"]
        page_id = item["id"]
        depth = PADDING_DEPTH.get(item["padding"], 1)

        if depth == 0:
            builder.reset_chapter(text)

        if builder.chapter_folder is None:
            continue

        filename = builder.filename_for(text, depth)
        plan.append(
            {
                "id": page_id,
                "text": text,
                "chapter_folder": builder.chapter_folder,
                "filename": filename,
                "url": f"{BASE_URL}{page_id}",
            }
        )

    return plan


def main() -> None:
    toc_items = json.loads(TOC_FILE.read_text(encoding="utf-8"))
    plan = build_page_plan(toc_items)
    PLAN_FILE.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built plan with {len(plan)} pages -> {PLAN_FILE}")


if __name__ == "__main__":
    main()
