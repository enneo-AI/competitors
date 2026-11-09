---
slug: "salesforce"
stand: "2026-11-09"
kurz: "US CRM platform, Service Cloud with AI agents from Agentforce"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **San Francisco, USA** | Salesforce, Inc. Acquiring Fin (formerly Intercom) for around USD 3.6bn, closing expected in Q4 of fiscal year 2027 |
| Gegründet | **1999, San Francisco** | Founded in 1999 by Marc Benioff, today Chair, CEO and co-founder |
| Ursprung | **Cloud CRM since 1999** | Started with CRM software from the cloud. AI predictions in the CRM since 2016, AI agents with Agentforce since 2024 |
| Preise | **Core €195 + AI** | Service Core €195, Advanced €395, Max €550 per user per month, for small teams Starter Suite from €25 and Pro Suite from €100. Agentforce: €2 per conversation or Flex Credits at €500 per 100,000 (one action is 20 credits, so €0.10), add-on €125 per user |
| Hosting | **Hyperforce, Germany region** | Hyperforce on AWS, Germany region selectable, EU Operating Zone with EU support costs extra. Third-party language models with zero retention |
| Zertifikat | **ISO 27001, C5** | For Agentforce: ISO 27001, 27017, 27018 (as of Oct 30, 2026) and C5 report (July 2026) |

## Erster Satz

"Salesforce is a very broad platform. It gets interesting where emails have attachments, photos or multiple requests, and where the data should be stored with a German provider."

## Das Wichtigste vorweg

Salesforce is the broadest platform in this comparison: CRM, service, sales, field service, Slack and its own agent platform, Agentforce. The Agentforce Service Agent answers emails on its own, but according to Salesforce's own docs it only reads the subject and email body, no images or attachments. For phone, chat, SMS and WhatsApp, the ready-made agent "Casey" has been available since September 2026, and with Fin, Salesforce is buying a second AI agent. Prices are public, but costs are made up of license plus AI usage.

## Unsere Verkaufsargumente

- **Attachments and photos:** enneo reads PDFs and photos along with the email, for example the meter photo. According to the docs, Salesforce's Service Agent only processes text from the subject and email, no images and no attachments.
- **Multiple requests, one reply:** Meter reading, new IBAN and new installment in one email: enneo handles all of it in one pass with one reply. At Salesforce, this is not documented for email.
- **Control before sending:** At enneo, the resolution plan shows detected values and a preview without posting. According to the docs, the Salesforce agent always sends a reply, except on handover to a human or on error. Instructions not to send a reply are not supported.
- **Ready-made processes for utilities:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo, and we build the ERP connection per customer. Salesforce's industry page mentions meter reading via chat and billing inquiries, but no billing system.
- **Stored with a German provider:** enneo stores data at Hetzner, on-premises if desired. Salesforce stores data on Hyperforce at AWS, and the company is based in the USA. For both, the language models come from US providers.

## Business-Impact

| With enneo | Outcome for the customer | How to say it |
|---|---|---|
| **Reads attachments and photos too** | Emails with a meter photo or PDF are handled automatically instead of landing with agents, less manual work | "According to its documentation, the Salesforce agent only reads the subject and email text. We also read the meter photo and the PDF." |
| **All requests, one reply** | Fewer follow-up questions and emails, one case instead of several | "Meter reading, new IBAN and new installment in one email: we handle them in one pass with one reply." |
| **Resolution plan and preview before sending** | Lower risk of wrong replies, the business team sees in advance what will happen | "With us, you see the resolution plan, the detected values and a preview without booking. According to its documentation, the Salesforce agent always replies." |
| **Ready-made specialist agents for utilities** | Faster start for meter reading, installment and bank details, only the ERP integration is built | "Meter reading, installment and bank details are ready-made agents with plausibility checks at enneo." |
| **German GmbH, storage in Germany** | Data protection review without questions about a US company, no surcharge for a special EU zone | "We're a German GmbH and store data at Hetzner. At Salesforce, the EU Operating Zone costs extra." |

## Wo Salesforce vorn liegt

- **Platform and channels:** Service, sales, field service, marketing and Slack from a single source. Casey covers phone, SMS, WhatsApp and web chat, plus a self-service help center from the Core edition upward.
- **Voicebot from the same toolkit:** Agentforce Voice uses the same agents, actions and data as chat, speaks German among other languages and hands over to humans with the full history.
- **Certifications:** ISO 27001, 27017, 27018 and C5 for Agentforce. We have none of our own.
- **Public pricing and purchase models:** Licenses, conversations and credits are listed on the website. Purchase up front, with a minimum commitment or by usage.
- **Ready-made agents and Fin:** Seven ready-made agents since Sep 11, 2026. Fin adds an agent for chat, email, WhatsApp, SMS and phone, with an average of 76% of requests resolved and over 30,000 customers according to Salesforce.

