---
name: "PolyAI"
slug: "polyai"
fokus: "Voicebot"
naehe: "mittel"
kategorie: "Direkter Wettbewerber"
stand: "2026-11-05"
geprueft_von: "Enni"
website: "https://poly.ai"
kurz: "Voice-KI-Agenten aus London mit eigenen Sprachmodellen"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **London, ca. 250 MA** | PolyAI Ltd, 2017 von Forschern aus Cambridge gegründet. Büros in London, New York, San Mateo, Belgrad, Toronto. Series D 12/2025: 86 Mio. USD, Lead Georgian, Hedosophia, Khosla Ventures, dazu NVentures (NVIDIA) und Zendesk Ventures. Insgesamt über 200 Mio. USD |
| Preise | **Plattform nicht öffentlich** | Enterprise-Plattform je verbundener Minute, Satz nur über den Vertrieb. Self-Service-API für das Sprachmodell Dialog-RSN-1: 2 Cent je Minute plus Text-Tokens, ohne Telefonie |
| Hosting | **AWS, Regionen US/UK/EU** | Laut Doku drei Regionen (US, UK, EU). Ein Land innerhalb der EU und einen Betrieb beim Kunden haben wir nicht gefunden |
| Zertifikat | **ISO 27001, SOC 2** | SOC 2 Typ II, dazu PCI DSS, HIPAA, Cyber Essentials Plus. C5 nicht gefunden |

## Erster Satz

„PolyAI hat am Telefon mit eigenen Sprachmodellen eine starke Technik, die Frage ist, wer bei Ihnen die Mails mit echten Vorgängen bearbeitet und in welchem System Ihr Team arbeitet.“

## Das Wichtigste vorweg

PolyAI baut KI-Agenten vor allem fürs Telefon, mit eigenen Sprach- und Dialogmodellen, viel Kapital und großen Kunden in den USA und Großbritannien, etwa PG&E, Marriott und UniCredit. Inzwischen gibt es auch einen E-Mail-Kanal, der beantwortet aber laut Doku Standardfragen aus der Wissensbasis und reicht den Rest mit Antwortentwurf an ein Postfach des Kunden weiter. Einen eigenen Arbeitsplatz für Mitarbeitende und Referenzen in DACH haben wir nicht gefunden. Am Telefon liegt PolyAI vorn, bei Schriftverkehr mit Aktion im Zielsystem und bei allem in einem System liegen wir vorn.

## Unsere Verkaufsargumente

- **E-Mail bis zur Aktion im Zielsystem:** enneo liest die Mail, erkennt Anliegen und Kunden, legitimiert, bucht im ERP und antwortet, auch vollautomatisch. Bei PolyAI beantwortet der E-Mail-Agent laut Doku Fragen aus der Wissensbasis, Beschwerden, Erstattungen und regulierte Anliegen gehen an das Team. Eine Buchung im Zielsystem per Mail ist dort nicht dokumentiert.
- **Mehrere Anliegen, eine Antwort:** Zählerstand, neue IBAN und neuer Abschlag in einer Mail erledigt enneo in einem Durchgang mit einer Antwort. Bei PolyAI ist dazu nichts dokumentiert.
- **Ein System statt zwei:** Bei enneo sind Arbeitsplatz, Postfach, KI-Agenten, Wissen und Telefonie ein Produkt mit Skill-Routing. PolyAI übergibt Anrufe per SIP an ein fremdes Contact Center und Mails als Fall an ein Postfach oder einen Helpdesk wie Zendesk oder Salesforce. Der Kunde braucht also ein zweites System.
- **Fertige Abläufe für Versorger:** Zählerstand, Abschlag und Bankdaten bringt enneo als fertige KI-Agenten mit Plausibilitätsprüfung mit, nur die ERP-Anbindung wird pro Kunde gebaut. PolyAI nennt für Versorger Störungen, Zahlungen, Termine und Identifizierung, Zählerstände nicht.
- **Speicherung bei deutschem Anbieter, kein Training:** enneo speichert bei Hetzner in Deutschland und trainiert nicht mit Kundendaten. PolyAI läuft auf AWS und darf laut Datenschutzhinweis mit Erlaubnis des Kunden Gesprächsausschnitte zum Training nutzen.

