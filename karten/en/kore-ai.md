---
slug: "kore-ai"
stand: "2026-11-05"
kurz: "US platform for AI agents and contact centers, office in Frankfurt"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Orlando (USA), office in Frankfurt** | Kore.ai, Inc., founder and CEO Raj Koneru. Since May 2026 a second headquarters in San Mateo, the official headquarters remains Orlando. Over 100 new enterprise customers in the last fiscal year, most recent investor AllianceBernstein. Headcount not public |
| Preise | **not public** | Billing per session. In AWS Marketplace, AI for Service, Contact Center AI, Agent AI, Quality AI, Workforce Management and Interaction Gateway are priced separately, Enterprise Support and test environment cost extra, no refunds |
| Hosting | **AWS, including Frankfurt** | Multi-tenant SaaS, dedicated VPC or on-premises according to the Trust Center. Frankfurt is documented in the energy case study. Subprocessors not publicly listed |
| Zertifikat | **ISO 27001, SOC 2 Type 2** | According to the Trust Center ISO/IEC 27001:2022, SOC 2 Type 1 and 2, PCI DSS. BSI C5 not found |

## Erster Satz

"Kore.ai is a very broad platform with a strong voicebot and its own contact center. With us, it's about written correspondence: one AI reads the email including the meter photo, posts in the target system and replies."

## Das Wichtigste vorweg

Kore.ai is a large US provider of AI agents with voicebot, chat, its own contact center and other products for internal processes. Kore.ai is ahead of us in breadth, voice services, certifications and contact center management. There is an email channel, but the docs mainly describe setup, not how the AI handles the content of an email through to posting, and according to the docs the agent platform doesn't read the content of images. Our advantage lies in fully automated email handling with multiple requests, photos and ready-made utility flows, from a German company with public privacy documentation.

## Unsere Verkaufsargumente

- **Email AI all in one:** At enneo, the AI reads the email, identifies and verifies the customer, posts in the target system and replies, fully automated if desired. Kore.ai has an email channel with custom domains and handover to agents. We found no public reference with automated email handling through to posting.
- **Multiple requests, one reply:** enneo creates a resolution plan for the whole email and handles all requests in one pass with one reply. At Kore.ai, language processing detects multiple requests via signal words such as "then" or "first" and works through them one after the other. According to the docs, if one fails, the rest no longer run.
- **Reading photos and PDFs:** enneo reads PDFs and photos, such as a meter photo. Kore.ai's agent platform extracts content from PDF, Word, text and JSON. Images are only stored, and according to the docs their content is not read.
- **For utilities, on top:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. Kore.ai offers ready-made packages for banking, retail and healthcare, and we found none for utilities.
- **German company, documentation open:** enneo is a GmbH from Berlin without investors, and data is stored at Hetzner in Germany. DPA, TOMs, subprocessors and SLA are public. At Kore.ai, the SLA and security documents in the Trust Center are only available on request, and DPA and subprocessor list are not listed there.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Email through to posting** | Fewer agents for written correspondence, no separate build phase for the email flow | "With us, the same AI reads, posts and replies, and we'll show you that on your own emails." |
| **Multiple requests in one pass** | One complete reply instead of follow-up questions and follow-up tickets | "Meter reading, new IBAN and installment in one email: with us, that's one pass and one reply." |
| **Reading photos in attachments** | Nobody has to type up meter photos | "Our AI simply reads the meter photo in the attachment along with the email." |
| **Ready-made flows for utilities** | Productive faster, only the ERP connection is built | "We bring meter reading, installment and bank details ready-made with plausibility checks." |
| **Privacy documentation public** | Privacy review without follow-up requests and without waiting for approvals | "Your privacy team can already read our DPA, TOMs, subprocessors and SLA themselves today." |
| **German company, storage at Hetzner** | Less back-and-forth on data residency and vendor country requirements | "We're a German GmbH and store data with a German provider in Germany." |

