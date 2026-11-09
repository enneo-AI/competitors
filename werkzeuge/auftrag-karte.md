# Auftrag: Battle Card für einen Wettbewerber schreiben

Du schreibst interne Battle Cards für den Vertrieb von **enneo** (Berlin, KI-Plattform für Kundenservice, Hauptkunden Energieversorger, auch Versicherer und BPOs). Die Karten landen in einer internen Galerie und werden von Vertriebsleuten im Kundengespräch genutzt. Sie müssen stimmen.

## Lies zuerst
1. `/Users/aleksaspalevic/Desktop/enneo-projekte/battlecards/karten/vier.md`: **Vorbild für Aufbau, Ton und Tiefe.** Genau dieses Format.
2. `/Users/aleksaspalevic/Desktop/enneo-projekte/battlecards/karten/zendesk.md`: zweites Beispiel.
3. `/Users/aleksaspalevic/Desktop/enneo-projekte/battlecards/werkzeuge/enneo-fakten.md`: **die einzigen Aussagen über enneo, die du verwenden darfst.**

## Recherche
- Quellen: Website des Anbieters (Produkt, Preise, Sicherheit/Trust Center, Zertifikate, Impressum, Referenzen, Release Notes, Doku), Presse, Bewertungsportale (OMR, G2). Alles per WebSearch und WebFetch prüfen, nicht aus dem Gedächtnis.
- Jede Aussage über den Wettbewerber muss aus einer Quelle stammen, die in „Quellen“ verlinkt ist. Was du nicht findest, schreibst du als „nicht gefunden“ oder „nicht öffentlich“, nie als „haben sie nicht“.
- Besonders prüfen: Kann der Anbieter eingehende E-Mails per KI bis zur Aktion im Zielsystem bearbeiten? Mehrere Anliegen in einer Mail? Anhänge/Fotos? Voicebot? Eigener Arbeitsplatz für Mitarbeitende oder Übergabe an fremdes Contact Center? Hosting-Ort und Firma dahinter? Zertifikate (ISO 27001, SOC 2, BSI C5)? Preise? Referenzen in Energie, Versicherung, DACH?
- Prüfe für jeden enneo-Vorteil: Kann der Wettbewerber das inzwischen auch? Ehrliche Einordnung schlägt Schönfärberei. Wo der Wettbewerber vorn liegt, steht das in „Wo <Name> vorn liegt“.

## Datei schreiben
Pfad: `/Users/aleksaspalevic/Desktop/enneo-projekte/battlecards/karten/<slug>.md` (slug klein, ohne Leerzeichen, z. B. `parloa`, `lime-connect`).

Kopf exakt so (Werte anpassen, keine weiteren Felder):
```
---
name: "<Anzeigename>"
slug: "<slug>"
fokus: "<genau einer: Voicebot | KI-Agenten | E-Mail-KI | Contact Center | Helpdesk | CRM & ERP>"
naehe: "<hoch, wenn gleiche Fälle bei gleichen Kunden (DACH, Energie/Versicherung, E-Mail- oder Voice-Automatisierung), sonst mittel>"
kategorie: "Direkter Wettbewerber"
stand: "2026-11-05"
geprueft_von: "Enni"
website: "https://..."
kurz: "<ein Satz, max. 12 Wörter, was der Anbieter ist>"
---
```