## Business-Impact

| Unterschied | Was das für den Kunden heißt | So sagen Sie es |
|---|---|---|
| **E-Mail bis zur Aktion im Zielsystem** | Auch Vorgänge mit Buchung werden automatisch erledigt, weniger Mitarbeitende für Schriftverkehr | „PolyAI beantwortet per Mail Standardfragen, bei uns bucht die KI den Vorgang im Zielsystem und antwortet.“ |
| **Mehrere Anliegen in einem Durchgang** | Eine vollständige Antwort statt Rückfragen und Folgemails | „Zählerstand, IBAN und Abschlag in einer Mail erledigen wir in einem Durchgang mit einer Antwort.“ |
| **Ein System statt zwei** | Kein zweites System und kein zweiter Vertrag für das Team, der Vorgang liegt an einer Stelle | „Bei PolyAI landet der Fall in einem anderen System, bei uns arbeiten KI und Team im selben Arbeitsplatz.“ |
| **Fertige Abläufe für Versorger** | Schneller produktiv bei Zählerstand, Abschlag und Bankdaten, nur die ERP-Anbindung wird gebaut | „Die wichtigsten Versorger-Abläufe bringen wir fertig mit Plausibilitätsprüfung mit.“ |
| **Speicherung in Deutschland, kein Training** | Datenschutzprüfung einfacher, keine Freigabe für Training mit Kundendaten nötig | „Wir speichern bei Hetzner in Deutschland und trainieren nicht mit Ihren Daten.“ |

## Wo PolyAI vorn liegt

- **Telefon und eigene Sprachmodelle:** Eigene Modelle für Sprache (Dialog-RSN-1) und Dialog (Raven), laut PolyAI unter 300 ms Antwortzeit, bis 10.000 parallele Gespräche und 99,994 % Verfügbarkeit. Über 2.000 Einsätze in 45 Sprachen, Deutsch ist dabei. Unser Voicebot läuft über OpenAI oder Deepslate, mit weniger Auswahl.
- **Anbindung an fremde Contact Center:** Laut PolyAI über 130 Integrationen, darunter Genesys, Five9, NICE, Avaya, Cisco, Amazon Connect, Talkdesk, Twilio, dazu Salesforce, Dynamics, ServiceNow, HubSpot und MCP. Übergabe am Telefon per SIP REFER oder INVITE mit eigenen SIP-Headern, Kontext per Handoff-API. Wir geben nur die Ticketnummer im SIP-Header nach außen und lesen eingehend keinen Kontext.
- **Zertifikate:** ISO 27001, SOC 2 Typ II, PCI DSS, HIPAA, Cyber Essentials Plus. Wir haben keine eigenen, ISO 27001 und SOC 2 sind in Prüfung.
- **Große Referenzen und Kapital:** Über 100 Großkunden in über 25 Ländern, etwa Marriott, Caesars, PG&E (laut PolyAI 35.000 Arbeitsstunden gespart), UniCredit und Foot Locker. Über 200 Mio. USD Finanzierung.
- **Einstieg zum Selbermachen:** Kostenlose Anmeldung im Agent Studio, Entwicklungskit (ADK) und Builder MCP seit 2026, Sprachmodell als API je Minute.

## Unterschiede auf einen Blick

