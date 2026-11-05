---
slug: "cognigy"
stand: "2026-11-05"
kurz: "AI agent platform for phone and chat from Düsseldorf, owned by NiCE"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Düsseldorf, part of NiCE** | Cognigy GmbH, founded 2016. Part of NiCE since Sep 8, 2025, purchase price around USD 955m. According to NiCE, over 1,000 brands as customers. Headcount not found |
| Preise | **not public** | Billed per conversation (up to 50 inputs within 24 hours), phone via concurrent lines. Knowledge AI, xApps, Ops Center and Voice Gateway licensed separately |
| Hosting | **SaaS in four regions** | Europe, USA, UK, Australia. Operator of the European environment not named. Via NiCE CXone on AWS, including Frankfurt. No longer on-premises for new customers |
| Zertifikat | **ISO 27001, SOC 2, C5** | According to the Trust Center, also ISO 27701, ISO 42001, TISAX. Type and scope of the C5 attestation not stated |

## Erster Satz

"Cognigy is one of the strongest platforms on the phone and in chat. The only question is what happens to your incoming emails and letters, because Cognigy has no inbound channel for them."

## Das Wichtigste vorweg

Cognigy is one of the best-known platforms for AI agents on the phone and in chat, with large references in Germany such as ERGO, AOK PLUS and Lufthansa. Cognigy is ahead of us on voicebot, AI agent testing and certifications. Cognigy does not process incoming emails: none of the 30 inbound channels in the docs is for email, and email exists only for sending from a flow. Cognigy no longer develops its own agent workspace. Handover goes to third-party contact centers, mainly NiCE CXone.

## Unsere Verkaufsargumente

- **Email AI from a single source:** At enneo, the AI reads the email, identifies and authenticates the customer, books in the target system and replies, fully automated if desired. Cognigy has no inbound channel for this, not even in the release notes up to 2026.22 (early November 2026). Its channels are phone, webchat, messengers and generic interfaces such as REST and webhook.
- **Multiple requests and attachments:** Meter reading, new IBAN and new installment in one email: enneo handles them in one pass with one reply, PDFs and photos included. At Cognigy, the language model can read images in chat if the channel allows attachments. Nothing is documented about PDFs from customers or multiple requests in one message.
- **One product with an agent workspace:** At enneo, ticketing agent workspace, inbox, AI agents, knowledge and telephony are one system. Cognigy's agent workspace ("Live Agent") is in maintenance mode and only gets security and bug fixes. Anyone who needs human agents buys a contact center on top, such as NiCE CXone.
- **For utilities in addition:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. At Cognigy we found no ready-made utility processes. The utility reference Salzburg AG is a chat assistant.
- **On-premises possible:** enneo stores data at Hetzner, and at high volume also in the customer's data center. Cognigy no longer offers on-premises to new customers, only existing customers continue.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Incoming email all the way to the booking** | No second system to buy and maintain for written correspondence | "For incoming emails you'd need another system alongside Cognigy. With us, the same AI handles it." |
| **Agent workspace in the product** | No extra contact center license, no risk from a workspace being phased out | "Cognigy's agent workspace no longer gets new features. With us, it's part of the product." |
| **Multiple requests and attachments** | Fewer follow-up contacts, one case instead of several | "Meter reading, new IBAN and the meter photo attached: with us that's one pass and one reply." |
| **Ready-made processes for utilities** | Less build effort for the most common requests | "You don't build meter reading, installment and bank details yourself with us, the AI agents are ready." |
| **On-premises possible** | An option for organizations with strict operating requirements | "Cognigy no longer offers new customers operation in their own data center. With us, that's possible at high volume." |

## Wo Cognigy vorn liegt

- **Voicebot and speech services:** Own Voice Gateway with SIP, SIPREC and recording. Speech recognition and speech synthesis from AWS, Deepgram, ElevenLabs, Google, Microsoft, Nuance, Speechmatics or custom providers, ElevenLabs and Deepgram also EU-hosted. We have an EU voicebot with Deepslate, but less choice.
- **Testing AI agents:** The Simulator (since January 2026) lets synthetic customers with a persona, a task and success criteria run many conversations, and an AI judge scores them. Since March 2026, comparison tests of prompts and models before launch have been added.
- **Certifications:** ISO 27001, 27701, 42001, SOC 2 Type II, TISAX and BSI C5 according to the Trust Center. We have no certification of our own.
- **Large references in DACH:** ERGO (phone and chat, since 2024), AOK PLUS (voice agent, 30,000 calls in the first month), Salzburg AG, Lufthansa, Mercedes-Benz, DATEV. According to Cognigy, a Leader in the Forrester Wave 2026 and the Gartner Magic Quadrant 2025.
- **Open to other systems:** Handover to NiCE CXone, Genesys, Salesforce, 8x8, RingCentral and others. Microsoft Teams, Slack and WhatsApp as channels. Choice of language models from OpenAI, Azure, Anthropic, Google, AWS Bedrock and Mistral. MCP and agent-to-agent interface.

