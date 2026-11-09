# enneo Battle Cards

Interne Wettbewerbs-Galerie für den enneo-Vertrieb. Repo `enneo-AI/competitors`, Branch `main`, veröffentlicht als claude.ai-Artifact https://claude.ai/artifact/NnZrCd7xu6GVPWmwXEjQeS (immer derselbe Link).

- Karten: `karten/<slug>.md` (Quelle), englisch `karten/en/<slug>.md`. Format und Regeln: `werkzeuge/auftrag-karte.md`, Übersetzung: `werkzeuge/auftrag-uebersetzung.md`. Aussagen über enneo nur aus `werkzeuge/enneo-fakten.md`.
- Bauen: `uv run --with markdown python3 werkzeuge/build.py` (Galerie + PDFs). Ohne PDFs: `CHROME=/nicht-da` davor.
- Änderungen bei Anbietern finden (ohne KI): `python3 werkzeuge/beobachten.py` → `werkzeuge/_beobachtung/bericht.md`.
- Protokoll: `aenderungen.md`. Überblick: `README.md`.
- Commits mit `-c user.name="Aleksa Spalevic" -c user.email="aleksa@enneo.ai"`, Nachricht endet mit `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Intern: nichts öffentlich machen, keine Namen von enneo-Kunden, Interessenten oder Partnern im Kartentext, Attio nur lesen. Sprache Deutsch.
- Die geplanten Aufgaben `enneo-battlecards-anfragen` und `enneo-battlecards-wochenlauf` laufen in diesem Ordner.
