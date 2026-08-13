"""Generate thematic SVG thumbnails for chapter cards."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "chapters"
OUT.mkdir(parents=True, exist_ok=True)

CX, CY = 160, 90  # icon center in 320×180 viewBox

CHAPTERS = [
    (1, "Forretningsmodeller", "blocks"),
    (2, "Forretningskonceptet", "lightbulb"),
    (3, "SWOT", "matrix"),
    (4, "Markeder", "globe"),
    (5, "Lovgivning", "scales"),
    (6, "Segmentering", "pie"),
    (7, "Købsadfærd", "cart"),
    (8, "Konkurrence", "race"),
    (9, "Produkt", "box"),
    (10, "Placering", "pin"),
    (11, "Pris", "tag"),
    (12, "Promotion", "megaphone"),
    (13, "Kundeservice", "headset"),
    (14, "Cases", "buildings"),
]

BG = "#e8f5f2"
INK = "#134e4a"
ACCENT = "#0f766e"
SOFT = "#99f6e4"
LINE = "#5eead4"


def svg_wrap(num: int, inner: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img" aria-hidden="true">
  <defs>
    <linearGradient id="g{num}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="#f6f1e8"/>
    </linearGradient>
  </defs>
  <rect width="320" height="180" fill="url(#g{num})"/>
  <g transform="translate({CX},{CY})">
{inner}
  </g>
</svg>
"""


def icon_blocks() -> str:
    return f"""
    <rect x="-36" y="-28" width="44" height="44" rx="6" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="12" y="-12" width="44" height="44" rx="6" fill="{ACCENT}" opacity="0.85"/>
    <rect x="-20" y="20" width="44" height="44" rx="6" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-14" y1="-6" x2="2" y2="-6" stroke="{INK}" stroke-width="2"/>
    <line x1="-14" y1="2" x2="-4" y2="2" stroke="{INK}" stroke-width="2"/>
"""


def icon_lightbulb() -> str:
    return f"""
    <circle cx="0" cy="0" r="28" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M0-28c-12 0-20 8-20 20 0 8 4 14 8 18v6h24v-6c4-4 8-10 8-18 0-12-8-20-20-20z" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-12" y="18" width="24" height="8" rx="2" fill="{ACCENT}"/>
    <line x1="-8" y1="-34" x2="-8" y2="-42" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="8" y1="-34" x2="8" y2="-42" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="20" y1="-26" x2="28" y2="-30" stroke="{ACCENT}" stroke-width="2"/>
"""


def icon_matrix() -> str:
    return f"""
    <rect x="-56" y="-46" width="112" height="96" rx="8" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="0" y1="-46" x2="0" y2="50" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="-56" y1="2" x2="56" y2="2" stroke="{ACCENT}" stroke-width="2"/>
    <text x="-42" y="-12" fill="{INK}" font-size="14" font-weight="700">S</text>
    <text x="14" y="-12" fill="{INK}" font-size="14" font-weight="700">W</text>
    <text x="-42" y="34" fill="{INK}" font-size="14" font-weight="700">O</text>
    <text x="14" y="34" fill="{INK}" font-size="14" font-weight="700">T</text>
"""


def icon_globe() -> str:
    return f"""
    <circle cx="0" cy="0" r="40" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <ellipse cx="0" cy="0" rx="40" ry="14" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>
    <ellipse cx="0" cy="0" rx="14" ry="40" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>
    <line x1="-40" y1="0" x2="40" y2="0" stroke="{ACCENT}" stroke-width="1.5"/>
"""


def icon_scales() -> str:
    return f"""
    <line x1="0" y1="-38" x2="0" y2="30" stroke="{ACCENT}" stroke-width="3"/>
    <line x1="-32" y1="-26" x2="32" y2="-26" stroke="{ACCENT}" stroke-width="3"/>
    <path d="M-32-26 L-48 6 L-16 6 Z" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M32-26 L16 6 L48 6 Z" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-8" y="30" width="16" height="8" rx="2" fill="{ACCENT}"/>
"""


def icon_pie() -> str:
    return f"""
    <circle cx="0" cy="0" r="36" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M0 0 L0-36 A36 36 0 0 1 32 18 Z" fill="{ACCENT}"/>
    <path d="M0 0 L32 18 A36 36 0 0 1-32 18 Z" fill="{SOFT}"/>
    <path d="M0 0 L-32 18 A36 36 0 0 1 0-36 Z" fill="{LINE}"/>
"""


