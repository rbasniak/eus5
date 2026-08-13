"""Remove failed Danish->Danish entries from the translation cache."""
from __future__ import annotations

import json
import re
from pathlib import Path

CACHE = Path(__file__).resolve().parents[1] / "scripts" / "cache" / "i18n.json"

DANISH_HINT = re.compile(
    r"[æøåÆØÅ]|\b(og|er|det|til|med|for|som|virksomhed|kapitel|elever|markedsføring|opgaver|afsnit|kunderne|produkt|lærer|eleven)\b",
    re.IGNORECASE,
)


def looks_danish(text: str) -> bool:
    return bool(DANISH_HINT.search(text))


def main() -> None:
    cache: dict[str, str] = json.loads(CACHE.read_text(encoding="utf-8"))
    remove = [k for k, v in cache.items() if k == v and len(k) > 8 and looks_danish(k)]
    for k in remove:
        del cache[k]
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"Removed {len(remove)} entries; {len(cache)} remain")


if __name__ == "__main__":
    main()
