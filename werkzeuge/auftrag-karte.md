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
geprueft_von: "Enni, noch nicht gegengelesen"
website: "https://..."
kurz: "<ein Satz, max. 12 Wörter, was der Anbieter ist>"
---
```

Danach diese Abschnitte in dieser Reihenfolge (`## `-Überschriften exakt so, `<Name>` ersetzen):
1. `## Eckdaten`: Tabelle wie im Vorbild, Kopfzeile `| | | |`, 4 Zeilen mit genau diesen Bezeichnungen in Spalte 1: `Firma` (Sitz, Größe), `Preise`, `Hosting`, `Zertifikat` oder `Referenzen`. Spalte 2 erscheint in der Übersichtstabelle, also kurz halten (max. 4 Wörter). Spalte 2 fett und kurz, Spalte 3 Erläuterung.
2. `## Das Wichtigste vorweg`: 3 bis 4 Sätze.
3. `## Unsere Verkaufsargumente`: 3 bis 5 Punkte, Format `- **Kurztitel:** Text`. Nur mit enneo-Fakten aus der Datei.
4. `## Wo <Name> vorn liegt`: 3 bis 5 Punkte, gleiches Format.
5. `## Unterschiede auf einen Blick`: Tabelle `| Thema | enneo | <Name> | Einordnung |`, 8 bis 12 Zeilen, Thema fett. Einordnung genau einer dieser Werte: `enneo klar vorn`, `enneo vorn`, `gleich`, `je nach Fall`, `<Name> vorn`, `<Name> klar vorn` (mit exakt dem Anzeigenamen aus dem Kopf).
6. `## Wo <Name> schwächer ist`: 2 bis 4 Punkte.
7. `## Fazit`: 2 bis 3 Sätze: wo gewinnen wir, wo nicht.
8. `## Quellen`: Liste `- [Kurztext](URL)`, nur tatsächlich geöffnete Seiten.

## Sprache
Deutsch, kurze Sätze, aktiv. Keine Gedankenstriche (– oder —), stattdessen Komma, Doppelpunkt oder Punkt. Keine Werbesprache, keine Floskeln. Fachbegriffe verständlich. Keine Namen von enneo-Kunden. Preise des Wettbewerbers nur, wenn öffentlich belegt.

## Rückmeldung
Am Ende kurz: welche Datei(en) geschrieben, die 2 wichtigsten Erkenntnisse je Anbieter und was du nicht belegen konntest.
