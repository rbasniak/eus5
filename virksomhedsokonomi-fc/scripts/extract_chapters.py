"""Extract raw HTML for selected chapters, then build each chapter immediately."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RAW_DIR = ROOT / "raw"
PLAN_FILE = SCRIPTS / "plan.json"
PROFILE_DIR = SCRIPTS / ".browser-profile"
BOOK_URL = "https://virksomhed-fc-eudeux.systime.dk/?id=1"

CHAPTER_FOLDERS = {
    0: "Introduktion",
    1: "Kapitel 1",
    2: "Kapitel 2",
    3: "Kapitel 3",
    4: "Kapitel 4",
    5: "Kapitel 5",
    6: "Kapitel 6",
    7: "Kapitel 7",
}


def wait_for_login(page, wait_seconds: int) -> None:
    print(f"Opening {BOOK_URL} — log in if needed.")
    page.goto(BOOK_URL, wait_until="networkidle")
    try:
        input("Press Enter here when logged in and the book is visible...")
        return
    except EOFError:
        print(f"Waiting {wait_seconds}s for login in the browser...")
        time.sleep(wait_seconds)


def extract_page_content(page, url: str, retries: int = 5) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_selector(".page-content", timeout=30000, state="visible")
            page.wait_for_timeout(900)
            html = page.eval_on_selector(".page-content", "el => el.outerHTML")
            if not html:
                raise RuntimeError(f"No .page-content found at {url}")
            return html
        except Exception as error:
            last_error = error
            message = str(error).lower()
            if "interrupted" in message or "navigation" in message or "timeout" in message:
                wait = 1.5 * (attempt + 1)
                print(f"  retry {attempt + 1}/{retries} in {wait:.1f}s...")
                time.sleep(wait)
                continue
            raise
    if last_error is not None:
        raise last_error
    raise RuntimeError(f"Failed to extract {url}")


def extract_folders(page, plan: list[dict], folders: set[str]) -> list[str]:
    failures: list[str] = []
    selected = [entry for entry in plan if entry["chapter_folder"] in folders]
    print(f"Extracting {len(selected)} pages for: {', '.join(sorted(folders))}")

    for index, entry in enumerate(selected, start=1):
        folder = RAW_DIR / entry["chapter_folder"]
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / entry["filename"]
        if target.exists():
            print(f"[{index}/{len(selected)}] skip existing {entry['chapter_folder']}/{entry['filename']}")
            continue
        print(f"[{index}/{len(selected)}] {entry['chapter_folder']}/{entry['filename']}")
        try:
            content_html = extract_page_content(page, entry["url"])
            target.write_text(content_html, encoding="utf-8")
        except Exception as error:
            message = f"{entry['url']}: {error}"
            failures.append(message)
            print(f"  FAILED: {error}")

    return failures


def build_chapter(num: int) -> None:
    print(f"Building HTML for chapter {num}...")
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / "build_all.py"), "--only", str(num)],
        cwd=str(SCRIPTS),
        check=False,
    )
    if result.returncode != 0:
        print(f"Build for chapter {num} exited with code {result.returncode}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract and build selected chapters.")
    parser.add_argument(
        "--chapters",
        type=int,
        nargs="+",
        default=[1],
        help="Chapter numbers to extract and build (0=intro, 1-7). Default: 1",
    )
    parser.add_argument(
        "--login-wait",
        type=int,
        default=int(os.environ.get("LOGIN_WAIT", "60")),
        help="Seconds to wait for login when Enter is unavailable.",
    )
    parser.add_argument(
        "--extract-only",
        action="store_true",
        help="Extract raw HTML only; do not run build_all.py.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    if not PLAN_FILE.exists():
        print(f"Missing plan file: {PLAN_FILE}")
        return 1

    plan = json.loads(PLAN_FILE.read_text(encoding="utf-8"))
    chapter_nums = sorted(set(args.chapters))
    folders = {CHAPTER_FOLDERS[num] for num in chapter_nums if num in CHAPTER_FOLDERS}
    if not folders:
        print("No valid chapter folders selected.")
        return 1

    failures: list[str] = []
    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
        )
        page = context.pages[0] if context.pages else context.new_page()
        wait_for_login(page, args.login_wait)

        failures = extract_folders(page, plan, folders)
        context.close()

    if failures:
        print(f"{len(failures)} pages failed:")
        for failure in failures:
            print(f"  - {failure}")

    if args.extract_only:
        return 1 if failures else 0

    for num in chapter_nums:
        if num not in CHAPTER_FOLDERS:
            continue
        folder = RAW_DIR / CHAPTER_FOLDERS[num]
        if not folder.exists() or not any(folder.glob("*.html")):
            print(f"Skip build for chapter {num}: no raw files in {folder}")
            continue
        build_chapter(num)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