## Wo Kore.ai vorn liegt

- **Full-scale contact center:** Its own contact center with agent desktop, skill-based routing, queues with SLAs, outbound voice and SMS campaigns, real-time monitoring for team leads, automated quality checks and workforce management as a separate module. We lack a dialer, live dashboards and workforce management.
- **Voicebot and voice services:** Its own Voice Gateway with SIP and AudioCodes. Speech recognition and speech synthesis from Google, Azure, AWS, ElevenLabs, Deepgram, OpenAI, Gemini, xAI and others, selectable per language, custom providers possible. Last update on Oct 31, 2026. We have an EU voicebot with Deepslate, but less choice.
- **Language models and channels:** Ready-made integration with OpenAI, Azure OpenAI, Anthropic, Google Gemini and Amazon Bedrock, plus custom models and its own XO GPT models. Microsoft Teams, Slack, WhatsApp, Genesys Cloud, Amazon Connect and Zoom Contact Center as channels.
- **Certifications and deployment options:** ISO 27001:2022, SOC 2 Type 2 and PCI DSS. Runs as SaaS, in a dedicated VPC or on-premises. We have no certification of our own.
- **Large references:** Morgan Stanley, Citi, Vanguard, AMD, Lilly, plus logos from Bosch, MetLife and Cigna. An energy group with 80m customers runs chat in the UK, Germany and Turkey with 60% automation. According to Kore.ai, a Leader in the 2026 Gartner Magic Quadrant for Conversational AI.

## Unterschiede auf einen Blick

| Topic | enneo | Kore.ai | Assessment |
|---|---|---|---|
| **AI handling of emails** | One AI reads, identifies the customer, posts and replies, fully automated if desired | Email channel with flows and handover to agents. AI handling of content through to posting not described | enneo vorn |
| **Multiple requests in one email** | One resolution plan, everything in one pass, one reply | Detection via signal words, one after the other, stops at the first error. Not documented for email | enneo vorn |
| **Reading attachments and photos** | PDFs and photos, e.g. meter photo | PDF, Word, text, JSON. Images without content extraction | enneo vorn |
| **Agent workspace** | Ticketing agent workspace with skill-based routing in the product | Agent desktop with skill-based routing and queues in its own contact center | gleich |
| **Contact center management** | No dialer, no live dashboard, no workforce management | Outbound campaigns, real-time monitoring, workforce management, quality checks | Kore.ai klar vorn |
| **Ready-made flows for utilities** | Meter reading, installment, bank details ready-made, ERP connection per customer | Packages for banking, retail, healthcare. Not found for utilities | enneo vorn |
| **Where data is stored** | Hetzner, German provider, on-premises possible | AWS, also Frankfurt, dedicated VPC or on-premises. Company in the USA | je nach Fall |
| **Privacy documentation** | DPA, TOMs, subprocessors, SLA public | SLA and security documents on request, DPA and subprocessors not listed | enneo vorn |
| **Voicebot and voice services** | OpenAI (USA) or Deepslate (EU), less choice | Own Voice Gateway, many providers per language, custom providers possible | Kore.ai klar vorn |
| **Language models** | US providers by default, EU models in the DPA: Mistral, Nebius, Media Trooper | OpenAI, Azure, Anthropic, Gemini, Bedrock, custom models | Kore.ai vorn |
| **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001:2022, SOC 2 Type 2, PCI DSS | Kore.ai klar vorn |
| **Price** | Package pricing per ticket and per voice minute (pricing model 2.2) | Not public, per session, modules separately, support and test environment extra | je nach Fall |

## Wo Kore.ai schwächer ist