| Thema | enneo | PolyAI | Einordnung |
|---|---|---|---|
| **KI-Bearbeitung von E-Mails** | Volle Strecke bis zur Aktion im Zielsystem, auch vollautomatisch. Brief als eigener Kanal | Antworten auf Standardfragen aus der Wissensbasis, Rest als Fall mit Antwortentwurf an ein Postfach. Nur eingehend, Antworten als reiner Text. Brief nicht gefunden | enneo vorn |
| **Mehrere Anliegen in einer Mail** | Alles in einem Durchgang, eine Antwort | Nicht dokumentiert | enneo vorn |
| **Anhänge und Fotos lesen** | PDF und Fotos, z. B. Zählerfoto | PDF, JPEG, PNG, bis 5 Dateien je 5 MB, wenn eingeschaltet | gleich |
| **Arbeitsplatz für Mitarbeitende** | Eigenes Ticketing, Postfach, Telefonie und Skill-Routing | Keiner gefunden, Übergabe an Contact Center, Postfach oder Helpdesk | enneo klar vorn |
| **Fertige Abläufe für Versorger** | Zählerstand, Abschlag, Bankdaten fertig, ERP-Anbindung pro Kunde | Störungen, Zahlungen, Termine, Identifizierung. Zählerstand nicht genannt | enneo vorn |
| **Wo gespeichert wird** | Hetzner, deutscher Anbieter, Betrieb beim Kunden ab großem Volumen | AWS, Regionen US, UK, EU. Land und Betrieb beim Kunden nicht gefunden | enneo vorn |
| **Training mit Kundendaten** | Keine Speicherung, kein Training | Gesprächsausschnitte zum Training, wenn der Kunde es erlaubt | enneo vorn |
| **Voicebot und Sprachmodelle** | Sprache zu Sprache über OpenAI (USA) oder Deepslate (EU) | Eigene Sprach- und Dialogmodelle, 45 Sprachen, bis 10.000 parallele Gespräche | PolyAI klar vorn |
| **Anbindung an fremde Contact Center** | Eigene Telefonie. Ticketnummer im SIP-Header nach außen, eingehend kein Kontext | Über 130 Integrationen, SIP-Übergabe mit eigenen Headern, Handoff-API | PolyAI klar vorn |
| **Qualitätssicherung** | Scorecards, manuell oder automatisch | PolyScore für Telefon, Chat und Mail, seit 10/2026 eigene AI Scores | gleich |
| **Zertifikate** | Keine eigenen, in Prüfung. Hetzner ISO 27001 | ISO 27001, SOC 2 Typ II, PCI DSS, HIPAA, Cyber Essentials Plus | PolyAI klar vorn |
| **Preis** | Paketpreise je Ticket und Sprachminute | Plattform je Minute über den Vertrieb, API 2 Cent je Minute ohne Telefonie | je nach Fall |

## Wo PolyAI schwächer ist

- **E-Mail nur vorgeschaltet:** Laut Doku gehen Beschwerden, Erstattungen und regulierte Anliegen an das Team. Die Antwort kommt als reiner Text, Anhänge kann der Agent nicht senden. Mails, die an der Anhang-Regel scheitern, gehen ohne die Dateien an das Team.
- **Kein eigener Arbeitsplatz:** Wird übergeben, arbeitet das Team in einem anderen System, am Telefon im Contact Center, bei Mail im eigenen Postfach oder Helpdesk.
- **Kaum Bezug zu DACH:** Auf Kunden- und Branchenseiten haben wir keinen Kunden aus Deutschland, Österreich oder der Schweiz gefunden. Die Kunden stammen vor allem aus den USA und Großbritannien.
- **Training und Speicherort:** Der Datenschutzhinweis erlaubt Training mit Gesprächsausschnitten, wenn der Kunde zustimmt. Eine öffentliche Liste der Subunternehmer und ein konkretes Land für die EU-Region haben wir nicht gefunden.

## Einwände