Danach diese Abschnitte in dieser Reihenfolge (`## `-Überschriften exakt so, `<Name>` ersetzen):
1. `## Eckdaten`: Tabelle wie im Vorbild, Kopfzeile `| | | |`, 6 Zeilen mit genau diesen Bezeichnungen in Spalte 1, in dieser Reihenfolge: `Firma` (Sitz, Größe), `Gegründet` (Jahr, in Spalte 3 Gründer oder Herkunft der Firma), `Ursprung` (womit die Firma angefangen hat und seit wann es die KI gibt, z. B. Spalte 2 **„CRM seit 1999“** oder **„von Anfang an KI“**, Spalte 3 die Geschichte in einem Satz), `Preise`, `Hosting`, `Zertifikat` oder `Referenzen`. Spalte 2 fett und kurz (max. 4 Wörter), Spalte 3 Erläuterung. Gründungsjahr und Ursprung nur mit Quelle (Impressum, „Über uns“, Handelsregister, Presse), sonst „nicht gefunden“. Ursprung sachlich: was belegt ist, keine Wertung wie „nicht KI-nativ“.
2. `## Erster Satz`: genau ein Satz, den ein Vertriebler im Call sagen kann, wenn der Kunde <Name> erwähnt. Anerkennend gegenüber <Name>, lenkt auf den Punkt, wo enneo gewinnt. In „…“.
3. `## Das Wichtigste vorweg`: 3 bis 4 Sätze.
4. `## Unsere Verkaufsargumente`: 3 bis 5 Punkte, Format `- **Kurztitel:** Text`. Nur mit enneo-Fakten aus der Datei.
5. `## Business-Impact`: Tabelle `| Mit enneo | Ergebnis für den Kunden | So sagen Sie es |`, 4 bis 6 Zeilen. Jede Zeile beschreibt, was der Kunde gewinnt, wenn er enneo statt <Name> nimmt, nie eine Aussage über <Name> allein. Spalte 1: was enneo kann, fett und kurz, aus Sicht von enneo formuliert (z. B. **Mails und Briefe bis zur Buchung**, **Ein System für KI und Team**, **Speicherung in Deutschland**). Spalte 2: das positive Ergebnis für den Kunden in Geld, Zeit, Risiko oder Aufwand, als Ergebnis formuliert (z. B. „Auch der Schriftverkehr läuft automatisch, weniger Mitarbeitende für Mails und Briefe“, „Ein Vertrag und ein System statt zwei“, „Datenschutzprüfung ohne Nachforderungen“). Spalte 3: ein Satz zum Vorlesen in „…“. Nur Unterschiede, die in dieser Karte belegt sind, und nur enneo-Fakten. Keine erfundenen Zahlen: Wirkung beschreiben, nicht beziffern, außer die Zahl steht in den enneo-Fakten.
6. `## Wo <Name> vorn liegt`: 3 bis 5 Punkte, gleiches Format.
7. `## Unterschiede auf einen Blick`: Tabelle `| Bereich | Thema | enneo | <Name> | Einordnung |`, 8 bis 12 Zeilen, Thema fett. **Bereich** genau einer dieser Werte (die Galerie gruppiert danach, Reihenfolge egal): `Kanäle`, `KI & Automatisierung`, `Arbeitsplatz & Anbindungen`, `Daten & Sicherheit` (Speicherort, Betrieb beim Kunden, Zertifikate), `Preis & Vertrag`, `Firma & Referenzen`. **Belege:** In der Spalte <Name> endet jede Zelle mit dem Link auf die Seite, die die Aussage belegt, als `[Kurzname](URL)` (z. B. `[Preisseite](https://…)`, bei „nicht gefunden“ die Seite, auf der gesucht wurde), mehrere durch Leerzeichen getrennt. Kurzname 1 bis 2 Wörter. Jede belegende Seite steht auch unter Quellen. Einordnung genau einer dieser Werte: `enneo klar vorn`, `enneo vorn`, `gleich`, `je nach Fall`, `<Name> vorn`, `<Name> klar vorn` (mit exakt dem Anzeigenamen aus dem Kopf).
8. `## Wo <Name> schwächer ist`: 2 bis 4 Punkte.
9. `## Einwände`: 3 Punkte im Format `- **„Einwand des Kunden“** Antwortvorschlag in 1 bis 3 Sätzen.` Typische Einwände: Marktführer, Referenzen, Preis, schon im Haus, Partnerschaft. Antwort erkennt Berechtigtes an und lenkt auf belegte enneo-Stärken.
10. `## Fragen an den Kunden`: 3 Punkte im Format `- **Frage, die eine Schwäche von <Name> sichtbar macht?** Erwartete Antwort: … Überleitung: „…“` Nur Schwächen, die in der Karte belegt sind oder als „nicht gefunden“ markiert sind (dann als echte Frage, nicht als Behauptung).
11. `## Intern`: was enneo aus eigenen Gesprächen weiß (Abschnitt „Intern aus Attio“ unten). 0 bis 9 Punkte, neueste zuerst, im Format `- **Kurztitel:** Aussage. *Attio-Call vom 27.10.2026, Min. 35:09*` (bei Notizen „Attio-Notiz vom …“, bei Mails „Attio-Mail vom …“). Gibt es nichts, genau diese Zeile: `Bisher keine internen Erkenntnisse in Attio (Stand <Datum>).`
12. `## Fazit`: 2 bis 3 Sätze: wo gewinnen wir, wo nicht.
13. `## Direktlinks`: Liste `- [Bezeichnung](URL)` mit den Einstiegsseiten des Anbieters, die ein Vertriebler direkt öffnen will. Nur diese Bezeichnungen, nur was es öffentlich gibt, in dieser Reihenfolge: `Doku`, `API`, `Community`, `Trust Center`, `Preise`, `Release Notes`, `Status`. Die Website steht schon im Kopf und kommt hier nicht hin. Gibt es keine, entfällt der Abschnitt.
14. `## Quellen`: Liste `- [Kurztext](URL)`, nur tatsächlich geöffnete öffentliche Seiten (Attio-Links stehen nur unter Intern).

