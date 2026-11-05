---
slug: "omq"
stand: "2026-11-05"
kurz: "Self-service AI from Berlin: help page, chatbot, email bot, voicebot since 2026"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Berlin, since 2012** | OMQ GmbH, headcount not public, over 250 customers according to its own website, research with DFKI and Humboldt University |
| Preise | **€160 to €3,000/month** | Starter, Essential, Business, Corporate public (€150 to €2,800 with annual contract), Flex on request. Email bot only from Business, plus one-time integration costs |
| Hosting | **AWS Frankfurt, Azure EU** | According to the DPA: AWS Frankfurt, Microsoft Azure Europe, Lime Connect Germany. Chatbot according to the website on "ChatGPT engine (OpenAI technology)" |
| Zertifikat | **not found** | No ISO 27001, SOC 2 or BSI C5 mentioned on the website, only "GDPR and AI Act compliant" |

## Erster Satz

"OMQ is very mature in self-service with its help page and chatbot. Emails are where we come in: with us, one AI handles even multiple requests all the way to posting in the target system, with one reply."

## Das Wichtigste vorweg

OMQ comes from self-service: help page, contact form and chatbot that answer questions from a knowledge base before they reach customer service. The email bot also answers from this knowledge base and plugs into third-party ticketing systems such as Zendesk, Freshdesk or Zammad. Actions in the backend (change address, cancel subscription, order status) are handled by a separate module, the AI Agent, documented mainly for chat and forms. OMQ has no agent workspace of its own, and the voicebot has only existed since August 2026.

## Unsere Verkaufsargumente

- **Email through to posting:** At enneo, the AI reads the email, identifies and verifies the customer, posts in the target system and replies, fully automated if desired. According to the product page, OMQ's email bot answers emails from the knowledge base. We found no documentation that it posts in the target system while doing so.
- **Multiple requests and attachments:** Meter reading, new IBAN and meter photo in one email: enneo handles all of it in one pass with one reply. At OMQ, nothing is documented on multiple requests or on reading attachments.
- **One system instead of a plugin:** enneo brings ticketing workspace, inbox, AI agents, knowledge and telephony in one product. For the cases the bot doesn't resolve, OMQ requires a third-party ticketing system.
- **Ready-made processes for utilities:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. OMQ's energy references are chatbots and help pages that answer questions about meter readings and installments. Capturing them in the billing system is not described there.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Posting in the target system by email** | Emails get resolved, not just answered, less rework for agents | "With us, the AI changes the installment in the system and confirms it in the reply." |
| **Multiple requests in one pass** | One complete reply instead of follow-up questions and follow-up tickets | "If your customer puts meter reading, IBAN and installment in one email, they get one reply from us." |
| **Reading attachments and photos** | Nobody has to type up meter photos and PDF attachments | "Our AI simply reads a meter photo in the attachment too." |
| **Own agent workspace in the product** | No second ticketing system to license and maintain, one point of contact | "Whatever the AI doesn't close lands with your agents in the same system." |
| **Ready-made processes for utilities** | Meter reading, installment and bank details productive faster, only the ERP connection needs to be built | "We bring the most important utility processes ready-made, with plausibility checks." |
| **TOMs and SLA public** | Privacy review without follow-up requests | "Besides the DPA, our TOMs, subprocessors and SLA are publicly available too." |

## Wo OMQ vorn liegt

- **Self-service for end customers:** Help page, smart contact form and chatbot answer questions before they become tickets. We don't have a help center for end customers.
- **Open pricing and frictionless trial:** Packages from €160 to €3,000 per month are on the website, 14-day trial, no onboarding costs. We don't have a public price list.
- **Quick to connect to existing systems:** Plugins for Zendesk, Freshdesk, Zammad, OTRS, Salesforce, plus shops (Shopware, Shopify), retail ERP (Xentral, JTL, Business Central) and parcel services. Anyone who already has a ticketing system doesn't have to replace anything.
- **Long reference list and good reviews:** Tchibo, Deutsche Bahn, Mister Spex, MAGIX, myphotobook (83% of emails answered automatically), in energy Stadtwerke Düren and Stadtwerke Stendal. OMR: 4.6 out of 5 from 95 reviews.
- **Many languages:** According to OMQ, over 30 languages for chatbot, email bot and voicebot.

## Unterschiede auf einen Blick

