---
name: "Rasa"
slug: "rasa"
fokus: "KI-Agenten"
naehe: "mittel"
kategorie: "Direkter Wettbewerber"
stand: "2026-11-06"
geprueft_von: "Enni"
website: "https://rasa.com"
kurz: "Entwickler-Plattform für Chat- und Voicebots aus Berlin und San Francisco"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Berlin + San Francisco** | Rasa Technologies GmbH (Berlin, HRB 184024 B) und Rasa Technologies Inc. (San Francisco). Über 70 Mio. USD Risikokapital, zuletzt 30 Mio. USD Serie C im Februar 2024 (StepStone, PayPal Ventures, Andreessen Horowitz, Accel). Größe nicht öffentlich |
| Preise | **nicht öffentlich** | Enterprise auf Anfrage. Kostenlose Developer Edition: ein Bot je Firma, bis 1.000 externe oder 100 interne Gespräche im Monat |
| Hosting | **beim Kunden** | „On-premise by default“, Rasa hostet laut Sicherheitsseite keine Kundendaten. Die Preisseite nennt zusätzlich einen Managed Service, Ort und Betreiber nicht genannt |
| Zertifikat | **keines genannt** | Kontrollen laut Rasa an ISO 27002 ausgerichtet, Nachweise auf Anfrage. ISO 27001 oder SOC 2 nicht gefunden |

## Erster Satz

„Rasa ist ein starkes Werkzeug, wenn Ihr eigenes Entwicklerteam Chat- und Voicebots selbst bauen und betreiben will, und bei den Mails setzen wir an: Die erledigt bei uns eine fertige KI bis zur Buchung im Zielsystem.“

## Das Wichtigste vorweg

Rasa ist ein Baukasten für Entwickler: Chat- und Voicebots aus festen Abläufen („Flows“) und Sprachmodell, betrieben in der Infrastruktur des Kunden. Rasa selbst schreibt, Forrester sehe es passend für Firmen mit eigenen Entwicklern oder mit Pflicht zum Betrieb im eigenen Haus. Ein E-Mail-Kanal, ein Arbeitsplatz für Mitarbeitende und fertige Abläufe für Versorger sind nicht dokumentiert. enneo gewinnt, wo ein fertiges Produkt für Schriftverkehr und Kundenservice gesucht wird, Rasa, wo ein Entwicklerteam alles selbst bauen, betreiben und jedes Modell frei wählen will.

## Unsere Verkaufsargumente

- **E-Mail-KI fertig im Produkt:** Bei enneo liest die KI die Mail, erkennt und legitimiert den Kunden, bucht im Zielsystem und antwortet, auch vollautomatisch. Bei Rasa nennt die Startseite E-Mail als Kanal, die Kanalliste der Doku führt aber keinen E-Mail-Kanal. Dafür müsste ein eigener Connector in Python gebaut werden.
- **Mehrere Anliegen und Anhänge:** Zählerstand, neue IBAN und neuer Abschlag in einer Mail erledigt enneo in einem Durchgang mit einer Antwort, Zählerfotos und PDF liest die KI mit. Bei Rasa ist zu beidem nichts dokumentiert.
- **Arbeitsplatz inklusive:** Bei enneo sind Ticketing-Arbeitsplatz, Postfach, KI-Agenten, Wissen, Telefonie und Voicebot ein System mit Skill-Routing. Einen Arbeitsplatz für Mitarbeitende haben wir bei Rasa nicht gefunden, übergebene Fälle landen in einem anderen System.
- **Beschreiben statt programmieren:** enneo-KI-Agenten werden in normaler Sprache beschrieben und mit Neo per Chat geändert. Rasa ist laut eigener Forrester-Einordnung für Firmen mit Entwicklerressourcen gedacht. Abläufe entstehen als Flows mit Python-Aktionen, Studio ergänzt eine Low-Code-Oberfläche.
- **Bei Energieversorgern zusätzlich:** Zählerstand, Abschlag und Bankdaten sind bei enneo fertige KI-Agenten mit Plausibilitätsprüfung. Rasa nennt die Energiebranche nicht, Referenzen kommen aus Telekommunikation, Banken und Versicherungen.

## Business-Impact

| Unterschied | Was das für den Kunden heißt | So sagen Sie es |
|---|---|---|
| **E-Mail-KI im Produkt** | Keinen eigenen E-Mail-Anschluss bauen und pflegen, Mails sind ab dem ersten Tag dabei | „Bei uns ist die Mail-Bearbeitung kein Projekt, sondern ein fertiger Teil des Produkts.“ |
| **Mehrere Anliegen und Anhänge** | Eine vollständige Antwort statt Rückfragen, Zählerfotos tippt niemand ab | „Schreibt Ihr Kunde Zählerstand, IBAN und Abschlag in eine Mail mit Foto, bekommt er bei uns eine Antwort.“ |
| **Arbeitsplatz inklusive** | Kein zweites System für die Mitarbeitenden lizenzieren und anbinden | „Was die KI nicht selbst erledigt, bearbeiten Ihre Leute im selben System weiter.“ |
| **Beschreiben statt programmieren** | Fachbereich ändert Abläufe selbst, weniger Abhängigkeit vom Entwicklerteam | „Bei uns beschreibt Ihr Fachbereich einen Ablauf in normaler Sprache, ohne Entwicklerteam.“ |
| **Betrieb durch enneo** | Kein eigenes Team für Server, Updates und Versionswechsel | „Wir betreiben die Plattform in Deutschland bei Hetzner, Sie müssen keinen eigenen Betrieb aufbauen.“ |
| **Fertige Abläufe für Versorger** | Zählerstand, Abschlag und Bankdaten schneller produktiv, nur die ERP-Anbindung wird gebaut | „Die wichtigsten Versorger-Abläufe bringen wir fertig mit Plausibilitätsprüfung mit.“ |

