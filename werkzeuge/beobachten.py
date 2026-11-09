"""Findet ohne KI heraus, bei welchen Anbietern sich öffentliche Seiten seit dem letzten Lauf geändert haben.

Aufruf: python3 werkzeuge/beobachten.py
Liest je Karte die Direktlinks (Preise, Release Notes, Trust Center), die Website und bis zu zwei weitere
Quellen auf der Domain des Anbieters, holt den Seitentext und vergleicht ihn mit dem Stand vom letzten Lauf.
Ergebnis: werkzeuge/_beobachtung/bericht.md mit den geänderten Anbietern und den neuen bzw. weggefallenen Sätzen.
Der Wochenlauf schaut nur bei diesen Anbietern genauer hin. Der erste Lauf legt nur den Ausgangsstand fest.
Der Stand liegt lokal in werkzeuge/_beobachtung/ (nicht im Repo).
"""
import concurrent.futures as cf, difflib, hashlib, html, json, pathlib, re, sys, urllib.parse, urllib.request
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
KARTEN = ROOT / "karten"
STAND = ROOT / "werkzeuge" / "_beobachtung"
DIREKT = {"Preise", "Release Notes", "Trust Center"}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def seiten(p):
    t = p.read_text()
    web = re.search(r'^website:\s*"?([^"\n]+)', t, re.M)
    web = web.group(1).strip() if web else ""
    abschnitt = lambda n: t.split(f"## {n}")[1].split("\n## ")[0] if f"## {n}" in t else ""
    urls = [u for lab, u in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", abschnitt("Direktlinks")) if lab in DIREKT]
    if web: urls.append(web)
    domain = urllib.parse.urlparse(web).netloc.removeprefix("www.")
    extra = [u for u in re.findall(r"\]\((https?://[^)\s]+)\)", abschnitt("Quellen"))
             if domain and domain in urllib.parse.urlparse(u).netloc and not u.lower().endswith(".pdf")]
    for u in extra:
        if len(urls) >= 5: break
        if u not in urls: urls.append(u)
    return list(dict.fromkeys(urls))


def text(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "de,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=25) as r:
        roh = r.read(3_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
    roh = re.sub(r"(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>", " ", roh)
    roh = re.sub(r"(?s)<[^>]+>", "\n", roh)
    zeilen = [re.sub(r"\s+", " ", html.unescape(z)).strip() for z in roh.split("\n")]
    # Zeilen ohne Aussage (Menüs, Einzelwörter) und typische wechselnde Teile weglassen
    zeilen = [z for z in zeilen if len(z) > 25 and not re.search(r"cookie|©|copyright|all rights reserved|trace id|[0-9a-f]{16,}", z, re.I)]
    return "\n".join(dict.fromkeys(zeilen))


def main():
    STAND.mkdir(parents=True, exist_ok=True)
    alt = json.loads((STAND / "stand.json").read_text()) if (STAND / "stand.json").exists() else {}
    auftraege = [(p.stem, u) for p in sorted(KARTEN.glob("*.md")) for u in seiten(p)]
    neu, fehler, geaendert = {}, [], {}
    with cf.ThreadPoolExecutor(16) as ex:
        res = {ex.submit(text, u): (s, u) for s, u in auftraege}
        for f in cf.as_completed(res):
            s, u = res[f]
            try:
                t = f.result()
            except Exception as e:
                fehler.append(f"{s}: {u} ({type(e).__name__})")
                if u in alt.get(s, {}): neu.setdefault(s, {})[u] = alt[s][u]
                continue
            h = hashlib.sha256(t.encode()).hexdigest()[:16]
            datei = STAND / "text" / f"{h}.txt"
            datei.parent.mkdir(exist_ok=True)
            datei.write_text(t)
            neu.setdefault(s, {})[u] = h
            vorher = alt.get(s, {}).get(u)
            if vorher and vorher != h and (STAND / "text" / f"{vorher}.txt").exists():
                a = (STAND / "text" / f"{vorher}.txt").read_text().splitlines()
                diff = [z for z in difflib.unified_diff(a, t.splitlines(), lineterm="", n=0) if z[:1] in "+-" and z[:3] not in ("+++", "---")]
                if diff: geaendert.setdefault(s, []).append((u, diff))
    (STAND / "stand.json").write_text(json.dumps(neu, indent=1, sort_keys=True))
    erster = not alt
    zeilen = [f"# Beobachtung {date.today().isoformat()}", ""]
    if erster:
        zeilen.append(f"Erster Lauf: Ausgangsstand für {len(neu)} Anbieter und {sum(map(len, neu.values()))} Seiten festgelegt, noch kein Vergleich.")
    else:
        neue = sorted(set(neu) - set(alt))
        zeilen.append(f"Geändert: {len(geaendert)} von {len(neu)} Anbietern." + (f" Neu beobachtet: {', '.join(neue)}." if neue else ""))
        for s in sorted(geaendert):
            zeilen += ["", f"## {s}"]
            for u, diff in geaendert[s]:
                zeilen.append(f"- {u}")
                kurz = "\n".join(diff)[:1800]
                zeilen += ["```", kurz, "```"]
    if fehler:
        zeilen += ["", f"Nicht erreichbar ({len(fehler)}): " + "; ".join(sorted(fehler))]
    (STAND / "bericht.md").write_text("\n".join(zeilen) + "\n")
    print("\n".join(zeilen[:3]))
    print("geändert:", " ".join(sorted(geaendert)) or "keine")


if __name__ == "__main__":
    main()
