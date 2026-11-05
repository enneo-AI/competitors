# enneo-Fakten für Battle Cards (Stand 05.11.2026)

Nur diese Aussagen über enneo verwenden. Nichts über enneo hinzuerfinden. Wenn ein Vergleichsthema hier nicht abgedeckt ist, das Thema weglassen.

## Firma und Betrieb
- Deutsche GmbH aus Berlin, keine Investoren.
- Speicherung bei Hetzner (deutscher Anbieter), Rechenzentren in Deutschland, Backups in Deutschland und Finnland.
- Betrieb beim Kunden (eigenes Rechenzentrum) ab großem Volumen möglich.
- Zertifikate: keine eigenen, ISO 27001 und SOC 2 in Prüfung. Hetzner ist ISO 27001 zertifiziert.
- AVV, TOM, Subunternehmer und SLA sind öffentlich einsehbar.
- Preis: Paketpreise je Ticket und Sprachminute (Preismodell 2.2). Keine konkreten Preise nennen.

## Produkt
- Ein Produkt: Ticketing-Arbeitsplatz, Postfach, KI-Agenten, Wissen, Telefonie und Voicebot in einem System, mit Skill-Routing.
- Kanäle: E-Mail, Brief (eigener Kanal, Scans per Mail oder API, gleiche KI wie E-Mail), Chat, WhatsApp, Telegram, Telefon.
- KI-Bearbeitung von E-Mails, volle Strecke: Eingang, Anliegen erkennen, Kunde erkennen und legitimieren, Aktion im ERP/Zielsystem, Antwort, auch vollautomatisch (Dunkelverarbeitung).
- Mehrere Anliegen in einer Mail: ein Lösungsplan für das ganze Ticket, alle Anliegen in einem Durchgang, eine Antwort, auch vollautomatisch (seit Release 2.34, Oktober 2026).
- Anhänge und Fotos lesen: PDF und Fotos, z. B. Zählerfoto.
- Kundenerkennung: Rahmen fertig (Nummer aus der Mail, Suchreihenfolge, Legitimationsregeln, Kunde am Ticket). Die Suche im ERP wird pro Kunde gebaut.
- Fertige Fachagenten für Energieversorger: Zählerstand, Abschlag, Bankdaten u. a. mit Plausibilitätsprüfung. Die ERP-Anbindung wird pro Kunde gebaut.
- KI-Agenten in normaler Sprache beschreiben statt Prozessmodell, mit Neo per Chat ändern, Testfälle.
- Schnittstellen als Code, jedes Format, beliebige Logik. API und MCP.
- Altsysteme ohne Schnittstelle: RPA-Bot mit Neo.
- Mehrere Postfächer oder Marken: je Postfach ein eigener KI-Agent mit eigener Anrede und eigenem Wissen.
- Begründung der KI nachvollziehbar: Lösungsplan, erkannte Werte, Vorschau ohne Buchung.
- Agent Assist: Entwurf, Zusammenfassung, Live-Transkription.
- Qualitätssicherung: Scorecards, manuell oder automatisch.
- Sprachmodelle: US-Anbieter Standard, EU-Modelle im AVV möglich (Mistral, Nebius, Media Trooper). Keine Speicherung, kein Training mit Kundendaten.
- Voicebot: eigene Telefonie oder SIP-Leitung des Kunden. Sprache zu Sprache über OpenAI (USA) oder Deepslate (EU). Weniger Auswahl an Sprachanbietern als große Contact-Center-Plattformen.

## Ehrliche Lücken von enneo (nicht verschweigen, wenn der Wettbewerber dort stark ist)
- Kein Workforce Management, kein Live-Dashboard für Contact-Center-Steuerung, kein Dialer für Outbound-Kampagnen.
- Kein Hilfecenter für Endkunden.
- Keine Signatur- oder Ausweisprüfung.
- MS Teams: keine native Anbindung, Telefonie nur per SIP.
- Übergabe an Fremd-Bots: Ticketnummer im SIP-Header nach außen, eingehend kein Kontext aus SIP-Headern.
- Weniger Zertifikate als große Anbieter (siehe oben).
- Kleineres Ökosystem an fertigen Konnektoren.
