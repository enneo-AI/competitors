---
slug: "polyai"
stand: "2026-11-05"
kurz: "Voice AI agents from London with proprietary speech models"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **London, approx. 250 employees** | PolyAI Ltd, founded in 2017 by researchers from Cambridge. Offices in London, New York, San Mateo, Belgrade, Toronto. Series D 12/2025: USD 86m, led by Georgian, Hedosophia, Khosla Ventures, plus NVentures (NVIDIA) and Zendesk Ventures. Over USD 200m in total |
| Preise | **Platform not public** | Enterprise platform per connected minute, rate only through sales. Self-serve API for the Dialog-RSN-1 speech model: 2 cents per minute plus text tokens, telephony not included |
| Hosting | **AWS, regions US/UK/EU** | According to the docs, three regions (US, UK, EU). We found no specific country within the EU and no on-premises option |
| Zertifikat | **ISO 27001, SOC 2** | SOC 2 Type II, plus PCI DSS, HIPAA, Cyber Essentials Plus. C5 not found |

## Erster Satz

"PolyAI has strong technology on the phone with its own speech models. The question is who handles the emails with real cases for you, and which system your team works in."

## Das Wichtigste vorweg

PolyAI builds AI agents mainly for the phone, with its own speech and dialog models, a lot of capital and large customers in the US and UK, such as PG&E, Marriott and UniCredit. It now also has an email channel, but according to the docs it answers standard questions from the knowledge base and hands the rest, with a draft reply, to a customer inbox. We found no agent workspace of its own and no references in DACH. On the phone, PolyAI leads. On written correspondence with actions in the target system, and on everything in one system, we lead.

## Unsere Verkaufsargumente

- **Email through to the action in the target system:** enneo reads the email, detects requests and the customer, verifies identity, posts in the ERP and replies, fully automated if desired. At PolyAI, according to the docs, the email agent answers questions from the knowledge base, while complaints, refunds and regulated requests go to the team. Posting in the target system via email is not documented there.
- **Multiple requests, one reply:** Meter reading, new IBAN and new installment in one email: enneo handles all of it in one pass with one reply. PolyAI has documented nothing on this.
- **One system instead of two:** At enneo, agent workspace, inbox, AI agents, knowledge and telephony are one product with skill-based routing. PolyAI hands calls via SIP to a third-party contact center and emails as a case to an inbox or a helpdesk such as Zendesk or Salesforce. So the customer needs a second system.
- **Ready-made flows for utilities:** enneo ships meter reading, installment and bank details as ready-made AI agents with plausibility checks, only the ERP integration is built per customer. For utilities, PolyAI names outages, payments, appointments and identification, but not meter readings.
- **Stored with a German provider, no training:** enneo stores data at Hetzner in Germany and does not train on customer data. PolyAI runs on AWS and, according to its privacy notice, may use conversation snippets for training with the customer's permission.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Email through to the action in the target system** | Cases that require posting are also handled automatically, fewer agents needed for written correspondence | "PolyAI answers standard questions by email. With us, the AI posts the case in the target system and replies." |
| **Multiple requests in one pass** | One complete reply instead of follow-up questions and emails | "Meter reading, IBAN and installment in one email: we handle it in one pass with one reply." |
| **One system instead of two** | No second system and no second contract for the team, the case lives in one place | "At PolyAI, the case lands in another system. With us, AI and team work in the same agent workspace." |
| **Ready-made flows for utilities** | Productive faster on meter reading, installment and bank details, only the ERP integration is built | "We ship the most important utility flows ready-made, with plausibility checks." |
| **Storage in Germany, no training** | Simpler privacy review, no approval needed for training on customer data | "We store data at Hetzner in Germany and don't train on your data." |

## Wo PolyAI vorn liegt

- **Phone and proprietary speech models:** Own models for speech (Dialog-RSN-1) and dialog (Raven), according to PolyAI under 300 ms response time, up to 10,000 concurrent calls and 99.994% uptime. Over 2,000 deployments in 45 languages, German included. Our voicebot runs via OpenAI or Deepslate, with less choice.
- **Integration with third-party contact centers:** According to PolyAI, over 130 integrations, including Genesys, Five9, NICE, Avaya, Cisco, Amazon Connect, Talkdesk, Twilio, plus Salesforce, Dynamics, ServiceNow, HubSpot and MCP. Phone handover via SIP REFER or INVITE with custom SIP headers, context via the Handoff API. We only pass the ticket number outbound in the SIP header and read no context inbound.
- **Certifications:** ISO 27001, SOC 2 Type II, PCI DSS, HIPAA, Cyber Essentials Plus. We have none of our own, ISO 27001 and SOC 2 are in progress.
- **Large references and capital:** Over 100 enterprise customers in more than 25 countries, such as Marriott, Caesars, PG&E (35,000 labor hours saved according to PolyAI), UniCredit and Foot Locker. Over USD 200m in funding.
- **Self-serve entry:** Free sign-up in Agent Studio, a development kit (ADK) and Builder MCP since 2026, speech model as an API priced per minute.

## Unterschiede auf einen Blick