## Wo Rasa vorn liegt

- **Betrieb im eigenen Haus als Standard:** Rasa läuft laut eigener Aussage in der Infrastruktur des Kunden, personenbezogene Daten verlassen sie nicht. Der Verkaufsassistent von Helvetia läuft laut Fallstudie „on-prem“. Bei enneo ist der Betrieb beim Kunden erst ab großem Volumen möglich.
- **Freie Wahl des Sprachmodells:** OpenAI, Azure, Bedrock, Mistral, Gemini, Anthropic und selbst gehostete Modelle über vLLM oder Ollama, laut Rasa auch kleine angepasste Modelle ab Llama 8B. Bei enneo sind US-Anbieter Standard, EU-Modelle im AVV möglich.
- **Breite bei Voice:** Telefonie über AudioCodes, Jambonz, Twilio, Vonage, SignalWire, Sprachdienste von Deepgram, Azure, Cartesia, Rime und seit Oktober 2026 ElevenLabs, dazu Gesprächsaufzeichnung. enneo hat weniger Auswahl an Sprachanbietern.
- **Werkzeuge für Entwicklerteams:** Versionskontrolle, CI/CD, getrennte Umgebungen, automatische Tests mit simulierten Gesprächen. Laut Rasa 5 von 5 Punkten bei Forrester für Orchestrierung, Lebenszyklus und Preistransparenz, Gesamturteil „Strong Performer“ (Q2 2026). Dazu eine kostenlose Developer Edition zum Ausprobieren.
- **Große Referenzen im DACH-Raum:** Deutsche Telekom mit über 38 Mio. Gesprächen, Swisscom mit Voice-IVR und laut Rasa 50 % weniger Betriebskosten, ERGO, Helvetia, Raiffeisen.

## Unterschiede auf einen Blick

| Thema | enneo | Rasa | Einordnung |
|---|---|---|---|
| **KI-Bearbeitung von E-Mails** | Eine KI liest, erkennt den Kunden, bucht und antwortet, auch vollautomatisch | Kein E-Mail-Kanal in der Doku, nur über selbst gebauten Connector | enneo klar vorn |
| **Mehrere Anliegen in einer Mail** | Alles in einem Durchgang, eine Antwort | Nicht dokumentiert | enneo vorn |
| **Anhänge und Fotos lesen** | PDF und Fotos, z. B. Zählerfoto | Nicht gefunden | enneo vorn |
| **Arbeitsplatz für Mitarbeitende** | Ticketing, Postfach und Skill-Routing im selben System | Nicht gefunden, Übergabe an ein anderes System | enneo klar vorn |
| **Fertige Abläufe für Versorger** | Zählerstand, Abschlag, Bankdaten fertig, ERP-Anbindung pro Kunde | Energiebranche nicht genannt, Versicherungsfälle als Beispiele | enneo vorn |
| **KI-Agenten bauen und testen** | In Worten beschreiben, mit Neo per Chat ändern, Testfälle | Flows mit Python-Aktionen, Studio als Low-Code, Tests mit simulierten Gesprächen | je nach Fall |
| **Wo betrieben wird** | Hetzner in Deutschland, beim Kunden ab großem Volumen | Beim Kunden als Standard, Managed Service ohne genannten Ort | je nach Fall |
| **Sprachmodelle** | US-Anbieter Standard, EU-Modelle im AVV: Mistral, Nebius, Media Trooper | Frei wählbar, auch selbst gehostet | Rasa vorn |
| **Voicebot und Sprachdienste** | Eigene Telefonie oder SIP, OpenAI (USA) oder Deepslate (EU) | Mehrere Telefonie-Anbindungen, fünf Sprachdienst-Anbieter, Aufzeichnung | Rasa vorn |
| **Unterlagen zum Datenschutz** | AVV, TOM, Subunternehmer, SLA öffentlich | Keine Subunternehmerliste, AVV nicht öffentlich gefunden | enneo vorn |
| **Zertifikate** | Keine eigenen, ISO 27001 und SOC 2 in Prüfung, Hetzner ISO 27001 | Keine genannt, an ISO 27002 ausgerichtet | gleich |

## Wo Rasa schwächer ist

