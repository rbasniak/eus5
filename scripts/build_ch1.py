"""Build the bilingual chapter 1 HTML page."""
from pathlib import Path

from ch1_content import body
from html_i18n import t

ROOT = Path(r"g:\Repositories\Pessoal\afsætning-f-c-til-eudeux")
OUT = ROOT / "kapitel-01.html"

TOC = [
    ("s10", "1. Forretningsmodeller", "1. Business models"),
    ("s11", "1.1 En forretningsmodel", "1.1 A business model"),
    ("s12", "1.2 Traditionelle modeller", "1.2 Traditional models"),
    ("s13", "1.3 Digitale modeller", "1.3 Digital models"),
    ("s14", "1.4 Kombination", "1.4 Combining models"),
    ("s15", "1.5 Bæredygtighed", "1.5 Sustainability"),
    ("s16", "1.6 AI", "1.6 AI"),
    ("s17", "1.7 Opgaver", "1.7 Exercises"),
    ("s18", "1.8 Begrebstræning", "1.8 Term practice"),
]


def toc_html() -> str:
    links = "\n".join(f'<a href="#{anchor}">{t(da, en)}</a>' for anchor, da, en in TOC)
    return f"""<details class="toc">
  <summary>{t("Indhold", "Contents")}</summary>
  <nav>{links}</nav>
</details>"""


def page() -> str:
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>1. Forretningsmodeller – Afsætning F-C</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="lang-bar">
    <div class="lang-bar-inner">
      <div class="brand">Afsætning F–C · {t("Kapitel 1", "Chapter 1")}</div>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-set-lang="da" aria-pressed="true">DA</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </header>
  <div class="wrap">
    {toc_html()}
    <main class="article">
      <p class="kicker">Afsætning F–C til EUD/EUX</p>
      <h1 id="s10">{t("1. Forretningsmodeller", "1. Business models")}</h1>
      {body()}
    </main>
  </div>
  <script src="assets/i18n.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    OUT.write_text(page(), encoding="utf-8")
    print("Wrote", OUT, "chars=", OUT.stat().st_size)
