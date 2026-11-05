"""Einmalige Übernahme: Vergleichs-JSON (PDF-Quelle) -> Markdown-Karte."""
import json, re, sys
PILL = {"pill-voll":"enneo klar vorn","pill":"enneo vorn","pill-grau":"gleich",
        "pill-rand":"{w} vorn","pill-dunkel":"{w} klar vorn","pill-offen":"je nach Fall"}
def pill(v, w):
    k = v.split(":")[0]
    return PILL.get(k, v).format(w=w)
def conv(src, slug, name, kategorie, kurz, website, partner_pdf=None):
    d = json.load(open(src))["dokumente"][0]
    stand = re.search(r"Stand (\S+)", d["kopf_untertitel"]).group(1)
    tt, mm, jj = stand.split(".")
    fm = {"name": name, "slug": slug, "kategorie": kategorie, "stand": f"{jj}-{mm}-{tt}",
          "geprueft_von": "Aleksa Spalevic", "website": website, "kurz": kurz,
          "pdf_intern": f"enneo-vs-{slug}.pdf"}
    if partner_pdf: fm["pdf_partner"] = partner_pdf
    out = ["---"] + [f'{k}: "{v}"' for k, v in fm.items()] + ["---", ""]
    for s in d["seiten"]:
        for a in s["abschnitte"]:
            if "meta" in a:
                out += ["## Eckdaten", "", "| | | |", "|---|---|---|"]
                out += [f"| {m['label']} | **{m['wert']}** | {m['sub']} |" for m in a["meta"]] + [""]
            elif "ueberschrift" in a:
                out += [f"## {a['ueberschrift']}", ""]
            elif "absatz" in a:
                out += [a["absatz"], ""]
            elif "liste" in a:
                out += [f"- {x}" for x in a["liste"]] + [""]
            elif "matrix" in a:
                m = a["matrix"]; sp = m["spalten"]
                if not any(b.get("ueberschrift") == "Unterschiede auf einen Blick" for b in s["abschnitte"]):
                    out += ["## Unterschiede auf einen Blick", ""]
                out += [f"| {sp[0]} | {sp[1]} | {sp[2]} | Einordnung |", "|---|---|---|---|"]
                for z in m["zeilen"]:
                    out.append(f"| {z[0]} | {z[1]} | {z[2]} | {pill(z[3], name)} |")
                out.append("")
            elif "hinweis" in a:
                out += [f"## {a['hinweis']['label']}", "", a["hinweis"]["text"], ""]
            elif "quellen" in a:
                out += ["## Quellen", ""] + [f"- [{l['text']}]({l['url']})" for l in a["quellen"]["links"]] + [""]
    open(f"karten/{slug}.md", "w").write("\n".join(out).rstrip() + "\n")
W = "/Users/aleksaspalevic/Desktop/enneo-projekte/wettbewerb/"
conv(W+"vier.json", "vier", "VIER", "Direkter Wettbewerber",
     "Contact-Center-Plattform aus Hannover, KI als Zusatzmodule", "https://www.vier.ai",
     partner_pdf="enneo-vs-vier-vertrieb.pdf")
conv(W+"zendesk.json", "zendesk", "Zendesk", "Direkter Wettbewerber",
     "Breite Helpdesk-Suite aus den USA, KI je gelöstem Fall abgerechnet", "https://www.zendesk.de")
conv(W+"thinkowl.json", "thinkowl", "ThinkOwl", "Direkter Wettbewerber",
     "KI-Kundenservice-Plattform, wirbt bei Stadtwerken mit Dunkelverarbeitung", "https://www.thinkowl.de")
