"""Holt für jede Karte ohne Logo ein quadratisches Firmenlogo.

Reihenfolge: größtes apple-touch-icon / icon der Startseite, sonst Googles Favicon-Dienst.
Ergebnis: werkzeuge/assets/logos/<slug>.png|svg|ico. Vorhandene Dateien bleiben unangetastet,
ein schlechtes Logo also löschen oder von Hand ersetzen und neu laufen lassen.
"""
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIEL = ROOT / "werkzeuge" / "assets" / "logos"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari/605.1.15"}


def holen(url, limit=3_000_000):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read(limit), r.headers.get("Content-Type", "")


def endung(url, typ, daten):
    if "svg" in typ or url.lower().split("?")[0].endswith(".svg") or daten.lstrip()[:5] in (b"<svg ", b"<?xml"):
        return "svg"
    if daten[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if daten[:4] == b"\x00\x00\x01\x00":
        return "ico"
    if daten[:3] == b"\xff\xd8\xff":
        return "jpg"
    if daten[:4] == b"RIFF":
        return "webp"
    return None


def kandidaten(start):
    html, _ = holen(start)
    html = html.decode("utf-8", "ignore")
    funde = []
    for tag in re.findall(r"<link\b[^>]*>", html, re.I):
        rel = (re.search(r'rel=["\']([^"\']+)', tag, re.I) or [None, ""])[1].lower()
        href = re.search(r'href=["\']([^"\']+)', tag, re.I)
        if not href or "icon" not in rel or "mask" in rel:
            continue
        groesse = re.search(r'sizes=["\'](\d+)x', tag, re.I)
        g = int(groesse.group(1)) if groesse else (180 if "apple" in rel else 32)
        if href.group(1).lower().endswith(".svg"):
            g = 512
        funde.append((g, urllib.parse.urljoin(start, href.group(1))))
    funde.append((180, urllib.parse.urljoin(start, "/apple-touch-icon.png")))
    return [u for _, u in sorted(funde, reverse=True)]


def logo_fuer(slug, website):
    teile = urllib.parse.urlsplit(website)
    start = f"{teile.scheme}://{teile.netloc}/"
    versuche = []
    try:
        versuche += kandidaten(start)
    except Exception as e:  # Seite blockt Abrufe: dann nur Google
        print(f"  {slug}: Startseite nicht lesbar ({e.__class__.__name__})")
    versuche.append("https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL"
                    f"&url={urllib.parse.quote(start)}&size=256")
    for url in versuche:
        try:
            daten, typ = holen(url)
        except Exception:
            continue
        art = endung(url, typ, daten)
        if not art or len(daten) < 300:
            continue
        if art == "svg" and b"<script" in daten.lower():
            continue
        datei = ZIEL / f"{slug}.{art}"
        datei.write_bytes(daten)
        return datei, url
    return None, None


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    vorhanden = {p.stem for p in ZIEL.iterdir()}
    for karte in sorted((ROOT / "karten").glob("*.md")):
        kopf = karte.read_text().split("---")[1]
        slug = re.search(r'^slug:\s*"([^"]+)"', kopf, re.M).group(1)
        if slug in vorhanden:
            continue
        website = re.search(r'^website:\s*"([^"]+)"', kopf, re.M).group(1)
        datei, url = logo_fuer(slug, website)
        print(f"{slug}: {datei.name if datei else 'KEIN LOGO'}  {url or ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