## Unterschiede auf einen Blick

| Area | Topic | enneo | Salesforce | Assessment |
|---|---|---|---|---|
| Kanäle | **Channels** | Email, letter, chat, WhatsApp, Telegram, phone | Email, phone, SMS, WhatsApp, web chat, Slack, portals [Email agent](https://help.salesforce.com/s/articleView?id=ai.agent_email_parent.htm&type=5) [Ready-made agents](https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/) [Fin acquisition](https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/) | Salesforce vorn |
| Kanäle | **Voicebot** | Own telephony or SIP, OpenAI (USA) or Deepslate (EU) | Agentforce Voice, same agents as in chat, German, 30 credits per action [Voice](https://www.salesforce.com/agentforce/voice/) [Agentforce pricing](https://www.salesforce.com/de/agentforce/pricing/) | je nach Fall |
| Kanäle | **Help center for end customers** | None | Self-service help center from Core [Service pricing](https://www.salesforce.com/de/service/pricing/) | Salesforce klar vorn |
| KI & Automatisierung | **AI handling of emails** | One AI reads, identifies and verifies the customer, books and replies, fully automated if desired | Service Agent replies autonomously to cases from Email-to-Case, identity verification on email not supported according to the documentation [Email agent](https://help.salesforce.com/s/articleView?id=ai.agent_email_parent.htm&type=5) | enneo vorn |
| KI & Automatisierung | **Reading attachments and photos** | PDFs and photos, e.g. meter photo | Email agent only reads subject and email text, no images or attachments [Email limits](https://help.salesforce.com/s/articleView?id=ai.service_agent_considerations_1.htm&type=5) | enneo klar vorn |
| KI & Automatisierung | **Multiple requests in one email** | Everything in one pass, one reply | Not documented for email [Email agent](https://help.salesforce.com/s/articleView?id=ai.agent_email_parent.htm&type=5) [Email limits](https://help.salesforce.com/s/articleView?id=ai.service_agent_considerations_1.htm&type=5) | enneo vorn |
| KI & Automatisierung | **Reasoning and preview** | Resolution plan, detected values, preview without booking | Agent always replies, instructions not to reply are not supported [Email limits](https://help.salesforce.com/s/articleView?id=ai.service_agent_considerations_1.htm&type=5) | enneo vorn |
| KI & Automatisierung | **Ready-made workflows for utilities** | Meter reading, installment, bank details ready, ERP integration per customer | Industry package with meter reading via chat and billing inquiries, billing systems not named [Agentforce energy](https://www.salesforce.com/de/energy-utilities/artificial-intelligence/) | enneo vorn |
| Arbeitsplatz & Anbindungen | **Ecosystem** | API, MCP, code tools per customer | CRM platform with Slack and industry packages such as the Energy & Utilities Cloud [Our story](https://www.salesforce.com/company/our-story/) [Energy pricing](https://www.salesforce.com/de/energy-utilities/cloud/pricing/) | Salesforce klar vorn |
| Daten & Sicherheit | **Where data is stored** | Hetzner, German provider, on-premises possible | Hyperforce on AWS, Germany region, EU Operating Zone at extra cost [Hyperforce EU](https://www.salesforce.com/eu/hyperforce/) [Subprocessors](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf) | enneo vorn |
| Daten & Sicherheit | **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001, 27017, 27018, C5 for Agentforce [Compliance](https://compliance.salesforce.com/en/services/agentforce-einstein-platform) [C5 reports](https://compliance.salesforce.com/en/categories/c5-isae-3000) | Salesforce klar vorn |
| Preis & Vertrag | **Price** | Package prices per ticket and voice minute (pricing model 2.2) | Service Cloud Core €195 per user (Starter Suite from €25), plus €2 per conversation or €0.10 per action [Service pricing](https://www.salesforce.com/de/service/pricing/) [Agentforce pricing](https://www.salesforce.com/de/agentforce/pricing/) | je nach Fall |

## Wo Salesforce schwächer ist

- **Costs stack up:** License per user, plus Agentforce add-on or usage. Unused Flex Credits don't roll over, credits and conversations can't be used at the same time in one org, and voice costs more credits per action.
- **Product line in transition:** For Casey, Salesforce does not list email, for Fin it does, and Fin only becomes part of Salesforce once the acquisition closes. Which agent will handle emails going forward is open.
- **Limits of the email agent:** No attachments, no customer identity verification, new emails on closed cases are not processed, and the agent doesn't close cases itself. Without a configured language, it replies in English.
- **Language models not named:** On its trust page, Salesforce only mentions "third-party providers", naming neither provider nor region.

## Einwände

- **"We already have Salesforce in-house."** Then Salesforce is set for CRM and sales, and that's fair. For written correspondence, it's worth looking at the details: according to the docs, the email agent reads no attachments and no images. Compare both on the same emails with a meter photo.
- **"Salesforce has C5 and ISO 27001, you don't."** That's a fair point, we have no certifications of our own, ISO 27001 and SOC 2 are in progress, and Hetzner is ISO 27001 certified. In return, enneo is a German GmbH, stores data in Germany, and our DPA, TOMs, subprocessors and SLA are public.
- **"With Agentforce and soon Fin, we get everything from a single source."** For CRM and help center, that's true. For email, it's open which agent will be responsible going forward, and costs are made up of license plus usage. With us, inbox, AI agents and telephony are one product.

## Fragen an den Kunden

- **What happens to emails with a photo or PDF attached?** Expected answer: The agent only reads subject and text, attachments go to agents. Transition: "Those are exactly the emails our AI reads in full, including the meter photo."
- **How many credits does a case with several actions consume, and what happens to unused credits?** Expected answer: Hard to say up front, unused Flex Credits don't roll over. Transition: "With us, you calculate with package pricing per ticket and per voice minute."
- **Which agent will handle your emails going forward, Agentforce or Fin?** Expected answer: Still open. Transition: "With us, the AI for emails is part of the product, with ready-made specialist agents for utilities."

## Intern

- **Reason to switch is dependency, not functionality:** A prospect (financial services, uses Salesforce in service) says Salesforce is "not perfect", but it works and has been optimized over years. They are looking because it isn't state of the art and creates heavy dependency on Salesforce. *Attio call, May 13, 2026, min. 24:27*
- **Lock-in is a sore point:** The same prospect is glad to be getting out of Salesforce soon and doesn't want a new lock-in with per-user licenses and annual commitments. That explicitly applied to enneo's offer as well. *Attio call, May 13, 2026, min. 22:01 and 22:39*
- **Agentforce is the default in Salesforce environments:** A prospect (energy group, service subsidiary) says that for agents in a Salesforce environment, "everyone always looks at Agentforce first". He sees an entry point in the commercial customer segment without Salesforce, or in a parallel pilot. *Attio call, Aug 24, 2026, min. 7:31 and 12:17*

## Fazit

Salesforce is the stronger platform when a customer wants CRM, sales, service and help center from a single source, and it leads on certifications. We can win when many emails have attachments, photos or multiple requests, when data should be stored with a German provider, and with ready-made processes for utilities. We won't win on price and channels alone.

## Direktlinks

- [Doku](https://help.salesforce.com/s/)
- [API](https://developer.salesforce.com/docs)
- [Community](https://trailhead.salesforce.com/trailblazer-community)
- [Trust Center](https://compliance.salesforce.com)
- [Preise](https://www.salesforce.com/de/service/pricing/)
- [Release Notes](https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm&type=5)
- [Status](https://status.salesforce.com)

## Quellen

- [Our story](https://www.salesforce.com/company/our-story/)

- [Service Cloud pricing](https://www.salesforce.com/de/service/pricing/)
- [Agentforce pricing](https://www.salesforce.com/de/agentforce/pricing/)
- [Agentforce for Service](https://www.salesforce.com/service/ai/)
- [Connect an agent to service email](https://help.salesforce.com/s/articleView?id=ai.agent_email_parent.htm&type=5)
- [Limits of the Service Agent on email](https://help.salesforce.com/s/articleView?id=ai.service_agent_considerations_1.htm&type=5)
- [Agentforce Voice](https://www.salesforce.com/agentforce/voice/)
- [Ready-made agents, Sep 11, 2026](https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/)
- [Acquisition of Fin](https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/)
- [Hyperforce EU](https://www.salesforce.com/eu/hyperforce/)
- [Trusted AI and Trust Layer](https://www.salesforce.com/artificial-intelligence/trusted-ai/)
- [Agentforce compliance](https://compliance.salesforce.com/en/services/agentforce-einstein-platform)
- [C5 reports](https://compliance.salesforce.com/en/categories/c5-isae-3000)
- [Agentforce for energy](https://www.salesforce.com/de/energy-utilities/artificial-intelligence/)
- [Energy & Utilities pricing](https://www.salesforce.com/de/energy-utilities/cloud/pricing/)
- [Infrastructure and subprocessors](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf)
- [Trust site](https://trust.salesforce.com)
- [Help](https://help.salesforce.com/s/)
- [Developer documentation](https://developer.salesforce.com/docs)
- [Trailblazer Community](https://trailhead.salesforce.com/trailblazer-community)
- [Release notes](https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm&type=5)
- [Status](https://status.salesforce.com)
