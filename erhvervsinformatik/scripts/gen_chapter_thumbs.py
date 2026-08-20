"""Generate thematic SVG thumbnails for erhvervsinformatik chapter cards."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "chapters"
OUT.mkdir(parents=True, exist_ok=True)

CX, CY = 160, 90

CHAPTERS = [
    (0, "Introduktion", "book"),
    (1, "Den digitale udvikling", "chip"),
    (2, "Sikkerhed og adfærd", "shield"),
    (3, "Digitale artefakter", "puzzle"),
    (4, "Designudvikling", "palette"),
    (5, "Programmering", "code"),
    (6, "Netværksarkitektur", "network"),
    (7, "Data", "chart"),
    (8, "Databaser", "database"),
    (9, "Projekter", "buildings"),
]

BG = "#eef2ff"
INK = "#1e3a8a"
ACCENT = "#2563eb"
SOFT = "#bfdbfe"
LINE = "#93c5fd"


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
    <line x1="-20" y1="-18" x2="-12" y2="-18" stroke="{INK}" stroke-width="2"/>
    <line x1="-20" y1="-6" x2="-12" y2="-6" stroke="{INK}" stroke-width="2"/>
    <line x1="4" y1="-18" x2="20" y2="-18" stroke="{SOFT}" stroke-width="2"/>
    <line x1="4" y1="-6" x2="20" y2="-6" stroke="{SOFT}" stroke-width="2"/>
"""


def icon_chip() -> str:
    return f"""
    <rect x="-36" y="-36" width="72" height="72" rx="8" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-18" y="-18" width="36" height="36" rx="4" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-36" y1="-18" x2="-48" y2="-18" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="-36" y1="0" x2="-48" y2="0" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="-36" y1="18" x2="-48" y2="18" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="36" y1="-18" x2="48" y2="-18" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="36" y1="0" x2="48" y2="0" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="36" y1="18" x2="48" y2="18" stroke="{ACCENT}" stroke-width="3"/>
"""


def icon_shield() -> str:
    return f"""
    <path d="M0-42 L34-28 V8 C34 28 0 44 0 44 S-34 28-34 8 V-28 Z" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M-10 4 L-2 14 L14-10" fill="none" stroke="{ACCENT}" stroke-width="4" stroke-linecap="round"/>
"""


def icon_puzzle() -> str:
    return f"""
    <path d="M-40-20 H-8 C-8-28 0-28 0-20 C0-12 8-12 8-20 H40 V20 H8 C8 28 0 28 0 20 C0 12-8 12-8 20 H-40 Z" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="-16" cy="0" r="6" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
    <circle cx="16" cy="-8" r="6" fill="{ACCENT}" opacity="0.5"/>
"""


def icon_palette() -> str:
    return f"""
    <ellipse cx="0" cy="4" rx="44" ry="36" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="-18" cy="-6" r="8" fill="{ACCENT}"/>
    <circle cx="4" cy="-14" r="8" fill="#f59e0b"/>
    <circle cx="22" cy="-2" r="8" fill="#10b981"/>
    <circle cx="8" cy="16" r="8" fill="#ef4444"/>
"""


def icon_code() -> str:
    return f"""
    <rect x="-48" y="-32" width="96" height="64" rx="8" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <polyline points="-24,0 -36,-12 -24,-24" fill="none" stroke="{ACCENT}" stroke-width="3"/>
    <polyline points="24,0 36,-12 24,-24" fill="none" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="-4" y1="18" x2="8" y2="-26" stroke="{INK}" stroke-width="3"/>
"""


def icon_network() -> str:
    return f"""
    <circle cx="0" cy="-24" r="10" fill="{ACCENT}"/>
    <circle cx="-32" cy="16" r="10" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="32" cy="16" r="10" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="0" y1="-14" x2="-26" y2="8" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="0" y1="-14" x2="26" y2="8" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-22" y1="16" x2="22" y2="16" stroke="{ACCENT}" stroke-width="2"/>
"""


def icon_chart() -> str:
    return f"""
    <rect x="-48" y="20" width="96" height="4" rx="2" fill="{LINE}"/>
    <rect x="-40" y="-8" width="16" height="28" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
    <rect x="-12" y="-24" width="16" height="44" rx="2" fill="{ACCENT}"/>
    <rect x="16" y="-16" width="16" height="36" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
"""


def icon_database() -> str:
    return f"""
    <ellipse cx="0" cy="-24" rx="36" ry="12" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M-36-24 V16 C-36 28 36 28 36 16 V-24" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <ellipse cx="0" cy="4" rx="36" ry="12" fill="none" stroke="{ACCENT}" stroke-width="2"/>
    <ellipse cx="0" cy="16" rx="36" ry="12" fill="none" stroke="{ACCENT}" stroke-width="2"/>
"""


def icon_buildings() -> str:
    return f"""
    <rect x="-56" y="-18" width="36" height="56" rx="2" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-12" y="-34" width="32" height="72" rx="2" fill="{ACCENT}" opacity="0.85"/>
    <rect x="28" y="2" width="28" height="40" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
"""


ICONS = {
    "book": icon_book,
    "chip": icon_chip,
    "shield": icon_shield,
    "puzzle": icon_puzzle,
    "palette": icon_palette,
    "code": icon_code,
    "network": icon_network,
    "chart": icon_chart,
    "database": icon_database,
    "buildings": icon_buildings,
}


def main() -> None:
    for num, _title, kind in CHAPTERS:
        path = OUT / f"ch{num:02d}.svg"
        path.write_text(svg_wrap(num, ICONS[kind]()), encoding="utf-8")
        print("Wrote", path.name)


if __name__ == "__main__":
    main()
