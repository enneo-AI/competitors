"""Baut die Galerie: karten/*.md -> site/index.html, dazu site/alle-karten.md für LLMs.
Aufruf: uv run --with markdown python3 werkzeuge/build.py"""
import json, re, shutil, pathlib, html
import markdown
ROOT = pathlib.Path(__file__).resolve().parent.parent
KARTEN, SITE = ROOT / "karten", ROOT / "site"
PILLS = [("klar vorn", "enneo", "p-voll"), ("vorn", "enneo", "p-hell"), ("gleich", None, "p-grau"),
         ("je nach Fall", None, "p-offen")]

def parse(p):
    t = p.read_text()
    _, fm, body = t.split("---", 2)
    meta = {k: v.strip().strip('"') for k, v in (l.split(":", 1) for l in fm.strip().splitlines())}
    return meta, body.strip()

def pill_class(label, name):
    if label.startswith("enneo klar"): return "p-voll"
    if label.startswith("enneo"): return "p-hell"
    if label.startswith(name) and "klar" in label: return "p-dunkel"
    if label.startswith(name): return "p-rand"
    if label == "gleich": return "p-grau"
    return "p-offen"

def render(meta, body):
    h = markdown.markdown(body, extensions=["tables"])
    def td(m):
        lab = m.group(1)
        return f'<td><span class="pill {pill_class(lab, meta["name"])}">{lab}</span></td>\n</tr>'
    labels = "|".join(re.escape(x) for x in ["enneo klar vorn", "enneo vorn", "gleich", "je nach Fall",
                                                f"{meta['name']} klar vorn", f"{meta['name']} vorn"])
    h = re.sub(rf"<td>({labels})</td>\s*</tr>", td, h)
    h = h.replace("<a href=", '<a target="_blank" rel="noopener" href=')
    return h

karten = []
for p in sorted(KARTEN.glob("*.md")):
    meta, body = parse(p)
    h = render(meta, body)
    vorn = h.count("pill p-voll") + h.count("pill p-hell")
    hinten = h.count("pill p-rand") + h.count("pill p-dunkel")
    folge = re.findall(r'class="pill (p-[a-z]+)"', h)
    # Eckdaten für die Übersichtstabelle
    eck = {}
    if "## Eckdaten" in body:
        for r in body.split("## Eckdaten")[1].split("\n## ")[0].splitlines():
            z = [c.strip() for c in r.strip().strip("|").split("|")]
            if len(z) >= 3 and z[0] and not z[0].startswith("-"):
                eck[z[0]] = (z[1].replace("**", ""), z[2])
    meta["firma"] = eck.get("Firma", ("", ""))[0]
    meta["hosting"] = eck.get("Hosting", ("", ""))[0]
    meta["preis"] = (eck.get("Preise") or eck.get("Lizenz") or ("", ""))[0]
    meta.update(html=h, vorn=vorn, hinten=hinten, folge=folge, md=p.name)
    karten.append(meta)

# Ein Dokument für LLMs: alle Karten am Stück
SITE.mkdir(exist_ok=True)
A = ROOT / "werkzeuge" / "assets"
(SITE / "fonts").mkdir(exist_ok=True)
for f in A.glob("*.ttf"): shutil.copy(f, SITE / "fonts" / f.name)
shutil.copy(A / "enneo-logo.svg", SITE / "enneo-logo.svg")
(SITE / "alle-karten.md").write_text("\n\n".join(p.read_text() for p in sorted(KARTEN.glob("*.md"))))
shutil.copytree(KARTEN, SITE / "karten", dirs_exist_ok=True)
shutil.copy(ROOT / "werkzeuge" / "enneo-fakten.md", SITE / "enneo-fakten.md")
shutil.copy(ROOT / "werkzeuge" / "auftrag-karte.md", SITE / "auftrag-karte.md")
shutil.copytree(ROOT / "pdf", SITE / "pdf", dirs_exist_ok=True)
# Logos je Anbieter (werkzeuge/logos.py holt fehlende)
LOGOS = A / "logos"
shutil.rmtree(SITE / "logos", ignore_errors=True); (SITE / "logos").mkdir()
for k in karten:
    datei = next(iter(sorted(LOGOS.glob(k["slug"] + ".*"))), None) if LOGOS.exists() else None
    if datei:
        shutil.copy(datei, SITE / "logos" / datei.name)
        k["logo"] = "logos/" + datei.name

# PDF je Karte aus der Markdown-Karte bauen, wenn keine handgesetzte PDF hinterlegt ist
import subprocess, os
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
DRUCK = ROOT / "werkzeuge" / "_druck"; DRUCK.mkdir(exist_ok=True)
def datum(iso): j, m, t = iso.split("-"); return f"{t}.{m}.{j}"
for k in karten:
    if k.get("pdf_intern"): continue
    h = k["html"]
    teile = re.split(r"(?=<h2>)", h)
    def sek(t): return next((x for x in teile if x.startswith(f"<h2>{t}</h2>")), "")
    fazit = sek("Fazit"); quellen = sek("Quellen"); eck = sek("Eckdaten")
    rest = "".join(x for x in teile if x not in (fazit, quellen, eck))
    links = " · ".join(f'<a href="{u}">{t}</a>' for u, t in re.findall(r'href="([^"]+)"[^>]*>([^<]+)</a>', quellen))
    doc = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><link rel="stylesheet" href="../druck.css"></head><body>
<div class="hd"><div class="l"><img src="../assets/enneo-logo.svg"><span class="sec">Intern · Vertrieb</span></div>
<div class="r"><b>Vergleich · enneo vs. {k['name']}</b>Stand {datum(k['stand'])} · nur intern</div></div>
<h1>enneo vs. <em>{k['name']}</em></h1><p class="lede">{k['kurz']}</p>
<div class="eck">{eck.replace('<h2>Eckdaten</h2>','')}</div>
{('<div class="fazit">' + fazit.replace('<h2>Fazit</h2>','') + '</div>') if fazit else ''}
{rest}
<h2>Quellen</h2><p class="quellen">{links}</p></body></html>"""
    src = DRUCK / f"{k['slug']}.html"; src.write_text(doc)
    ziel = ROOT / "pdf" / f"enneo-vs-{k['slug']}.pdf"
    if not os.path.exists(CHROME):
        # Auf Netlify gibt es kein Chrome: vorhandenes PDF aus dem Repo verwenden
        if ziel.exists(): k["pdf_intern"] = ziel.name
        continue
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                    f"--print-to-pdf={ziel}", src.as_uri()], check=True, capture_output=True)
    k["pdf_intern"] = ziel.name
shutil.copytree(ROOT / "pdf", SITE / "pdf", dirs_exist_ok=True)

tpl = (ROOT / "werkzeuge" / "vorlage.html").read_text()
logo = (A / "enneo-logo.svg").read_text()
logo = re.sub(r"<\?xml[^>]*>\s*", "", logo).replace(".st2{fill:#292C3F}", ".st2{fill:currentColor}")
logo = logo.replace('<svg id="Layer_1"', '<svg class="logo" role="img" aria-label="enneo"', 1)
fragment = tpl.replace("/*LOGO*/", logo).replace("/*DATEN*/[]", json.dumps(karten, ensure_ascii=False).replace("</", "<\\/"))
(SITE / "artifact.html").write_text(fragment)
(SITE / "index.html").write_text('<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>' + fragment + "</body></html>")
print(f"{len(karten)} Karten gebaut -> {SITE/'index.html'}")
