---
slug: "genesys"
stand: "2026-11-05"
kurz: "Large US contact center, strong on the phone"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Menlo Park, private** | Genesys, more than 8,000 customers worldwide. Majority owned by Hellman & Friedman and Permira, Salesforce and ServiceNow holding stakes worth USD 1.5bn combined (announced 07/2025) |
| Preise | **USD 75 to 240** | per user per month on an annual contract, packages CX 1 to CX 4. Some AI features cost "Experience Units", only CX 4 includes 30 per agent |
| Hosting | **AWS Frankfurt and others** | Plus Dublin, London, Zurich. "European Sovereign Region" in Brandenburg only available with restrictions, email and SMS excluded there |
| Zertifikat | **ISO 27001, C5** | Plus ISO 27017, 27018, 42001, SOC 1 and 2, PCI DSS. C5 applies to EMEA |

## Erster Satz

"Genesys is one of the strongest platforms on the market for the phone. The question is who handles your written correspondence automatically, all the way to the booking."

## Das Wichtigste vorweg

Genesys is one of the largest contact centers in the world and much broader than we are in telephony, routing, dialer, workforce management, quality and voicebot. For email, Genesys now uses AI to recognize the request from the email text, after which a fixed flow with rules and a prewritten reply runs. We did not find an AI agent that handles an email on its own all the way to the booking. That is where our advantage lies. On the phone, Genesys is ahead.

## Unsere Verkaufsargumente

- **Email AI across the full journey:** With enneo, the AI reads the email, identifies and verifies the customer, books in the ERP and replies, fully automated if desired. With Genesys, the AI recognizes a request, and the rest is built as a fixed flow with rules, data lookup and auto-reply. Genesys only announced an AI summary of emails in Copilot on Aug 24, 2026.
- **Multiple requests and attachments:** enneo handles a meter reading, a new IBAN and a new installment in one email in a single pass with one reply. enneo also reads PDFs and photos, e.g. a photo of the meter. For Genesys, nothing is documented on either for email.
- **For utilities in addition:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. Genesys mentions meter readings by email only as an example, and the customer builds the flow themselves.
- **Stored with a German provider, also on-premises:** enneo stores data at Hetzner, and on-premises for large volumes. Genesys runs on AWS, and the sovereign EU region does not apply to email. Genesys Engage On-Premise ends on Dec 31, 2028, so existing customers have to switch anyway.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **AI agent for email all the way to the booking** | Written correspondence gets resolved without building every flow as a fixed rule, fewer agents needed for inboxes | "With us, the AI handles the email all the way to the booking. You don't build a fixed flow for every request." |
| **Multiple requests and attachments** | Fewer repeat contacts, nobody has to retype meter photos and PDFs | "enneo handles a meter reading, a new IBAN and a meter photo in one email in a single pass with one reply." |
| **Ready-made workflows for utilities** | Shorter rollout, no in-house build of the business workflows | "Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo." |
| **Storage in Germany, also on-premises** | Simpler data protection review, no forced switch like with the end of Engage On-Premise | "We store data at Hetzner in Germany, and for large volumes also in your data center." |
| **Package prices instead of consumption units** | AI costs can be planned in advance | "With us, you calculate in packages per ticket and voice minute, not in consumption units." |

## Wo Genesys vorn liegt

- **Contact center in full breadth:** Dialer and campaigns in all packages, quality assurance from CX 2, workforce management with forecasting from CX 3, speech and text analytics, Copilot for agents and team leads. We don't have that to this extent.
- **Voicebot and speech services:** Speech recognition from Genesys, Google, Microsoft, Amazon and Deepgram, with your own Azure, Google or Nuance accounts pluggable. Since February 2026, an "Agentic Virtual Agent" that is meant to resolve requests across multiple systems on its own. With Deepslate we have an EU voicebot, but fewer options.
- **Third-party bots and Teams:** Up to five third-party bots via the Bot Connector, and Cognigy is listed as a premium app on AppFoundry. Microsoft Teams via Direct Routing, Teams presence in Genesys and the Genesys workspace directly in Teams. We connect Teams only via SIP.
- **Certifications:** ISO 27001, 27017, 27018, 42001, SOC 1 and 2, PCI DSS and C5. We have none of our own.
- **References in DACH:** The energy service provider HanseWerk Natur (Hamburg, 200 employees) with T-Systems MMS as partner. The Konzern Versicherungskammer via Mitel, where virtual agents and Copilot are only planned so far.