- **Written correspondence poorly documented:** The email docs describe domains, inboxes and grouping of emails, not how the AI reads and posts an email. The energy reference covers chat and agent assistance in Zendesk, and email doesn't appear there.
- **Many products and modules:** AI for Service, AI for Work, AI for Process and the agent platform are separate products. In AWS Marketplace, Contact Center AI, Agent AI, Quality AI, Workforce Management and Gateway are each billed separately per session. This makes the total cost hard to predict.
- **Little presence in the German market:** There isn't a single review on OMR. We found no public reference at a utility, insurer or municipal utility in the DACH region.
- **US company with documentation on request:** The contracting party in AWS Marketplace is an Indian subsidiary. Security and contract documents in the Trust Center are only available after approval, and no DPA is listed there.

## Einwände

- **"According to Gartner, Kore.ai is a Leader and much bigger than you."** That's true, Kore.ai is broader on voicebot, contact center and certifications. But for emails that an AI should handle on its own through to the target system, what counts is what happens with your own emails. We'll show that live, with multiple requests and a meter photo.
- **"But Kore.ai also runs in Frankfurt."** Yes, Kore.ai can run on AWS in Frankfurt. But the company is based in the USA, and the DPA and subprocessor list are not public. We're a German GmbH, store data at Hetzner in Germany, and all documentation is open.
- **"Kore.ai can do email too."** Kore.ai has an email channel, that's right. Ask for a reference in which the AI handles emails with multiple requests and photos on its own through to posting. We haven't found one publicly.

## Fragen an den Kunden

- **Has Kore.ai shown you how an email with three requests and a meter photo is handled fully automatically?** Expected answer: They showed chat or voicebot, not the email flow. Transition: "That's exactly what we're happy to show you with your own sample emails."
- **Which Kore.ai modules are in your offer, and what does your annual session volume cost?** Expected answer: Several modules, total cost still unclear. Transition: "With us, everything is one product with package pricing per ticket and per voice minute. Let's put the total costs side by side."
- **Does your privacy team already have Kore.ai's DPA and subprocessor list?** Expected answer: No, only on request. Transition: "Our documentation is public, so your privacy team can start reviewing today."

## Intern

No internal insights in Attio yet (as of Nov 5, 2026).

## Fazit

We won't win against Kore.ai on voicebot, contact center management, certifications or the size of its references. We can win where a lot of written correspondence should be handled automatically: multiple requests, photos in attachments, posting in the target system, ready-made utility flows. On top of that come a German company and open privacy documentation.

## Quellen

- [Kore.ai homepage](https://kore.ai)
- [About Kore.ai](https://www.kore.ai/about-us)
- [Second headquarters Bay Area, May 2026](https://kore.ai/news/kore-ai-establishes-bay-area-strategic-headquarters-to-lead-the-next-wave-of-enterprise-ai)
- [Trust Center](https://trust.kore.ai/)
- [Security and compliance](https://www.kore.ai/agent-platform/security-and-compliance)
- [Email channel](https://docs.kore.ai/xo/channels/add-email-channel/)
- [Channels](https://docs.kore.ai/ai-for-service/channels.md)
- [Contact Center AI](https://docs.kore.ai/ai-for-service/contact-center.md)
- [Multi-intent detection](https://docs.kore.ai/ai-for-service/automation/natural-language/nlu-configurations/multi-intent-detection)
- [Attachments in the agent platform](https://docs.kore.ai/agent-platform/v1/agents/agentic-apps/attachment-support.md)
- [Language models](https://docs.kore.ai/ai-for-service/generative-ai-tools/llm-integration)
- [Release notes Voice Gateway](https://docs.kore.ai/ai-for-service/release-notes/voice-gateway)
- [Energy group with 80m customers](https://kore.ai/customer-stories/80-million-customer-energy-giant)
- [AWS Marketplace AI for Service](https://aws.amazon.com/marketplace/pp/prodview-ru3m2q5dzyebu)
- [User reviews OMR](https://omr.com/de/reviews/product/kore-ai)
- [enneo resolution plan](https://docs.enneo.ai/en/ai-functions-agents/intent-lifecycle#smart-agent-v2)