- **Kein fertiges Produkt für Service-Teams:** Laut Rasas eigener Zusammenfassung der Forrester-Bewertung finden Käufer, die breite No-Code-Werkzeuge, ein großes Partnernetz oder einen gemanagten Betrieb wollen, anderswo Besseres.
- **Betrieb und Pflege beim Kunden:** Server, Updates und Versionswechsel liegen beim Kunden. Rasa bringt jeden Monat eine neue Version, die Version 3.21 vom Oktober 2026 enthält mehrere Änderungen, die bestehende Projekte anpassen müssen.
- **Schriftverkehr nicht im Fokus:** Kein E-Mail-Kanal in der Doku, keine E-Mail-Referenz gefunden, Anhänge und mehrere Anliegen nicht dokumentiert.
- **Wenig Nachweise nach außen:** Kein Zertifikat genannt, keine Subunternehmerliste. Bei OMR gibt es noch keine Bewertung.

## Einwände

- **„Rasa ist Forrester Strong Performer und bei Telekom und Swisscom im Einsatz.“** Stimmt, das sind starke Referenzen für Chat und Voice in der Telekommunikation. Eine Referenz für E-Mail-Bearbeitung oder für Energieversorger haben wir nicht gefunden, fragen Sie gezielt danach.
- **„Mit Rasa bleibt alles im eigenen Haus.“** Das ist ein echter Vorteil, wenn der Betrieb im eigenen Rechenzentrum Pflicht ist. enneo geht ab großem Volumen ebenfalls beim Kunden, sonst betreiben wir in Deutschland bei Hetzner, und Ihr Team muss keinen eigenen Betrieb aufbauen.
- **„Rasa gibt es kostenlos.“** Die Developer Edition ist frei, aber auf einen Bot und 1.000 Gespräche im Monat begrenzt, Enterprise kostet auf Anfrage. Dazu kommen Entwickler und Betrieb, die bei enneo im Produkt stecken.

## Fragen an den Kunden

- **Wer baut, betreibt und aktualisiert den Bot bei Ihnen, und wie viele Entwickler sind dafür eingeplant?** Erwartete Antwort: das eigene IT-Team oder ein Dienstleister. Überleitung: „Bei uns beschreibt der Fachbereich die Abläufe, und den Betrieb übernehmen wir.“
- **Wie sollen die E-Mails Ihrer Kunden in Rasa ankommen und dort bis zur Buchung bearbeitet werden?** Erwartete Antwort: noch offen oder über eine eigene Anbindung. Überleitung: „Bei uns ist das der Kern des Produkts, zeigen wir gern mit Ihren eigenen Beispielmails.“
- **Wo bearbeiten Ihre Mitarbeitenden die Fälle, die der Bot nicht selbst löst?** Erwartete Antwort: in einem anderen System, das extra angebunden wird. Überleitung: „Bei uns arbeiten KI und Mitarbeitende im selben System, ohne Übergabe nach außen.“

## Intern

Bisher keine internen Erkenntnisse in Attio (Stand 06.11.2026).

## Fazit

Gegen Rasa gewinnen wir, wo ein Kunde ein fertiges Produkt für Kundenservice sucht: E-Mail-KI bis zur Buchung, mehrere Anliegen, Anhänge, Arbeitsplatz und fertige Versorger-Abläufe ohne eigenes Entwicklerteam. Rasa liegt vorn, wo ein starkes IT-Team Chat- und Voicebots selbst bauen, im eigenen Haus betreiben und Modelle wie Sprachdienste frei wählen will. Dort ist enneo für den Schriftverkehr oft das bessere Gespräch als für den Voicebot.

## Quellen

- [Rasa Startseite](https://rasa.com)
- [Über Rasa](https://rasa.com/about)
- [Impressum](https://rasa.com/imprint)
- [Preise](https://rasa.com/pricing)
- [Sicherheit](https://rasa.com/security-at-rasa)
- [Betrieb und Datenschutz](https://rasa.com/product/managed-service)
- [Kunden](https://rasa.com/customers)
- [Fallstudie Helvetia](https://rasa.com/customers/helvetia)
- [Branche Versicherung](https://rasa.com/industries/insurance)
- [Branche Telekommunikation](https://rasa.com/industries/telecom)
- [CALM erklärt](https://rasa.com/docs/learn/concepts/calm)
- [Kanäle Text und Voice](https://rasa.com/docs/reference/channels/messaging-and-voice-channels)
- [Eigene Kanäle bauen](https://rasa.com/docs/reference/channels/custom-connectors)
- [Sprachdienste](https://rasa.com/docs/reference/integrations/speech-integrations)
- [Sprachmodelle](https://rasa.com/docs/reference/config/components/llm-configuration)
- [Release Notes Rasa Pro](https://rasa.com/docs/reference/changelogs/rasa-pro-changelog)
- [Forrester Wave Q2 2026 aus Sicht von Rasa](https://rasa.com/blog/forrester-wave-2026-where-rasa-stands-out)
- [Serie C, SiliconANGLE](https://siliconangle.com/2024/02/14/draft-conversational-ai-startup-rasa-technologies-raises-30m-combine-llms-traditional-chatbots)
- [Nutzerbewertungen OMR](https://omr.com/en/reviews/product/rasa)
