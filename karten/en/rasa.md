---
slug: "rasa"
stand: "2026-11-06"
kurz: "Developer platform for chat and voice bots from Berlin and San Francisco"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Berlin + San Francisco** | Rasa Technologies GmbH (Berlin, HRB 184024 B) and Rasa Technologies Inc. (San Francisco). Over USD 70m in venture capital, most recently a USD 30m Series C in February 2024 (StepStone, PayPal Ventures, Andreessen Horowitz, Accel). Headcount not public |
| Preise | **not public** | Enterprise on request. Free Developer Edition: one bot per company, up to 1,000 external or 100 internal conversations per month |
| Hosting | **on-premises** | "On-premise by default", according to its security page Rasa does not host customer data. The pricing page also mentions a Managed Service, location and operator not named |
| Zertifikat | **none named** | Controls aligned with ISO 27002 according to Rasa, evidence on request. ISO 27001 or SOC 2 not found |

## Erster Satz

"Rasa is a strong tool if your own development team wants to build and run chat and voice bots itself, and emails are where we come in: with us, a ready-made AI handles them all the way to the booking in the target system."

## Das Wichtigste vorweg

Rasa is a construction kit for developers: chat and voice bots built from fixed processes ("flows") plus a language model, running in the customer's own infrastructure. Rasa itself writes that Forrester sees it as a fit for companies with their own developers or with a requirement to run everything on-premises. An email channel, an agent workspace and ready-made processes for utilities are not documented. enneo wins where a finished product for written communication and customer service is wanted. Rasa wins where a development team wants to build and run everything itself and choose any model freely.

## Unsere Verkaufsargumente

- **Email AI ready in the product:** At enneo, the AI reads the email, identifies and verifies the customer, books in the target system and replies, fully automated if desired. Rasa's homepage lists email as a channel, but the channel list in the documentation has no email channel. That would require building a custom connector in Python.
- **Multiple requests and attachments:** Meter reading, new IBAN and new installment in one email: enneo handles them in one pass with one reply, and the AI reads meter photos and PDFs along the way. Nothing on either is documented at Rasa.
- **Agent workspace included:** At enneo, ticketing workspace, inbox, AI agents, knowledge, telephony and voicebot are one system with skill-based routing. We did not find an agent workspace at Rasa, so handed-over cases end up in another system.
- **Describe instead of code:** enneo AI agents are described in plain language and changed via chat with Neo. According to its own Forrester summary, Rasa is meant for companies with developer resources. Processes are built as flows with Python actions, and Studio adds a low-code interface.
- **Additionally for utilities:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. Rasa does not mention the energy sector, its references come from telecom, banking and insurance.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Email AI in the product** | No email connector to build and maintain, emails are covered from day one | "With us, email handling isn't a project, it's a finished part of the product." |
| **Multiple requests and attachments** | One complete reply instead of follow-up questions, nobody retypes meter photos | "If your customer sends meter reading, IBAN and installment in one email with a photo, they get one reply from us." |
| **Agent workspace included** | No second system to license and connect for your agents | "Whatever the AI doesn't handle itself, your people continue in the same system." |
| **Describe instead of code** | Business teams change processes themselves, less dependence on developers | "With us, your business team describes a process in plain language, no development team needed." |
| **Operated by enneo** | No in-house team for servers, updates and version upgrades | "We run the platform in Germany at Hetzner, so you don't have to build your own operations." |
| **Ready-made processes for utilities** | Meter reading, installment and bank details go live faster, only the ERP connection is built | "We bring the most important utility processes ready-made with plausibility checks." |

## Wo Rasa vorn liegt

- **On-premises by default:** According to Rasa, it runs in the customer's infrastructure and personal data does not leave it. According to the case study, Helvetia's sales assistant runs "on-prem". At enneo, on-premises is only possible at high volume.
- **Free choice of language model:** OpenAI, Azure, Bedrock, Mistral, Gemini, Anthropic and self-hosted models via vLLM or Ollama, according to Rasa even small fine-tuned models from Llama 8B. At enneo, US providers are standard, EU models are possible under the DPA.
- **Breadth in voice:** Telephony via AudioCodes, Jambonz, Twilio, Vonage, SignalWire, speech services from Deepgram, Azure, Cartesia, Rime and, since October 2026, ElevenLabs, plus call recording. enneo has fewer speech providers to choose from.
- **Tools for development teams:** Version control, CI/CD, separate environments, automated tests with simulated conversations. According to Rasa, 5 out of 5 at Forrester for orchestration, lifecycle and pricing transparency, overall rating "Strong Performer" (Q2 2026). Plus a free Developer Edition to try it out.
- **Large references in DACH:** Deutsche Telekom with over 38 million conversations, Swisscom with a voice IVR and, according to Rasa, 50% lower operating costs, ERGO, Helvetia, Raiffeisen.

## Unterschiede auf einen Blick