## Intern aus Attio
Werkzeuge: der Attio-Connector, per ToolSearch laden (Suchbegriff „attio semantic search“, dazu `get-call-recording`, `get-note-body`, `get-email-content`), nur lesen. Attio (Workspace „Enneo“) ist enneos CRM mit Call-Aufnahmen, Mails und Notizen aus Kunden- und Partnergesprächen. Dort steht oft, wie ein Anbieter in der Praxis wirklich funktioniert, anders als im Marketing. Vorgehen:
- Suche mit `semantic-search-call-recordings`, `semantic-search-notes` und `semantic-search-emails` (mit `include_emails_of_others: true`) nach dem Anbieternamen, Produktnamen und Schreibvarianten (z. B. „Parloa“, „Paloa“), jeweils auch mit Zusatz wie „Erfahrung“, „Preis“, „Probleme“, „wechseln“. Treffer mit `get-call-recording`, `get-note-body` bzw. `get-email-content` an der Stelle lesen.
- Aufnehmen nur, was Kunden, Interessenten oder Partner aus eigener Erfahrung über den Anbieter sagen: Erfahrungen, Probleme, Preise und Angebote, Wechselgründe, Grenzen in der Praxis, Lob. Kein Marketing-Wiederkäuen, keine reinen Erwähnungen.
- **Anonymisieren:** Im Text nie Firmen- oder Personennamen von Kunden, Interessenten oder Partnern. Stattdessen Art und Branche, z. B. „ein Bestandskunde (Energieversorger, Großkunde)“, „ein Interessent (Versicherung)“, „ein Partner (BPO)“. Als Quelle nur Art und Datum (und Minute), keinen Call-Titel, weil Titel oft Kundennamen enthalten. Das Datum steht in `get-call-recording`. Wer die Stelle braucht, findet sie in Attio über Datum und Anbieternamen.
- Wörtliche Zitate kurz (höchstens 15 Wörter) in „…“, mit Minute, wenn bekannt.
- Gilt nur für den Abschnitt Intern. Die übrigen Abschnitte bleiben auf öffentlichen Quellen, Intern-Wissen darf aber in Einwände und Fragen einfließen, ohne Herkunft zu nennen.

## Englische Fassung
Die Galerie lässt sich auf Englisch umschalten. Nach der deutschen Karte schreibst du `karten/en/<slug>.md` nach `werkzeuge/auftrag-uebersetzung.md` (Überschriften, erste Eckdaten-Spalte und Urteile bleiben deutsch, `stand` identisch). Änderst du eine bestehende Karte und setzt `stand` neu, übersetzt du die englische Fassung neu. PDFs gibt es nur auf Deutsch.

## Sprache
Deutsch, kurze Sätze, aktiv. Keine Gedankenstriche (– oder —), stattdessen Komma, Doppelpunkt oder Punkt. Keine Werbesprache, keine Floskeln. Fachbegriffe verständlich. Keine Namen von enneo-Kunden. Preise des Wettbewerbers nur, wenn öffentlich belegt.

## Rückmeldung
Am Ende kurz: welche Datei(en) geschrieben (deutsch und englisch), die 2 wichtigsten Erkenntnisse je Anbieter, was Attio intern ergab und was du nicht belegen konntest.