## Unterschiede auf einen Blick

| Topic | enneo | Cognigy | Einordnung |
|---|---|---|---|
| **AI handling of emails** | One AI reads, identifies the customer, books and replies, fully automated if desired | No inbound channel for email. Email only for sending from the flow | enneo klar vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Reading attachments and photos** | PDFs and photos, e.g. meter photo | Images in chat via the language model if the channel allows attachments. PDFs from customers not documented | enneo vorn |
| **Agent workspace** | Ticketing agent workspace with skill-based routing in the product | Live Agent in maintenance mode, handover to third-party contact centers | enneo vorn |
| **Ready-made processes for utilities** | Meter reading, installment, bank details ready, ERP integration per customer | Not found, processes are built by the customer | enneo vorn |
| **Where data is stored** | Hetzner, German provider, on-premises possible | SaaS Europe, operator not named. CXone variant on AWS. No longer on-premises for new customers | enneo vorn |
| **Building and testing AI agents** | Describe in words, change via chat with Neo, test cases | Agent with job description and tools, Simulator with synthetic customers, comparison tests | Cognigy vorn |
| **Voicebot and speech services** | OpenAI (USA) or Deepslate (EU), less choice | Own Voice Gateway, eight providers plus custom ones, EU-hosted options | Cognigy klar vorn |
| **Language models** | US providers by default, EU models in the DPA: Mistral, Nebius, Media Trooper | OpenAI, Azure, Anthropic, Google, Bedrock, Mistral, custom endpoint possible | Cognigy vorn |
| **Contact center integration** | Own telephony, SIP trunk. Teams only via SIP | Handover to CXone, Genesys, Salesforce, 8x8 and others, Teams as a channel | Cognigy vorn |
| **Certifications** | None of our own, under audit. Hetzner ISO 27001 | ISO 27001, 27701, 42001, SOC 2 Type II, TISAX, BSI C5 | Cognigy klar vorn |
| **Price** | Package prices per ticket and voice minute (pricing model 2.2) | Not public, per conversation, phone via lines, add-on modules separate | je nach Fall |

## Wo Cognigy schwächer ist

- **Written correspondence is missing:** Neither the docs nor the release notes nor the Nexus 2026 announcements name email as a channel. The ERGO and AOK PLUS references also cover only phone and chat. Text could be fed in via the REST interface, but Cognigy does not describe an email flow.
- **Being restructured under NiCE:** Live Agent no longer gets new features, and on-premises is no longer available to new customers. Development is visibly aligning with NiCE CXone, for example with dedicated nodes for CXone Copilot.
- **Costs add up:** No public prices. Knowledge AI, xApps, Ops Center and Voice Gateway each need their own license. In CXone, a call over 10 minutes counts as two conversations.
- **Integrations not ready out of the box:** Users on OMR praise the low-code builder but want more ready-made integrations with enterprise systems (only 7 reviews).

## Einwände

- **"Cognigy is the market leader and now belongs to NiCE."** For voicebots that's true, and we acknowledge it. But the acquisition also means Live Agent is in maintenance mode and development is aligning with NiCE CXone. If you want your agents in the same system, with Cognigy you buy a contact center on top.
- **"We already have Cognigy on the phone."** Then there's no need for a complete switch. Cognigy has no channel for incoming emails and letters. That's where we come in, all the way to the booking in the target system and with an agent workspace for the rest.
- **"Cognigy has ISO 27001, SOC 2 and C5, you don't."** That's true, we don't have our own certifications yet, and ISO 27001 and SOC 2 are under audit. Data is stored at Hetzner in Germany, and Hetzner is ISO 27001 certified. DPA, TOMs, subprocessors and SLA are publicly available.

## Fragen an den Kunden

- **How do incoming emails and letters get into the same case as the phone call?** Expected answer: via a different system, not via Cognigy. Transition: "Then written correspondence stays in a second system. With us, email, letter, chat and phone run in one."
- **Which agent workspace is set for your agents over the next few years, Cognigy Live Agent or NiCE CXone?** Expected answer: uncertainty or a reference to CXone. Transition: "According to Cognigy's own docs, Live Agent is in maintenance mode. With us, the agent workspace is part of the product."
- **Which modules are already included in your Cognigy offer?** Expected answer: the base license, add-on modules open. Transition: "At Cognigy, Knowledge AI, xApps, Ops Center and Voice Gateway each need their own license. Let's put the total costs side by side."