| Topic | enneo | PolyAI | Assessment |
|---|---|---|---|
| **AI handling of emails** | Full flow through to the action in the target system, fully automated if desired. Letter as its own channel | Answers standard questions from the knowledge base, the rest goes as a case with a draft reply to an inbox. Inbound only, replies in plain text. Letter not found | enneo vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Reading attachments and photos** | PDF and photos, e.g. meter photo | PDF, JPEG, PNG, up to 5 files of 5 MB each, when enabled | gleich |
| **Agent workspace** | Own ticketing, inbox, telephony and skill-based routing | None found, handover to contact center, inbox or helpdesk | enneo klar vorn |
| **Ready-made flows for utilities** | Meter reading, installment, bank details ready-made, ERP integration per customer | Outages, payments, appointments, identification. Meter reading not mentioned | enneo vorn |
| **Where data is stored** | Hetzner, German provider, on-premises at large volumes | AWS, regions US, UK, EU. Country and on-premises option not found | enneo vorn |
| **Training on customer data** | No storage, no training | Conversation snippets used for training if the customer permits | enneo vorn |
| **Voicebot and speech models** | Speech-to-speech via OpenAI (USA) or Deepslate (EU) | Own speech and dialog models, 45 languages, up to 10,000 concurrent calls | PolyAI klar vorn |
| **Integration with third-party contact centers** | Own telephony. Ticket number outbound in the SIP header, no context inbound | Over 130 integrations, SIP handover with custom headers, Handoff API | PolyAI klar vorn |
| **Quality assurance** | Scorecards, manual or automatic | PolyScore for phone, chat and email, custom AI Scores since 10/2026 | gleich |
| **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001, SOC 2 Type II, PCI DSS, HIPAA, Cyber Essentials Plus | PolyAI klar vorn |
| **Price** | Package prices per ticket and voice minute | Platform per minute through sales, API 2 cents per minute without telephony | je nach Fall |

## Wo PolyAI schwächer ist

- **Email only as a front layer:** According to the docs, complaints, refunds and regulated requests go to the team. The reply is plain text, and the agent cannot send attachments. Emails that fail the attachment rules go to the team without the files.
- **No agent workspace of its own:** On handover, the team works in another system: the contact center for calls, its own inbox or helpdesk for email.
- **Little DACH presence:** On the customer and industry pages, we found no customer from Germany, Austria or Switzerland. Customers come mainly from the US and UK.
- **Training and storage location:** The privacy notice allows training on conversation snippets if the customer consents. We found no public subprocessor list and no specific country for the EU region.

## Einwände

- **"PolyAI can do email now too."** True, there is now an email channel that answers standard questions and passes the rest on with a draft. Ask whether it also posts a meter reading or a new IBAN in the target system. For us, that is exactly the core flow, even with multiple requests in one email.
- **"PolyAI is bigger and has customers like Marriott and PG&E."** On the phone and in capital, that's true. We found no DACH customers at PolyAI, and your team would need a second system there. With us, phone, email and agent workspace run in one product.
- **"PolyAI only costs 2 cents per minute."** That is the price for the speech model via API, without telephony. The platform with integrations and support is negotiated per minute through sales. Let's compare total costs, including the system for written correspondence and the agent workspace.

## Fragen an den Kunden

- **What should happen to an email containing a meter reading, a new IBAN and a new installment?** Expected answer: everything should end up in the billing system. Transition: "Our AI handles that in one pass through to posting. PolyAI has documented nothing on this."
- **Which system does your team work in when PolyAI hands over?** Expected answer: the existing contact center or helpdesk, licensed separately. Transition: "With us, the agent workspace is part of the product, with inbox, telephony and skill-based routing."
- **Do you have a reference from Germany from PolyAI, and a commitment on exactly where your data is stored and whether it is used for training?** Expected answer: not yet. Transition: "We store data at Hetzner in Germany, we don't train on your data, and our DPA and TOMs are public."

## Intern

No internal insights in Attio yet (as of Nov 5, 2026).

## Fazit

Against PolyAI, we don't win on the phone, on certifications or on integration with large contact centers. We can win where there is a lot of written correspondence with real cases and the customer wants everything in one system: posting in the target system, multiple requests in one email, an agent workspace for the team, data stored with a German provider. In DACH, PolyAI has so far appeared without visible references.

## Quellen

- [Homepage](https://poly.ai)
- [About PolyAI](https://poly.ai/about)
- [Series D](https://poly.ai/blog/polyai-raises-86m-to-transform-how-enterprises-talk-to-their-customers)
- [Pricing](https://poly.ai/pricing)
- [Security](https://poly.ai/security)
- [Certifications](https://docs.poly.ai/legal/compliance)
- [Privacy notice](https://poly.ai/privacy-policy)
- [API and regions](https://docs.poly.ai/api-reference/introduction)
- [Platform](https://docs.poly.ai/platform/introduction)
- [Email channel](https://docs.poly.ai/messaging-channel/email/email)
- [Email handoff](https://docs.poly.ai/messaging-channel/email/handoff)
- [Phone handoff](https://docs.poly.ai/voice-channel/handoffs)
- [Integrations](https://poly.ai/integrations)
- [Languages](https://poly.ai/languages)
- [Customers](https://poly.ai/customers)
- [Utilities](https://poly.ai/industries/utilities)
- [Release notes 10/2026](https://docs.poly.ai/releases/notes/26.10)
- [enneo solution plan](https://docs.enneo.ai/en/ai-functions-agents/intent-lifecycle#smart-agent-v2)
