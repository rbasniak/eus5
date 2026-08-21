"""Fetch table of contents from virksomhed-fc-eudeux.systime.dk."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TOC_FILE = SCRIPTS / "toc.json"
BOOK_URL = "https://virksomhed-fc-eudeux.systime.dk/?id=1"


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


def main() -> int:
    SCRIPTS.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        toc = expand_all_toc(page)
        browser.close()

    TOC_FILE.write_text(json.dumps(toc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Fetched {len(toc)} TOC entries -> {TOC_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