## Unterschiede auf einen Blick

| Topic | enneo | Genesys | Assessment |
|---|---|---|---|
| **AI handling of emails** | One AI reads, identifies the customer, books and replies, fully automated if desired | AI recognizes the request, then a fixed flow with rules, data lookup and auto-reply. No AI agent for emails found | enneo klar vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Reading attachments and photos** | PDFs and photos, e.g. a photo of the meter | Not documented for email | enneo vorn |
| **Ready-made workflows for utilities** | Meter reading, installment, bank details ready, ERP integration per customer | Meter reading by email mentioned as an example, the customer builds the flow | enneo vorn |
| **Where data is stored** | Hetzner, German provider, on-premises possible | AWS Frankfurt and others, sovereign region restricted and without email. On-premise ends in 2028 | enneo vorn |
| **Agent Assist** | Draft, summary, live transcription | Agent Copilot in all packages, email summary only announced | je nach Fall |
| **Voicebot and speech services** | OpenAI (US) or Deepslate (EU), fewer options | Six speech recognition engines, own accounts pluggable, Agentic Virtual Agent | Genesys klar vorn |
| **Handoff to third-party bots** | Ticket number in the SIP header outbound, no context inbound | Up to five third-party bots, Cognigy as a premium app | Genesys klar vorn |
| **Workforce management, dialer, quality** | No WFM, no dialer, no live dashboard, scorecards | Dialer in all packages, QA from CX 2, WFM from CX 3 | Genesys klar vorn |
| **Microsoft Teams** | No native integration, SIP only | Direct Routing, presence sync, workspace in Teams | Genesys klar vorn |
| **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001, 27017, 27018, 42001, SOC 1 and 2, PCI DSS, C5 | Genesys klar vorn |
| **Price** | Package prices per ticket and voice minute (pricing model 2.2) | USD 75 to 240 per user per month, AI partly via Experience Units | je nach Fall |

## Wo Genesys schwächer ist

- **Email AI arrives in small steps:** AI recognition for emails was announced in April 2025, and the announcement still says "in a future release". The documentation now describes it, and it requires an AI Experience license and consumes tokens. The email summary in Copilot has only been announced since Aug 24, 2026.
- **Sovereignty with gaps:** The EU region with EU staff is only available with restrictions. Email, SMS and third-party messengers run outside it even there. The company is based in the US.
- **On-premise is being phased out:** Maintenance and support for Genesys Engage On-Premise end on Dec 31, 2028. Anyone who wants to stay in their own data center will find no way to do so with Genesys.
- **AI costs hard to plan:** Some AI features require Experience Units, and Genesys notes "Usage-based pricing may apply". Only CX 4 includes a fixed allowance.

## Einwände

- **"Genesys is the market leader, and we just renewed."** Genesys is strong for telephony, workforce management and dialer, and we don't want to replace that. enneo comes in on written correspondence: emails and letters all the way to the booking, alongside Genesys, and with its own telephony if wanted later.
- **"But Genesys can do email and AI too."** Genesys uses AI to recognize the request, after which a fixed flow with rules and a prewritten reply runs. Ask whether the written correspondence module really meets your requirements and whether you use it today. With enneo, an AI agent handles the email all the way to the booking, with multiple requests and attachments.
- **"Genesys has every certification, including C5."** Genesys is ahead on certifications, and we say so openly. We store data at Hetzner in Germany, Hetzner is ISO 27001 certified, our own certifications are in progress, and the DPA, TOMs and SLA are public. At Genesys, the sovereign EU region does not apply to email.

## Fragen an den Kunden

- **Which parts of the Genesys package do you really use today, for example for email?** Expected answer: telephony and reporting yes, written correspondence often not, or through another system. Transition: "enneo is built for written correspondence, all the way to the booking in the billing system."
- **Where are your emails stored with Genesys, and is that enough for your data protection team?** Expected answer: in an AWS region, the sovereign EU region does not apply to email, and the company is based in the US. Transition: "With us, the data stays at Hetzner in Germany, and for large volumes also on your premises."
- **How do you plan the costs for AI features with Genesys?** Expected answer: hard to predict, some AI features consume Experience Units, and only CX 4 includes a fixed allowance. Transition: "With us, there are package prices per ticket and voice minute."

## Intern

