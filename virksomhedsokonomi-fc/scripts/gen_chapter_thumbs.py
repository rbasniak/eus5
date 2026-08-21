"""Generate thematic SVG thumbnails for virksomhedsøkonomi chapter cards."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "chapters"
OUT.mkdir(parents=True, exist_ok=True)

CX, CY = 160, 90
BG = "#ecfdf5"
INK = "#065f46"
ACCENT = "#059669"
SOFT = "#a7f3d0"
LINE = "#6ee7b7"

CHAPTERS = [
    (0, "Introduktion", "book"),
    (1, "Virksomheden", "building"),
    (2, "Regnskab", "ledger"),
    (3, "Budget", "chart"),
    (4, "Omkostninger", "coins"),
    (5, "Logistik", "truck"),
    (6, "Økonomisystem", "system"),
    (7, "Økonomisk effektivitet", "gauge"),
]


def svg_wrap(num: int, inner: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img" aria-hidden="true">
  <defs>
    <linearGradient id="g{num}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
  </defs>
  <rect width="320" height="180" fill="url(#g{num})"/>
  <g transform="translate({CX},{CY})">
{inner}
  </g>
</svg>
"""


def icon_book() -> str:
    return f"""
    <rect x="-28" y="-34" width="56" height="72" rx="4" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-8" y1="-34" x2="-8" y2="38" stroke="{ACCENT}" stroke-width="2"/>
"""


def icon_building() -> str:
    return f"""
    <rect x="-40" y="-10" width="34" height="50" rx="2" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-2" y="-28" width="42" height="68" rx="2" fill="{ACCENT}" opacity="0.85"/>
    <rect x="44" y="0" width="28" height="40" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
"""


def icon_ledger() -> str:
    return f"""
    <rect x="-44" y="-34" width="88" height="68" rx="6" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-28" y1="-14" x2="28" y2="-14" stroke="{LINE}" stroke-width="2"/>
    <line x1="-28" y1="2" x2="28" y2="2" stroke="{LINE}" stroke-width="2"/>
    <line x1="-28" y1="18" x2="28" y2="18" stroke="{LINE}" stroke-width="2"/>
    <text x="-18" y="16" font-size="10" fill="{ACCENT}">D</text>
    <text x="10" y="16" font-size="10" fill="{ACCENT}">K</text>
"""


def icon_chart() -> str:
    return f"""
    <rect x="-48" y="20" width="96" height="4" rx="2" fill="{LINE}"/>
    <rect x="-40" y="-8" width="16" height="28" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
    <rect x="-12" y="-24" width="16" height="44" rx="2" fill="{ACCENT}"/>
    <rect x="16" y="-16" width="16" height="36" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
"""


def icon_coins() -> str:
    return f"""
    <ellipse cx="-16" cy="8" rx="22" ry="10" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <ellipse cx="16" cy="-8" rx="22" ry="10" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <ellipse cx="0" cy="16" rx="22" ry="10" fill="{ACCENT}" opacity="0.75"/>
"""


def icon_truck() -> str:
    return f"""
    <rect x="-46" y="-8" width="58" height="28" rx="4" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="12" y="-18" width="28" height="38" rx="4" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="-24" cy="24" r="8" fill="{INK}"/>
    <circle cx="24" cy="24" r="8" fill="{INK}"/>
"""


def icon_system() -> str:
    return f"""
    <rect x="-48" y="-28" width="96" height="56" rx="8" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="-20" cy="-4" r="8" fill="{ACCENT}"/>
    <circle cx="16" cy="-12" r="8" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
    <circle cx="16" cy="12" r="8" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
    <line x1="-12" y1="-4" x2="8" y2="-12" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-12" y1="-4" x2="8" y2="12" stroke="{ACCENT}" stroke-width="2"/>
"""


def icon_gauge() -> str:
    return f"""
    <circle cx="0" cy="0" r="40" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M0 0 L28 -18" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="0" cy="0" r="4" fill="{ACCENT}"/>
    <path d="M-28 18 A32 32 0 0 1 28 18" fill="none" stroke="{SOFT}" stroke-width="6"/>
"""


ICONS = {
    "book": icon_book,
    "building": icon_building,
    "ledger": icon_ledger,
    "chart": icon_chart,
    "coins": icon_coins,
    "truck": icon_truck,
    "system": icon_system,
    "gauge": icon_gauge,
}


def main() -> None:
    for num, _title, kind in CHAPTERS:
        path = OUT / f"ch{num:02d}.svg"
        path.write_text(svg_wrap(num, ICONS[kind]()), encoding="utf-8")
        print("Wrote", path.name)


if __name__ == "__main__":
    main()
