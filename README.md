# enneo Wettbewerb · Battle Cards (Prototyp)

Stand 05.11.2026. 21 Karten, alle freigegeben (kein Entwurf-Vermerk mehr). Logos je Anbieter in `werkzeuge/assets/logos/`, fehlende holt `werkzeuge/logos.py`. Übersicht als Tabelle mit Filtern nach Schwerpunkt (`fokus`) und Nähe (`naehe`), dazu ein Co-Pilot (Knopf „Fragen“), der über die sample-Funktion des Artifacts mit dem Claude-Konto des Fragenden läuft und die offene Karte plus `enneo-fakten.md` kennt. Veröffentlicht als claude.ai-Artifact https://claude.ai/artifact/NnZrCd7xu6GVPWmwXEjQeS (für alle mit enneo-Claude-Konto freigeben). Wochenlauf als geplante Aufgabe in Claude Code auf Aleksas enneo MacBook (`battlecards-wochenlauf`, montags 07:11).

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

Verbindlich ist `werkzeuge/auftrag-karte.md`. Kurz (Stand 09.11.2026, nach Feedback aus dem Vertrieb):

1. Eckdaten: Firma, Gegründet, Ursprung (womit die Firma begann, seit wann KI), Preise, Hosting, Zertifikat/Referenzen
2. Erster Satz, Das Wichtigste vorweg
3. Unsere Verkaufsargumente
4. Business-Impact: `Mit enneo | Ergebnis für den Kunden | So sagen Sie es`, jede Zeile aus Sicht des Kunden, der enneo nimmt
5. Wo der Anbieter vorn liegt
6. Unterschiede auf einen Blick: `Bereich | Thema | enneo | Anbieter | Einordnung`. Bereich gruppiert die Zeilen (Kanäle, KI & Automatisierung, Arbeitsplatz & Anbindungen, Daten & Sicherheit, Preis & Vertrag, Firma & Referenzen), jede Anbieter-Zelle endet mit ihrem Beleg-Link
7. Wo der Anbieter schwächer ist, Einwände, Fragen an den Kunden, Intern, Fazit
8. Direktlinks (Doku, API, Community, Trust Center, Preise, Release Notes, Status), Quellen

In der Galerie: Reiter Überblick, Business-Impact, Argumente, Einwände & Fragen, Vergleich, Quellen (oben „Direkt beim Anbieter“), dazu Intern. In Argumente und Einwände & Fragen ist nur die Kernaussage sichtbar, die Erklärung klappt auf.

Kategorien: `Direkter Wettbewerber`, `Angrenzender Anbieter`, `Möglicher Partner`.

## Was noch fehlt (Plan)

- **Veröffentlichen:** `build.py` erzeugt `site/artifact.html` (Seite ohne Dokumentrahmen, so wie Artifacts sie erwarten) und `site/index.html` zum lokalen Ansehen. Fürs Artifact `artifact.html`, `pdf/`, `karten/` und `alle-karten.md` hochladen, PDFs laufen über die Download-Funktion des Artifacts.
- **Wöchentlicher Lauf (seit 05.11.):** geplante Aufgabe `battlecards-wochenlauf` in Claude Code, montags 07:11, läuft nur bei offener App (sonst beim nächsten Start). Prüft alle Karten auf belegte Änderungen, nimmt höchstens 3 neue Wettbewerber auf, baut, pusht, veröffentlicht das Artifact unter demselben Link und schickt Aleksa eine Slack-Direktnachricht. Protokoll in `aenderungen.md`, neue Anbieter bekommen ihr Logo über `werkzeuge/logos.py`. Vorschrift: `~/.claude/scheduled-tasks/battlecards-wochenlauf/SKILL.md`.
- **Neue Anbieter (seit 05.11.):** Plus-Knopf in der Kopfleiste der Galerie. Die Website landet in der Artifact-Datenbank (Sammlung `anfragen`) und steht sofort als nicht anklickbare Zeile in der Tabelle: „In der Warteschlange“, dann „Wird erstellt · <Schritt>“. Erst die fertige, recherchierte Karte erscheint als Eintrag. Die geplante Aufgabe `battlecards-anfragen` schaut werktags 8 bis 19 Uhr alle 10 Minuten nach (nur bei offener App auf Aleksas Mac), recherchiert nach `werkzeuge/auftrag-karte.md`, holt das Logo, baut Karte und PDF, pusht, veröffentlicht und meldet sich per Slack. Bewusst keine Sofort-Karte ohne Recherche: der Vertrieb soll sich auf jede Karte verlassen können. Anfragen kann, wer mindestens Contributor („Mitwirken“) ist. Vorschrift: `~/.claude/scheduled-tasks/battlecards-anfragen/SKILL.md`.
- **Firmenlisten (seit 05.11.):** Im Plus-Feld Excel oder CSV hochladen. Der Lauf ordnet jede Firma ein (Wettbewerber, angrenzend, Partner, kein Anbieter, mit Begründung und Website), die Person wählt danach im Auswahlfenster Kategorien oder einzelne Firmen und startet erst dann die Recherche. Einordnung als Excel exportierbar.
- **PDFs:** `build.py` erzeugt für jede Karte ohne `pdf_intern` im Kopf ein PDF im enneo-Stil (Chrome headless, `werkzeuge/druck.css`). VIER, Zendesk, ThinkOwl haben noch die handgesetzten PDFs aus `../wettbewerb/`.
- **Englisch:** Schalter DE/EN in der Kopfleiste (Auswahl bleibt im Browser gespeichert). Zu jeder Karte gehört `karten/en/<slug>.md` nach `werkzeuge/auftrag-uebersetzung.md`: `## `-Überschriften, erste Eckdaten-Spalte und Urteile bleiben deutsch und werden beim Anzeigen übersetzt (`build.py` `englisch()`, Vorlage `titelText()`), `stand` muss dem Original entsprechen, sonst zeigt die Galerie das deutsche Original mit Hinweis und der Build meldet „veraltet“. Oberflächentexte im Wörterbuch `T` in `vorlage.html`. PDFs nur deutsch.
- **Neue Karte:** Auftrag `werkzeuge/auftrag-karte.md`, enneo-Aussagen nur aus `werkzeuge/enneo-fakten.md`. Fehlendes Logo: `uv run python3 werkzeuge/logos.py`, Ergebnis ansehen, schlechte Datei durch ein quadratisches Logo von der Website ersetzen.
- **Summit-Liste:** `summit/service-summit-2026-anbieter.xlsx` (130 Anbieter eingeordnet).
- **Abruf per Slack/KI:** `alle-karten.md` bzw. das Repo als Wissensquelle für den Slack-Bot und das enneo OS.