- **„PolyAI kann inzwischen auch E-Mail.“** Stimmt, es gibt inzwischen einen E-Mail-Kanal, der Standardfragen beantwortet und den Rest mit Entwurf weitergibt. Fragen Sie, ob er einen Zählerstand oder eine neue IBAN auch im Zielsystem bucht. Bei uns ist genau das die Kernstrecke, auch mit mehreren Anliegen in einer Mail.
- **„PolyAI ist größer und hat Kunden wie Marriott und PG&E.“** Am Telefon und beim Kapital stimmt das. Kunden aus DACH haben wir bei PolyAI nicht gefunden, und für Ihr Team brauchen Sie dort ein zweites System. Bei uns laufen Telefon, Mail und Arbeitsplatz in einem Produkt.
- **„PolyAI kostet nur 2 Cent pro Minute.“** Das ist der Preis für das Sprachmodell per API, ohne Telefonie. Die Plattform mit Integrationen und Betreuung wird je Minute über den Vertrieb verhandelt. Lassen Sie uns die Gesamtkosten vergleichen, inklusive System für Schriftverkehr und Arbeitsplatz.

## Fragen an den Kunden

- **Was soll mit einer Mail passieren, in der Zählerstand, neue IBAN und neuer Abschlag stehen?** Erwartete Antwort: alles soll im Abrechnungssystem landen. Überleitung: „Das erledigt unsere KI in einem Durchgang bis zur Buchung, bei PolyAI ist dazu nichts dokumentiert.“
- **In welchem System arbeitet Ihr Team, wenn PolyAI übergibt?** Erwartete Antwort: im vorhandenen Contact Center oder Helpdesk, der eigens lizenziert wird. Überleitung: „Bei uns ist der Arbeitsplatz Teil des Produkts, mit Postfach, Telefonie und Skill-Routing.“
- **Haben Sie von PolyAI eine Referenz aus Deutschland und eine Zusage, wo genau Ihre Daten liegen und ob damit trainiert wird?** Erwartete Antwort: noch nicht. Überleitung: „Wir speichern bei Hetzner in Deutschland, trainieren nicht mit Ihren Daten, und unsere AVV und TOM sind öffentlich.“

## Intern

Bisher keine internen Erkenntnisse in Attio (Stand 05.11.2026).

## Fazit

Gegen PolyAI gewinnen wir nicht am Telefon, bei Zertifikaten oder bei der Anbindung an große Contact Center. Gewinnen können wir, wo viel Schriftverkehr mit echten Vorgängen anfällt und der Kunde alles in einem System will: Buchung im Zielsystem, mehrere Anliegen in einer Mail, Arbeitsplatz für das Team, gespeichert bei einem deutschen Anbieter. In DACH tritt PolyAI bisher ohne sichtbare Referenzen auf.

## Quellen

- [Startseite](https://poly.ai)
- [Über PolyAI](https://poly.ai/about)
- [Series D](https://poly.ai/blog/polyai-raises-86m-to-transform-how-enterprises-talk-to-their-customers)
- [Preise](https://poly.ai/pricing)
- [Sicherheit](https://poly.ai/security)
- [Zertifikate](https://docs.poly.ai/legal/compliance)
- [Datenschutzhinweis](https://poly.ai/privacy-policy)
- [API und Regionen](https://docs.poly.ai/api-reference/introduction)
- [Plattform](https://docs.poly.ai/platform/introduction)
- [E-Mail-Kanal](https://docs.poly.ai/messaging-channel/email/email)
- [E-Mail-Übergabe](https://docs.poly.ai/messaging-channel/email/handoff)
- [Übergabe am Telefon](https://docs.poly.ai/voice-channel/handoffs)
- [Integrationen](https://poly.ai/integrations)
- [Sprachen](https://poly.ai/languages)
- [Kunden](https://poly.ai/customers)
- [Versorger](https://poly.ai/industries/utilities)
- [Release Notes 10/2026](https://docs.poly.ai/releases/notes/26.10)
- [enneo Lösungsplan](https://docs.enneo.ai/en/ai-functions-agents/intent-lifecycle#smart-agent-v2)
