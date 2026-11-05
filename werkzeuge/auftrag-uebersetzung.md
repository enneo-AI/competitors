# Auftrag: englische Fassung einer Battle Card

Die Galerie lässt sich auf Englisch umschalten. Zu jeder Karte `karten/<slug>.md` gehört deshalb `karten/en/<slug>.md`. PDFs bleiben deutsch. Die deutsche Karte ist das Original, die englische eine treue Übersetzung: nichts weglassen, nichts ergänzen, nichts neu bewerten.

## Aufbau der Datei

```
---
slug: "<slug wie im Original>"
stand: "<stand wie im Original, unverändert>"
kurz: "<englische Übersetzung von kurz>"
---

<Inhalt>
```

Keine weiteren Felder im Kopf. `stand` muss exakt dem Original entsprechen, daran erkennt die Galerie, dass die Übersetzung aktuell ist. Ändert sich die deutsche Karte, wird die englische komplett neu übersetzt.

## Was deutsch bleibt (Schlüssel für den Code, die Galerie übersetzt sie beim Anzeigen)

1. **Jede `## `-Überschrift exakt wie im Original**, z. B. `## Eckdaten`, `## Erster Satz`, `## Wo Parloa vorn liegt`, `## Intern`, `## Quellen`. Gleiche Reihenfolge.
2. **In `## Eckdaten` die erste Spalte** (`Firma`, `Preise`, `Hosting`, `Zertifikat`, `Lizenz` usw.). Die zweite und dritte Spalte übersetzen.
3. **In `## Unterschiede auf einen Blick` die letzte Spalte** exakt wie im Original: `enneo klar vorn`, `enneo vorn`, `gleich`, `je nach Fall`, `<Name> vorn`, `<Name> klar vorn`. Die Kopfzeile der Tabelle und alle anderen Zellen übersetzen.

## Wie übersetzen

- Natürliches, professionelles Business-Englisch (US-Schreibweise) für Vertriebsleute im Kundengespräch. Kurze Sätze wie im Original, keine Marketing-Floskeln, keine Gedankenstriche.
- Zitate (Erster Satz, „So sagen Sie es“, Einwände) so übersetzen, dass man sie im Call auf Englisch sagen kann.
- Produkt-, Firmen- und Funktionsnamen bleiben, wie der Anbieter sie schreibt. Zitierte deutsche Originaltitel von Anbietern dürfen bleiben, wenn es keinen englischen gibt.
- Zahlen und Daten englisch: `350 Mio. USD` → `USD 350m`, `2.490 €` → `€2,490`, `1,50 €` → `€1.50`, `05.11.2026` → `Nov 5, 2026`, `01/2026` → `01/2026`, `380+ MA` → `380+ employees`.
- Links: URL unverändert, Linktext übersetzen.
- Intern: Anonymisierung beibehalten, Quellen als `*Attio call, Oct 27, 2026, min. 35:09*` (Notiz: `Attio note`, Mail: `Attio email`). Die Leerzeile `Bisher keine internen Erkenntnisse in Attio (Stand <Datum>).` wird zu `No internal insights in Attio yet (as of <date>).`
- Wiederkehrende Begriffe: Sachbearbeiter/Mitarbeitende → agents, Kundenservice → customer service, Energieversorger/Versorger → utilities, Stadtwerke → municipal utilities, Abschlag → installment, Zählerstand → meter reading, Postfach → inbox, Arbeitsplatz → agent workspace, AVV → DPA, Rechenzentrum des Kunden / Betrieb beim Kunden → on-premises, Ausschreibung → tender, Fall/Vorgang → case, Anliegen → request.

## Grenzen

Nur `karten/en/<slug>.md` schreiben. Die deutsche Karte, den Build und Git nicht anfassen.
