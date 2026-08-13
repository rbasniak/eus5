"""Re-translate bilingual spans where EN still equals DA."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_all import Translator, looks_danish, purge_failed_translations  # noqa: E402

MANUAL: dict[str, str] = {
    "7.1 Forbrugernes behov": "7.1 Consumer needs",
    "SNT-kunders behov": "SNT customers' needs",
    "Kulturbestemte behov": "Culturally determined needs",
    "Forbrugerens behov": "The consumer's needs",
    "Fysiske behov": "Physical needs",
    "Sociale behov": "Social needs",
    "Logo Søstrene Grene": "Søstrene Grene logo",
    "Logo Søstene Grene": "Søstrene Grene logo",
    "Søvn": "Sleep",
    "Brød": "Bread",
    "Kød": "Meat",
    "Mejeriprodukter": "Dairy products",
    "3. SWOT-opsamling": "3. SWOT summary",
    "SWOT-opsamling": "SWOT summary",
    "SWOT-opsamlingen": "The SWOT summary",
    "Kundepolitik": "Customer policy",
    "Proces": "Process",
    "Kilder": "Sources",
    "Styrker": "Strengths",
    "Svagheder": "Weaknesses",
    "Muligheder": "Opportunities",
    "Trusler": "Threats",
    "fornuftige priser": "reasonable prices",
    "Hvad vi spiser?": "What do we eat?",
    "Hvor ofte vi spiser?": "How often do we eat?",
    "Hvordan vi spiser?": "How do we eat?",
    "Hvor meget vi spiser?": "How much do we eat?",
    "8.1 Konkurrencesituationen": "8.1 The competitive situation",
    "Konkurrencesituation": "Competitive situation",
    "Konkurrenceforhold": "Competitive conditions",
    "Konkurrence": "Competition",
    "Baggrund": "Background",
    "Branchen": "The industry",
    "Kommunikation": "Communication",
    "Levering": "Delivery",
    "Sikkerhed": "Security",
    "Reklamer": "Advertisements",
    "Behandling af reklamationer": "Handling of complaints",
    "Informative reklamer": "Informative advertisements",
    "Manipulative reklamer": "Manipulative advertisements",
    "Manipulative eller informative reklamer": "Manipulative or informative advertisements",
    "Offline betjeningsformer": "Offline service formats",
    "Eksempel: Produkterne hos Boozt.com": "Example: Products at Boozt.com",
    "Kilder: Boozt.com": "Sources: Boozt.com",
    "Kilder: JYSK": "Sources: JYSK",
    "Kilder: Joe & the Juice": "Sources: Joe & the Juice",
    "Kilder: Too Good To Go": "Sources: Too Good To Go",
    "Fakta: JOE AND THE JUICE": "Facts: JOE AND THE JUICE",
}

HOSTS = {
    "p", "h1", "h2", "h3", "h4", "li", "td", "th", "figcaption",
    "a", "blockquote", "summary",
}

SKIP_SAME = re.compile(
    r"^(?:"
    r"\d+(?:\.\d+)?\s*(?:AI|Promotion|Channel marketing)?"
    r"|Vision"
    r"|Promotion|Online promotion|Offline promotion|Sales Promotion|Distribution|Segment|Brand|Marketing|CSR|Apps|Niche|SMOK"
    r"|Airbnb|The Sims|Endomondo|Wikipedia|Blogger\.com|Amazon|Zalando|Pandora"
    r"|Boozt\.com|IKEA|Airtox|Too Good To Go|JOE & THE JUICE|REMA 1000"
    r"|Airtox B2B|JYSK B2B|Lakrids by Bülow B2B|ed A/S|JYSK B2C"
    r"|Elgiganten|Magasin du Nord|Bilka|GreenMind|Create2STAY|RE-ZIP|ReCollector"
    r"|Shaping New Tomorrow|Coolshop \(webshop\)|Ditur logo|150 brands"
    r"|[A-Za-z0-9\-]+\.(?:dk|com|org)$"
    r")$",
    re.I,
)

DANISH_QUESTION = re.compile(
    r"^(?:Hvad|Hvor|Hvordan|Hvilke|Hvilken|Skal|MFL)\b",
    re.I,
)

DANISH_PREFIX = re.compile(
    r"^(?:Eksempel|Eksempler|Kilder|Fakta|Videoer|AI-interaktivitet)\b",
    re.I,
)

ENGLISH_CITATION = re.compile(
    r"^(?:Søstrene Grene|IKEA|JYSK|Boozt|Joe).*(?:Retail|Retailing|Internet|\d{2}\.\d{2}\.\d{2})",
    re.I,
)

DANISH_STEM = re.compile(
    r"(?:virksomhed|forretnings|kapitel|opgave|marked|produkt|sortiment|pris|placering|"
    r"organisation|forbrug|elever|lærer|interne|eksterne|anvendelse|geografi|konsument|"
    r"producent|begreb|værktøj|gruppe|læring|teori|praktisk|swot|idé|værdier|profil|"
    r"styrke|svaghed|mulighed|trussel|kunde|konkurrent|markedsføring|distribution|"
    r"promotion|segment|målgruppe|købsadfærd|kundeservice|indhold|opgaver|case|"
    r"diskut|beskriv|forklar|gennemfør|inspiration|afslutning|walk and talk|"
    r"mejeri|brød|kød|søvn|tekstil|kvalitet|spare|nemt|bekvemt|rejser|services|varer|"
    r"baggrund|reklam|betjening|kommunikation|konkurrence|levering|sikkerhed|branchen|"
    r"kilder|fakta|eksempel|informativ|manipulativ|offline|indsamler|udvikler|anvender|"
    r"behandling|mersalg|finansieres|hukommelse|spiser|reklamation|konkurrencesituation)",
    re.I,
)


def en_sibling(da_span):
    sib = da_span.find_next_sibling("span")
    if sib is not None and sib.get("lang") == "en":
        return sib
    return None


def needs_translation(text: str) -> bool:
    if text in MANUAL:
        return True
    if len(text) <= 3:
        return False
    if ENGLISH_CITATION.match(text):
        return False
    if SKIP_SAME.match(text):
        return False
    if DANISH_QUESTION.match(text):
        return True
    if DANISH_PREFIX.match(text):
        return True
    if looks_danish(text):
        return True
    if DANISH_STEM.search(text):
        return True
    return False


def collect_pairs(soup: BeautifulSoup) -> list[tuple]:
    fixes = []
    seen = set()
    for host in soup.find_all(HOSTS):
        spans = host.find_all("span", attrs={"lang": True}, recursive=False)
        if len(spans) < 2:
            continue
        if spans[0].get("lang") != "da" or spans[1].get("lang") != "en":
            continue
        da_t = spans[0].get_text(" ", strip=True)
        en_t = spans[1].get_text(" ", strip=True)
        if not da_t or da_t != en_t:
            continue
        if not needs_translation(da_t):
            continue
        key = da_t
        if key in seen:
            continue
        seen.add(key)
        fixes.append((spans[0], spans[1], da_t))
    return fixes


def apply_fixes(soup: BeautifulSoup, tr: Translator, translations: dict[str, str]) -> int:
    changed = 0
    for host in soup.find_all(HOSTS):
        spans = host.find_all("span", attrs={"lang": True}, recursive=False)
        if len(spans) < 2:
            continue
        if spans[0].get("lang") != "da" or spans[1].get("lang") != "en":
            continue
        da_t = spans[0].get_text(" ", strip=True)
        en_t = spans[1].get_text(" ", strip=True)
        if not da_t or da_t != en_t:
            continue
        new_en = translations.get(da_t)
        if not new_en or new_en == da_t:
            continue
        en_span = spans[1]
        en_span.clear()
        en_span.append(new_en)
        changed += 1
    return changed


def purge_identity_cache(tr: Translator) -> int:
    remove = []
    for k, v in tr.cache.items():
        if k != v:
            continue
        if k in MANUAL or len(k) <= 3:
            if k not in MANUAL:
                continue
        if SKIP_SAME.match(k):
            continue
        if needs_translation(k):
            remove.append(k)
    for k in remove:
        del tr.cache[k]
    return len(remove)


def main() -> None:
    tr = Translator()
    removed = purge_failed_translations(tr.cache) + purge_identity_cache(tr)
    tr.save()
    print(f"Purged {removed} cache entries", flush=True)

    all_pairs: dict[str, list] = {}
    for path in sorted(ROOT.glob("kapitel*.html")):
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        for item in collect_pairs(soup):
            all_pairs.setdefault(item[2], []).append((path, item))

    texts = sorted(all_pairs)
    print(f"Unique untranslated strings: {len(texts)}", flush=True)
    if not texts:
        print("Nothing to fix.", flush=True)
        return

    for t in texts:
        tr.cache.pop(t, None)
    tr.translate_many(texts)
    translations = {t: MANUAL.get(t) or tr.translate(t) for t in texts}

    total = 0
    touched = set()
    for path in sorted(ROOT.glob("kapitel*.html")):
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        changed = apply_fixes(soup, tr, translations)
        if changed:
            path.write_text(soup.decode(formatter="html"), encoding="utf-8")
            print(f"{path.name}: fixed {changed}", flush=True)
            total += changed
            touched.add(path.name)

    tr.save()
    print(f"Done. Fixed {total} spans in {len(touched)} files.", flush=True)


if __name__ == "__main__":
    main()