| Topic | enneo | OMQ | Assessment |
|---|---|---|---|
| **AI handling of emails** | Receipt, identify customer, posting in the target system, reply, fully automated if desired | Reply from the knowledge base, automatically or as a draft. Posting in the target system by email not documented | enneo vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Reading attachments and photos** | PDFs and photos, e.g. meter photo | Not documented | enneo vorn |
| **Actions in third-party systems** | Integrations as code, API, MCP, RPA for legacy systems | AI Agent via API (address, subscription, order status), MCP too since 08/2026 | je nach Fall |
| **Agent workspace** | Own ticketing with skill-based routing in the same product | None of its own, plugin in Zendesk, Freshdesk, Salesforce, OTRS, Zammad | enneo klar vorn |
| **Ready-made processes for utilities** | Meter reading, installment, bank details with plausibility checks | Information on meter readings and installments via chatbot and help page | enneo vorn |
| **Voicebot** | Own telephony or SIP, handover in the same system | Since 08/2026, via sipgate, answers from knowledge, forwarding to an extension, callback request by email | enneo vorn |
| **Agent assist** | Draft, summary, live transcription | Draft reply as a plugin in the ticketing system | enneo vorn |
| **Help center and contact form** | No help center for end customers | Help page, smart contact form, chatbot with widget for web and apps | OMQ klar vorn |
| **Hosting and models** | Hetzner Germany, EU models possible under the DPA | AWS Frankfurt, Azure Europe, chatbot on OpenAI technology, anonymization before storage | gleich |
| **Data protection documents** | DPA, TOMs, subprocessors, SLA public | DPA with subprocessors public, TOMs only on handover (as of 03/2023), SLA not found | enneo vorn |
| **Price** | Package pricing per ticket and per voice minute | Public monthly packages with request quota, email bot from Business plus integration costs | je nach Fall |

## Wo OMQ schwächer ist

- **No agent workspace of its own:** Everything the bot doesn't resolve goes to a third-party ticketing system or by email to the service team. So the customer needs two systems.
- **Email bot mainly answers from knowledge:** The product page describes replies from the knowledge base. It says nothing about multiple requests, attachments or posting in the target system. Users on OMR mention comprehension problems with complex requests and high effort maintaining the knowledge base.
- **Young voicebot:** Only since release 10.5 in August 2026, telephony only via sipgate, no public voice reference found.
- **Thin security evidence:** No certification found, TOM catalog from March 2023 not public, website privacy policy from 2022.

## Einwände

- **"OMQ is cheaper, the prices are even on the website."** That's true, the packages are open and the entry point is inexpensive. Ask what integration costs come on top for the email bot from Business, and which ticketing system you pay for separately for the remaining cases. With us, agent workspace and AI are one product.
- **"OMQ has municipal utilities as references."** Correct, Stadtwerke Düren and Stendal use the chatbot for questions about contracts, bills and meter readings. For emails in which the customer wants to change something, meter reading, installment and bank details are ready-made processes with posting in the system at enneo.
- **"We already run the OMQ chatbot."** Good, OMQ does self-service on the website very well. For the written correspondence that still comes in, enneo alongside it is often the better conversation than a complete switch.

## Fragen an den Kunden

- **What does the OMQ email bot do with an email that contains a meter reading, a new IBAN and a meter photo?** Expected answer: Unclear, or it only answers part of it from the knowledge base. Transition: "We're happy to show you that live with your own sample emails, including posting in the system."
- **Does the email bot already post changes in your billing system today, or does it only reply?** Expected answer: It replies, and an agent has to make the change. Transition: "With us, the AI makes the change and confirms it in the same reply."
- **Which system do your agents use for the cases the bot doesn't resolve?** Expected answer: A separate ticketing system. Transition: "With us, bot and agent workspace are one system, with one contract."

## Intern

No internal insights in Attio yet (as of Nov 5, 2026).

## Fazit

We don't win against OMQ on website self-service, open pricing or the number of languages. We can win where written correspondence really needs to be resolved: multiple requests, attachments, posting in the target system and an agent workspace in the same product. Where OMQ already runs as a chatbot, enneo for email alongside it is often an easier entry point than a switch.

## Quellen

- [Homepage](https://omq.ai)
- [About us](https://omq.ai/company/about-us/)
- [Legal notice](https://omq.ai/company/imprint/)
- [Pricing](https://omq.ai/pricing/)
- [AI Email Bot](https://omq.ai/products/reply/)
- [Email bot (German)](https://omq.ai/de/produkte/reply/)
- [AI Agent](https://omq.ai/products/ai-agent/)
- [AI Chatbot](https://omq.ai/products/chatbot/)
- [AI Voice Bot](https://omq.ai/products/voice-bot/)
- [Ticket System Assistant](https://omq.ai/products/assist/)
- [Integrations](https://omq.ai/integrations/)
- [Energy industry page](https://omq.ai/de/branchen/energie/)
- [Insurance industry page](https://omq.ai/industries/insurance/)
- [Case studies](https://omq.ai/customers/case-studies/)
- [myphotobook case study](https://omq.ai/customers/case-studies/deutsche-online-medien/)
- [Release Montevideo 10.5](https://omq.ai/blog/version-montevideo/)
- [Blog](https://omq.ai/blog/)
- [Data protection and data security](https://omq.ai/company/data-security/)
- [DPA (PDF)](https://omq.ai/de/unternehmen/OMQ_AnlageB_AVV_ausf%C3%BCllbar.pdf)
- [Press](https://omq.ai/company/press/)
- [OMR user reviews](https://omr.com/de/reviews/product/omq)