## Intern

- **Too expensive for the partner's customers:** A partner had its own partnership with Cognigy and implemented hardly any projects. Its customers declined: "we implemented hardly any projects there, because they were simply too expensive." *Attio call, Oct 19, 2026, min. 43:19*
- **Many integrations, one gets used:** The same partner sees little value in the breadth: "in the end you need exactly one integration, not those thirty." *Attio call, Oct 19, 2026, min. 43:40*
- **Too big and too expensive:** A potential partner is looking for alternatives because Cognigy is too big and too expensive "in many places". *Attio call, Sep 4, 2026, min. 9:18*
- **Unhappy existing customer under contract:** A partner (AI consulting) reports on an industrial company that started with Cognigy and is "not so happy". An ongoing contract makes switching harder. *Attio call, Jul 16, 2026, min. 31:44*

## Fazit

We don't win against Cognigy on voicebot, AI agent testing, certifications or the size of references. We can win where incoming emails and letters should be processed automatically all the way to the booking, with multiple requests, attachments, energy processes and its own agent workspace in the same product. Where Cognigy already runs on the phone, enneo for written correspondence alongside it is often the better conversation than a complete switch.

## Quellen

- [Cognigy homepage](https://www.cognigy.com)
- [Legal notice](https://www.cognigy.com/legal-notice)
- [Trust Center](https://trust.cognigy.com)
- [Channels (endpoints)](https://docs.cognigy.com/ai/deploy/endpoint-reference/overview)
- [Email notification (sending only)](https://docs.cognigy.com/ai/agents/develop/node-reference/data/email-notification.md)
- [LLM Prompt node, reading images](https://docs.cognigy.com/ai/agents/develop/node-reference/service/llm-prompt.md)
- [Installation types](https://docs.cognigy.com/ai/administer/installation/about)
- [SaaS environments and regions](https://docs.cognigy.com/ai/administer/installation/ip-ranges-shared-environments.md)
- [Live Agent maintenance mode](https://docs.cognigy.com/live-agent/installation/browser-requirements)
- [Live Agent inboxes](https://docs.cognigy.com/live-agent/settings/inboxes.md)
- [Billing](https://docs.cognigy.com/ai/administer/billing.md)
- [AI Agents](https://docs.cognigy.com/ai/agents/overview.md)
- [Simulator](https://docs.cognigy.com/ai/agents/test/simulator/overview.md)
- [Simulator launch January 2026](https://www.cmswire.com/contact-center/nice-unveils-cognigy-simulator-for-ai-agent-testing/)
- [Nexus 2026](https://www.nice.com/press-releases/nice-cognigy-unveils-breakthrough-agentic-ai-innovations-at-nexus-2026)
- [Release notes 2026.22](https://docs.cognigy.com/release-notes/2026.22.md)
- [Release notes 2026.21](https://docs.cognigy.com/release-notes/2026.21.md)
- [Product updates](https://www.cognigy.com/product-updates)
- [Voice Gateway speech providers](https://docs.cognigy.com/voice-gateway/references/tts-and-stt-vendors)
- [Voice Gateway technical capabilities](https://docs.cognigy.com/voice-gateway/technical-capabilities.md)
- [EU-hosted speech services](https://www.cognigy.com/product-updates/2025.17)
- [Cognigy in CXone](https://help.nicecxone.com/Content/cognigyai/cognigyai.htm)
- [BSI C5](https://www.cognigy.com/blog/why-bsi-c5-certification-matters-for-banking-and-insurance)
- [Acquisition announced](https://www.nice.com/press-releases/nice-to-acquire-cognigy-advancing-the-leading-cx-ai-platform-to-accelerate-ai-first-customer-experience)
- [Acquisition closed](https://www.nice.com/press-releases/nice-closes-acquisition-of-cognigy-transforming-customer-experience-with-best-in-class-data-driven-cx-ai-platform)
- [Düsseldorf location](https://israel.ahk.de/en/news/major-german-israeli-ai-exit-nice-acquires-duesseldorf-s-cognigy-for-approx.-955m)
- [ERGO](https://www.cognigy.com/news/ergo-selects-cognigy)
- [AOK PLUS](https://www.cognigy.com/news/aok-plus-selects-cognigy)
- [Salzburg AG](https://cognigy.com/en/case-study/salzburg-ag)
- [DATEV](https://www.cognigy.com/news/datev-cognigy.ai-compliant-voice-bots)
- [OMR user reviews](https://omr.com/de/reviews/product/cognigy-ai)
- [enneo solution plan](https://docs.enneo.ai/en/ai-functions-agents/intent-lifecycle#smart-agent-v2)
