"""Extract raw page-content HTML from virksomhed-fc-eudeux.systime.dk."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RAW_DIR = ROOT / "raw"
PLAN_FILE = SCRIPTS / "plan.json"
BOOK_URL = "https://virksomhed-fc-eudeux.systime.dk/?id=1"

BUILD_CHAPTERS = {
    "Introduktion": 0,
    "Kapitel 1": 1,
    "Kapitel 2": 2,
    "Kapitel 3": 3,
    "Kapitel 4": 4,
    "Kapitel 5": 5,
    "Kapitel 6": 6,
    "Kapitel 7": 7,
}


def expand_all_toc(page) -> list[dict]:
    page.goto(BOOK_URL, wait_until="networkidle")
    page.wait_for_selector(".page-content", timeout=30000)

    page.evaluate(
        """
        async () => {
            for (let round = 0; round < 20; round++) {
                const toggles = [...document.querySelectorAll(
                    '.toc-link__toggle[aria-pressed="false"], .toc-link__toggle[aria-expanded="false"]'
                )];
                if (toggles.length === 0) {
                    break;
                }
                for (const toggle of toggles) {
                    toggle.click();
                    await new Promise((resolve) => setTimeout(resolve, 120));
                }
                await new Promise((resolve) => setTimeout(resolve, 400));
            }
        }
        """
    )

    return page.evaluate(
        """
        () => {
            return [...document.querySelectorAll('li.accordion.toc-link')].map((li) => {
                const link = li.querySelector('a.toc-link__trigger');
                const content = li.querySelector('.toc-link__content');
                const padding = content ? getComputedStyle(content).paddingLeft : '0px';
                return {
                    id: new URL(link.href).searchParams.get('id'),
                    text: (link.getAttribute('aria-label') || link.textContent).trim(),
                    padding,
                };
            });
        }
        """
    )


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


def wait_for_login(page) -> None:
    print("Opening the book. Log in in the browser window if needed, then press Enter here...")
    page.goto(BOOK_URL, wait_until="networkidle")
    try:
        input()
        return
    except EOFError:
        wait_seconds = int(os.environ.get("LOGIN_WAIT", "300"))
        print(f"Press Enter unavailable — waiting {wait_seconds}s for login in the browser...")
        time.sleep(wait_seconds)


def announce_chapter_complete(folder_name: str) -> None:
    if folder_name not in BUILD_CHAPTERS:
        return
    num = BUILD_CHAPTERS[folder_name]
    print("")
    print("=" * 60)
    print(f"CHAPTER COMPLETE: {folder_name} (build with --only {num})")
    print(f"  python build_all.py --only {num}")
    print("=" * 60)
    print("")


def main() -> int:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    retry_missing = "--retry-missing" in sys.argv

    if not PLAN_FILE.exists():
        print(f"Missing plan file: {PLAN_FILE}")
        print("Run build_plan.py first (or extract toc.json and rebuild the plan).")
        return 1

    plan = json.loads(PLAN_FILE.read_text(encoding="utf-8"))

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        wait_for_login(page)

        print(f"Extracting {len(plan)} pages to {RAW_DIR}")

        failures: list[str] = []
        current_folder: str | None = None
        for index, entry in enumerate(plan, start=1):
            if current_folder is not None and entry["chapter_folder"] != current_folder:
                announce_chapter_complete(current_folder)
            current_folder = entry["chapter_folder"]

            folder = RAW_DIR / entry["chapter_folder"]
            folder.mkdir(parents=True, exist_ok=True)
            target = folder / entry["filename"]

            if target.exists() and not retry_missing:
                print(f"[{index}/{len(plan)}] skip existing {entry['chapter_folder']}/{entry['filename']}")
                continue

            print(f"[{index}/{len(plan)}] {entry['chapter_folder']}/{entry['filename']}")

            try:
                content_html = extract_page_content(page, entry["url"])
                target.write_text(content_html, encoding="utf-8")
            except Exception as error:
                message = f"{entry['url']}: {error}"
                failures.append(message)
                print(f"  FAILED: {error}")

        if current_folder is not None:
            announce_chapter_complete(current_folder)

        browser.close()

    print(f"\nDone. Raw files saved under: {RAW_DIR}")
    if failures:
        print(f"{len(failures)} pages failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