def icon_cart() -> str:
    return f"""
    <path d="M-54-18h16l12 48h72l8-36H-30" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linejoin="round"/>
    <circle cx="-14" cy="42" r="6" fill="{ACCENT}"/>
    <circle cx="26" cy="42" r="6" fill="{ACCENT}"/>
    <rect x="-10" y="-6" width="20" height="14" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
"""


def icon_race() -> str:
    return f"""
    <rect x="-52" y="18" width="100" height="8" rx="4" fill="{LINE}"/>
    <rect x="-44" y="-2" width="28" height="16" rx="4" fill="{ACCENT}"/>
    <rect x="-8" y="-14" width="28" height="16" rx="4" fill="{SOFT}" stroke="{ACCENT}" stroke-width="1.5"/>
    <rect x="28" y="-26" width="28" height="16" rx="4" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <polygon points="44,-18 56,-18 50,-26" fill="{ACCENT}"/>
"""


def icon_box() -> str:
    return f"""
    <path d="M-32-18 L0-34 L32-18 L32 30 L-32 30 Z" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M-32-18 L0-2 L32-18" fill="none" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="0" y1="-2" x2="0" y2="30" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-20" y="6" width="40" height="4" rx="1" fill="{ACCENT}" opacity="0.6"/>
"""


def icon_pin() -> str:
    return f"""
    <path d="M0-38c-16 0-28 12-28 28 0 20 28 48 28 48s28-28 28-48c0-16-12-28-28-28z" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="0" cy="-10" r="10" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M-52 38h104" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6 4"/>
"""


def icon_tag() -> str:
    return f"""
    <path d="M-52-26h40l52 52-28 28-52-52V-26z" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <circle cx="-36" cy="-10" r="6" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <text x="-12" y="18" fill="{INK}" font-size="18" font-weight="700">kr</text>
"""


def icon_megaphone() -> str:
    return f"""
    <path d="M-60-2h32l48-16v72l-48-16h-32V-2z" fill="{ACCENT}"/>
    <path d="M-60 6c-12 4-12 28 0 32" fill="none" stroke="{ACCENT}" stroke-width="3"/>
    <path d="M20-18c8 8 8 52 0 60" fill="none" stroke="{SOFT}" stroke-width="3"/>
    <rect x="-68" y="-6" width="12" height="40" rx="3" fill="{INK}"/>
"""


def icon_headset() -> str:
    return f"""
    <path d="M-32-18c0-16 12-28 24-28s24 12 24 28" fill="none" stroke="{ACCENT}" stroke-width="3"/>
    <rect x="-44" y="-18" width="16" height="32" rx="8" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="28" y="-18" width="16" height="32" rx="8" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
    <path d="M-28 14h40v8c0 8-8 16-20 16s-20-8-20-16v-8z" fill="{ACCENT}"/>
"""


def icon_buildings() -> str:
    return f"""
    <rect x="-56" y="-18" width="36" height="56" rx="2" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>
    <rect x="-44" y="-6" width="8" height="8" fill="{SOFT}"/>
    <rect x="-44" y="8" width="8" height="8" fill="{SOFT}"/>
    <rect x="-12" y="-34" width="32" height="72" rx="2" fill="{ACCENT}" opacity="0.85"/>
    <rect x="-2" y="-22" width="8" height="8" fill="#fff" opacity="0.7"/>
    <rect x="-2" y="-6" width="8" height="8" fill="#fff" opacity="0.7"/>
    <rect x="28" y="2" width="28" height="40" rx="2" fill="{SOFT}" stroke="{ACCENT}" stroke-width="2"/>
"""


ICONS = {
    "blocks": icon_blocks,
    "lightbulb": icon_lightbulb,
    "matrix": icon_matrix,
    "globe": icon_globe,
    "scales": icon_scales,
    "pie": icon_pie,
    "cart": icon_cart,
    "race": icon_race,
    "box": icon_box,
    "pin": icon_pin,
    "tag": icon_tag,
    "megaphone": icon_megaphone,
    "headset": icon_headset,
    "buildings": icon_buildings,
}


def main() -> None:
    for num, _title, kind in CHAPTERS:
        path = OUT / f"ch{num:02d}.svg"
        path.write_text(svg_wrap(num, ICONS[kind]()), encoding="utf-8")
        print("Wrote", path.name)


if __name__ == "__main__":
    main()
