"""Extract raw page-content HTML from erhvervsinformatik.systime.dk."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RAW_DIR = ROOT / "raw"
PLAN_FILE = SCRIPTS / "plan.json"
BOOK_URL = "https://erhvervsinformatik.systime.dk/?id=485"


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


def extract_page_content(page, url: str) -> str:
    page.goto(url, wait_until="networkidle")
    page.wait_for_selector(".page-content", timeout=30000)
    time.sleep(0.5)
    html = page.eval_on_selector(".page-content", "el => el.outerHTML")
    if not html:
        raise RuntimeError(f"No .page-content found at {url}")
    return html


def main() -> int:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if not PLAN_FILE.exists():
        print(f"Missing plan file: {PLAN_FILE}")
        print("Run build_plan.py first (or extract toc.json and rebuild the plan).")
        return 1

    plan = json.loads(PLAN_FILE.read_text(encoding="utf-8"))

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Opening the book. Log in in the browser window if needed, then press Enter here...")
        page.goto(BOOK_URL, wait_until="networkidle")
        input()

        print(f"Extracting {len(plan)} pages to {RAW_DIR}")

        failures: list[str] = []
        for index, entry in enumerate(plan, start=1):
            folder = RAW_DIR / entry["chapter_folder"]
            folder.mkdir(parents=True, exist_ok=True)
            target = folder / entry["filename"]

            print(f"[{index}/{len(plan)}] {entry['chapter_folder']}/{entry['filename']}")

            try:
                content_html = extract_page_content(page, entry["url"])
                target.write_text(content_html, encoding="utf-8")
            except Exception as error:
                message = f"{entry['url']}: {error}"
                failures.append(message)
                print(f"  FAILED: {error}")

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