- **Telephony yes, their own bots no:** An existing customer (utility, enterprise account) is happy with Genesys as a phone system and for reporting and recently renewed the contract for two years. He used to use the Genesys bots, was not satisfied with their performance in mid-2025 and switched to a voicebot specialist. *Attio call, Oct 16, 2026, min. 2:55, 5:36 and 20:32*
- **Written correspondence module paid for but not used:** According to the same customer, Genesys itself said of his requirements for written correspondence "we can't do that at all". The module is part of the package and is paid for regardless. Genesys's focus is on telephony, and written channels only come bit by bit. *Attio call, Oct 16, 2026, min. 47:13, 48:16 and 52:06*
- **Modular kit with extra costs:** The same customer describes Genesys as a modular kit that has to be booked in full. Ad hoc call recording was at times sold separately, and today it is included in the package. *Attio call, Oct 16, 2026, min. 9:25 and 49:36*
- **Announced features delayed:** According to the same customer, new features often arrived later than announced, and one release was postponed twice without a reliable date. *Attio call, Oct 16, 2026, min. 53:04*
- **Support and decisions in the US:** A German technical contact is helpful, but deep technical questions go through an English-language ticket portal and "take more explaining". Decisions are made in the US, and requests from German customers count for little there. *Attio call, Oct 16, 2026, min. 56:00 and 57:55*
- **Phone system without intelligence:** A customer (education provider, many locations) describes their Genesys setup as a large phone system that routes by fixed tiers but contains "no intelligence whatsoever". Another existing customer (utility) runs Genesys alongside separate solutions per channel and rebuilds logic for each channel. *Attio call, Jun 12, 2026, min. 38:22, and Attio call, Oct 27, 2026, min. 35:09*

## Fazit

Against Genesys, we don't win on telephony, voicebot, workforce management, Teams or certifications. We can win where a lot of written correspondence should be handled automatically all the way to the booking, with multiple requests, attachments and energy workflows, and where data should be stored with a German provider or in the customer's own data center. Where Genesys is already in place as the contact center, enneo for email and letters alongside it is often the better conversation than a complete switch.

## Quellen

- [Pricing](https://www.genesys.com/pricing)
- [Security standards](https://help.genesys.cloud/articles/supported-security-standards/)
- [AWS regions](https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/)
- [European Sovereign Region](https://help.genesys.cloud/articles/european-sovereign-region/)
- [Email at Genesys](https://help.genesys.cloud/articles/about-email/)
- [Flow for inbound emails](https://help.genesys.cloud/articles/inbound-email-flows/)
- [Detecting intents](https://help.genesys.cloud/articles/detect-intent-action/)
- [AI intents for emails, license](https://help.genesys.cloud/articles/generate-ai-powered-intents-based-on-description-for-an-inbound-email-flow/)
- [Announcement AI for email (04/2025)](https://help.genesys.cloud/announcements/ai-powered-email-routing-and-responses/)
- [Announcement Copilot for email (08/2026)](https://help.genesys.cloud/announcements/genesys-cloud/427451/)
- [Copilot email summary](https://help.genesys.cloud/articles/configure-agent-copilot-email-summaries/)
- [Genesys Virtual Agent](https://help.genesys.cloud/articles/about-genesys-virtual-agent/)
- [Agentic Virtual Agent (02/2026)](https://www.genesys.com/company/newsroom/announcements/genesys-unveils-industrys-first-agentic-virtual-agent-powered-by-lams-for-enterprise-cx)
- [Speech recognition](https://help.genesys.cloud/articles/speech-to-text-stt-engines-overview/)
- [Bot Connector](https://help.genesys.cloud/articles/about-genesys-bot-connector/)
- [Cognigy on AppFoundry](https://www.cognigy.com/news/cognigy.ai-conversational-ai-platform-now-available-on-genesys-appfoundry)
- [Microsoft Teams](https://help.genesys.cloud/articles/configure-the-microsoft-teams-integration/)
- [End of Engage On-Premise](https://cxfoundation.com/blog/genesys-engage-end-of-life)
- [Salesforce and ServiceNow investment](https://www.intelligentcio.com/north-america/2025/08/01/genesys-secures-1-5-billion-investment-from-salesforce-and-servicenow-to-boost-ai-powered-cx-orchestration/)
- [HanseWerk Natur](https://www.genesys.com/de-de/customer-stories/hansewerk-natur)
- [Konzern Versicherungskammer](https://www.mitel.com/de-de/mehr-erfahren/kundenreferenzen/konzern-versicherungskammer)
- [enneo solution plan](https://docs.enneo.ai/en/ai-functions-agents/intent-lifecycle#smart-agent-v2)