| Topic | enneo | Rasa | Einordnung |
|---|---|---|---|
| **AI handling of emails** | One AI reads, identifies the customer, books and replies, fully automated if desired | No email channel in the documentation, only via a self-built connector | enneo klar vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Reading attachments and photos** | PDFs and photos, e.g. meter photo | Not found | enneo vorn |
| **Agent workspace** | Ticketing, inbox and skill-based routing in the same system | Not found, handover to another system | enneo klar vorn |
| **Ready-made processes for utilities** | Meter reading, installment, bank details ready, ERP connection per customer | Energy sector not mentioned, insurance cases as examples | enneo vorn |
| **Building and testing AI agents** | Describe in words, change via chat with Neo, test cases | Flows with Python actions, Studio as low-code, tests with simulated conversations | je nach Fall |
| **Where it runs** | Hetzner in Germany, on-premises at high volume | On-premises by default, Managed Service without a named location | je nach Fall |
| **Language models** | US providers standard, EU models under the DPA: Mistral, Nebius, Media Trooper | Freely selectable, including self-hosted | Rasa vorn |
| **Voicebot and speech services** | Own telephony or SIP, OpenAI (USA) or Deepslate (EU) | Several telephony connections, five speech service providers, recording | Rasa vorn |
| **Data protection documents** | DPA, TOM, subprocessors, SLA public | No subprocessor list, DPA not found publicly | enneo vorn |
| **Certifications** | None of our own, ISO 27001 and SOC 2 in progress, Hetzner ISO 27001 | None named, aligned with ISO 27002 | gleich |

## Wo Rasa schwächer ist

- **No finished product for service teams:** According to Rasa's own summary of the Forrester evaluation, buyers who want broad no-code tools, a large partner ecosystem or managed deployment will find better fits elsewhere.
- **Operations and maintenance with the customer:** Servers, updates and version upgrades are the customer's job. Rasa ships a new version every month, and version 3.21 from October 2026 contains several changes that existing projects have to adapt to.
- **Written communication not the focus:** No email channel in the documentation, no email reference found, attachments and multiple requests not documented.
- **Little external evidence:** No certification named, no subprocessor list. There are no reviews on OMR yet.

## Einwände

- **"Rasa is a Forrester Strong Performer and is used at Telekom and Swisscom."** True, those are strong references for chat and voice in telecom. We did not find a reference for email handling or for utilities, so ask for one specifically.
- **"With Rasa, everything stays in-house."** That's a real advantage if running in your own data center is mandatory. enneo can also run on-premises at high volume, otherwise we operate in Germany at Hetzner and your team doesn't have to build its own operations.
- **"Rasa is free."** The Developer Edition is free, but limited to one bot and 1,000 conversations per month, and Enterprise is priced on request. On top come developers and operations, which are part of the product at enneo.

## Fragen an den Kunden

- **Who builds, runs and updates the bot at your company, and how many developers are planned for it?** Expected answer: the in-house IT team or a service provider. Transition: "With us, the business team describes the processes and we take care of operations."
- **How will your customers' emails get into Rasa and be handled there all the way to the booking?** Expected answer: still open, or via a custom connection. Transition: "For us, that's the core of the product, we're happy to show it with your own sample emails."
- **Where do your agents handle the cases the bot doesn't resolve itself?** Expected answer: in another system that has to be connected separately. Transition: "With us, AI and agents work in the same system, with no handover to the outside."

## Intern

No internal insights in Attio yet (as of Nov 6, 2026).

## Fazit

We win against Rasa where a customer is looking for a finished customer service product: email AI all the way to the booking, multiple requests, attachments, an agent workspace and ready-made utility processes without an in-house development team. Rasa is ahead where a strong IT team wants to build chat and voice bots itself, run them on-premises and freely choose models and speech services. There, enneo is often the better conversation for written communication than for the voicebot.

## Quellen

- [Rasa homepage](https://rasa.com)
- [About Rasa](https://rasa.com/about)
- [Imprint](https://rasa.com/imprint)
- [Pricing](https://rasa.com/pricing)
- [Security](https://rasa.com/security-at-rasa)
- [Operations and data protection](https://rasa.com/product/managed-service)
- [Customers](https://rasa.com/customers)
- [Helvetia case study](https://rasa.com/customers/helvetia)
- [Insurance industry](https://rasa.com/industries/insurance)
- [Telecom industry](https://rasa.com/industries/telecom)
- [CALM explained](https://rasa.com/docs/learn/concepts/calm)
- [Text and voice channels](https://rasa.com/docs/reference/channels/messaging-and-voice-channels)
- [Building custom channels](https://rasa.com/docs/reference/channels/custom-connectors)
- [Speech services](https://rasa.com/docs/reference/integrations/speech-integrations)
- [Language models](https://rasa.com/docs/reference/config/components/llm-configuration)
- [Rasa Pro release notes](https://rasa.com/docs/reference/changelogs/rasa-pro-changelog)
- [Forrester Wave Q2 2026 from Rasa's perspective](https://rasa.com/blog/forrester-wave-2026-where-rasa-stands-out)
- [Series C, SiliconANGLE](https://siliconangle.com/2024/02/14/draft-conversational-ai-startup-rasa-technologies-raises-30m-combine-llms-traditional-chatbots)
- [User reviews OMR](https://omr.com/en/reviews/product/rasa)
