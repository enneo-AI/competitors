# enneo Wettbewerb · Battle Cards (Prototyp)

Stand 05.11.2026. 18 Karten (VIER, Zendesk, ThinkOwl geprüft, 15 weitere als Entwurf „Enni, noch nicht gegengelesen“). Noch nicht gehostet, noch keine Automatisierung.

## Aufbau

| Ordner | Inhalt |
|---|---|
| `karten/` | Eine Markdown-Datei je Anbieter. **Das ist die einzige Quelle.** Oben Eckdaten im Kopf (Name, Kategorie, Stand, Website, PDFs), darunter die Abschnitte. |
| `pdf/` | PDFs je Anbieter: `enneo-vs-<anbieter>.pdf` intern, optional eine Partnerfassung. |
| `site/` | Die gebaute Galerie (`index.html`), dazu `alle-karten.md`, also alle Karten in einer Datei für LLMs. |
| `werkzeuge/` | `build.py` baut die Galerie, `vorlage.html` ist ihr Aussehen, `aus_json.py` hat die drei ersten Karten aus den PDF-Quellen übernommen. |

## Bauen

```bash
cd ~/Desktop/enneo-projekte/battlecards
uv run --with markdown python3 werkzeuge/build.py
open site/index.html
```

## Aufbau einer Karte

Feste Reihenfolge, damit jede Karte gleich zu lesen ist und eine KI sie sicher findet:

1. Eckdaten (Firma, Preise, Hosting, Zertifikat/Referenzen)
2. Das Wichtigste vorweg
3. Unsere Verkaufsargumente
4. Wo der Anbieter vorn liegt
5. Unterschiede auf einen Blick (Tabelle mit Einordnung: `enneo klar vorn`, `enneo vorn`, `gleich`, `<Anbieter> vorn`, `<Anbieter> klar vorn`, `je nach Fall`)
6. Wo der Anbieter schwächer ist
7. Fazit
8. Quellen

Kategorien: `Direkter Wettbewerber`, `Angrenzender Anbieter`, `Möglicher Partner`.

## Was noch fehlt (Plan)

- **Ort mit Login:** Battle Cards sind intern. Hosting mit enneo-Anmeldung, mit der Technik klären.
- **Wöchentlicher Lauf:** Ein geplanter Agent prüft Release Notes, News und Preisseiten der direkten Wettbewerber, ändert die betroffene Karte, setzt das Stand-Datum und baut das PDF neu. Funde laufen als Änderungsvorschlag und werden vor der Veröffentlichung freigegeben.
- **PDFs:** `build.py` erzeugt für jede Karte ohne `pdf_intern` im Kopf ein PDF im enneo-Stil (Chrome headless, `werkzeuge/druck.css`). VIER, Zendesk, ThinkOwl haben noch die handgesetzten PDFs aus `../wettbewerb/`.
- **Neue Karte:** Auftrag `werkzeuge/auftrag-karte.md`, enneo-Aussagen nur aus `werkzeuge/enneo-fakten.md`. Nach dem Gegenlesen `geprueft_von` auf den Namen setzen, dann verschwindet „Entwurf“.
- **Summit-Liste:** `summit/service-summit-2026-anbieter.xlsx` (130 Anbieter eingeordnet).
- **Abruf per Slack/KI:** `alle-karten.md` bzw. das Repo als Wissensquelle für den Slack-Bot und das enneo OS.
- **Gegenlesen:** die 15 Entwürfe vom 05.11. prüfen, besonders die Einordnungen in der Vergleichstabelle.
