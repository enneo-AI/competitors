---
slug: "parloa"
stand: "2026-11-09"
kurz: "AI agents for phone and chat from Berlin, with lots of capital"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Berlin and New York, 380+ employees** | Parloa GmbH, Berlin (HRB 187494 B). Series D 01/2026: USD 350m at a USD 3bn valuation, led by General Catalyst, plus EQT Ventures, Altimeter and others. SAP has held a strategic stake since 05/2026 |
| Gegründet | **2018 (predecessor 2017)** | By Malte Kosub (CEO) and Stefan Ostwald (Chief AI Officer) in Berlin, first as the agency Future of Voice |
| Ursprung | **Voice agency since 2017** | Future of Voice helped companies use speech technology. In 2018, Parloa was created internally as a tool for Alexa skills and phone bots. In 2020, the founders sold the agency and focused on Parloa |
| Preise | **not public** | Pricing page since 10/2026: phone per minute, chat per interaction, rate based on the complexity of the use case, one volume commitment across all use cases, outcome-based billing optional |
| Hosting | **Microsoft Azure** | Previously its own instance in Germany, since 09/2026 "Parloa Zones" with a choice of region. The Trust Center only names a "Major Cloud Provider" |
| Zertifikat | **ISO 27001, SOC 2** | Plus ISO 42001, PCI DSS, HIPAA. No C5: Parloa states it is not subject to it and that the cloud it uses is C5-attested |

## Erster Satz

"Parloa is one of the strongest vendors on the phone. The question is what happens to your emails and letters, and which system your agents end up working in."

## Das Wichtigste vorweg

Parloa builds AI agents for phone and chat and is among the strongest vendors there, with lots of capital and large insurers in DACH as customers. Even in November 2026, we found neither an email channel nor an agent workspace of its own. Parloa hands over to third-party contact centers and CRMs. Our advantage lies in written correspondence and in everything running in one system. On the phone, Parloa is ahead.

## Unsere Verkaufsargumente

- **Email and letters with AI:** enneo reads emails and letters, identifies requests and customers, posts in the target system and replies, also fully automated. On its pricing page, its channel page and in the February 2026 product release, Parloa lists only phone and chat. We found no email channel.
- **One system instead of two:** With enneo, the agent workspace, inbox, AI agents, knowledge and telephony are one product with skill-based routing. At Parloa, humans take over in a third-party system such as Genesys, Five9, Salesforce or Zendesk. So the customer always needs a second product and a second contract.
- **Multiple requests, one reply:** enneo handles a meter reading, a new IBAN and a new installment in one email in a single pass with one reply, including a PDF and a photo in the attachment. Parloa has documented nothing on this for written requests. In chat, Parloa accepts files, but it doesn't say whether the AI evaluates their content.
- **Stored with a German provider:** enneo stores data at Hetzner in Germany, and for large volumes also in the customer's own data center. Parloa runs on Microsoft Azure. We found no on-premises option.

## Business-Impact

| With enneo | Outcome for the customer | How to say it |
|---|---|---|
| **Emails and letters through to posting** | Written correspondence is also automated through to the action in the target system, fewer agents needed for emails and letters | "Parloa lists phone and chat. With us, the AI also handles emails and letters through to the action in the target system." |
| **One system for AI and team** | One system and one contract, every case sits in one place | "At Parloa, humans take over in a third-party system. With us, AI and team work in the same agent workspace." |
| **Multiple requests and attachments in one pass** | Emails with a meter reading, an IBAN and a photo are handled with one reply, fewer follow-up questions and follow-up emails | "We handle three requests and a meter photo in one email in a single pass with one reply." |
| **Storage in Germany, on-premises if needed** | Simpler data protection review, and for large volumes everything runs in your own data center | "We store data at Hetzner in Germany, and for large volumes also at your site. We did not find an on-premises option at Parloa." |

## Wo Parloa vorn liegt

- **Phone and speech:** According to Parloa, more than 140 languages and variants, SIP directly to the phone system, contact center and WebRTC, and switching from chat to a call without losing context. Speech synthesis can be set to EU or US per agent (ElevenLabs). Our voicebot runs via OpenAI or Deepslate, with less choice.
- **Integration with third-party contact centers:** Ready-made integrations with Genesys, Amazon Connect, Cisco, Avaya, Five9, Talkdesk, RingCentral, Vonage and others, plus SAP, Salesforce, Dynamics and ServiceNow. On handover, the human gets a transcript or summary. On Oct 16, Parloa's docs also described context via SIP header (UUI) in both directions, for example with Genesys. We only pass the ticket number in the SIP header outbound and read no context inbound.
- **Certifications:** ISO 27001:2022, ISO 42001, SOC 2 Type 1 and 2, PCI DSS, HIPAA. We have none of our own, ISO 27001 and SOC 2 are in progress.
- **References in our industries:** Insurers such as Swiss Life, BarmeniaGothaer, Württembergische (33% shorter wait times according to Parloa), Schwäbisch Hall, Uelzener, Münchener Verein and DOMCURA. Plus utilities such as MAINGAU, evm and rhenag.
- **Capital and partners:** More than USD 560m in funding. Since Oct 26, 2026, SAP has been selling the platform as "SAP Conversational Agent Management by Parloa". Teams is connected to bring experts into the conversation. We have no native Teams integration.

## Unterschiede auf einen Blick

| Area | Topic | enneo | Parloa | Assessment |
|---|---|---|---|---|
| Kanäle | **Email and letters with AI** | Full process through to the action in the target system, also fully automated. Letters as a separate channel | Not found, Parloa lists only phone and chat [Channels](https://www.parloa.com/platform/conversation-infrastructure/) [Pricing](https://www.parloa.com/de/plattform/preise/) | enneo klar vorn |
| Kanäle | **Voicebot and speech providers** | Speech to speech via OpenAI (USA) or Deepslate (EU) | 140+ languages, speech synthesis per agent EU or US via ElevenLabs [Channels](https://www.parloa.com/platform/conversation-infrastructure/) [Release 02/2026](https://www.parloa.com/blog/parloa_product_release_2026/) | Parloa vorn |
| KI & Automatisierung | **Multiple requests in one email** | Everything in one pass, one reply | Not documented, as there is no email channel [Channels](https://www.parloa.com/platform/conversation-infrastructure/) | enneo vorn |
| KI & Automatisierung | **Language models** | US providers by default, EU models possible in the DPA, no training on customer data | OpenAI, Anthropic, Gemini, Azure, Bedrock, xAI, Mistral. Zero retention mode. No commitment against training found [Integrations](https://www.parloa.com/platform/integrations/) [Release 02/2026](https://www.parloa.com/blog/parloa_product_release_2026/) | gleich |
| Arbeitsplatz & Anbindungen | **Agent workspace** | Own ticketing, inbox, telephony and skill-based routing | None found, handover to Genesys, Five9, Salesforce, Zendesk and others [Integrations](https://www.parloa.com/platform/integrations/) | enneo klar vorn |
| Arbeitsplatz & Anbindungen | **Integration with third-party contact centers** | Own telephony. Ticket number in the SIP header outbound, no context inbound | Ten contact center platforms, handover with transcript or summary [Integrations](https://www.parloa.com/platform/integrations/) | Parloa klar vorn |
| Arbeitsplatz & Anbindungen | **MS Teams** | No native integration, telephony only via SIP | Teams to bring experts into the conversation. Teams telephony not found [Integrations](https://www.parloa.com/platform/integrations/) | Parloa vorn |
| Daten & Sicherheit | **Where data is stored** | Hetzner, German provider, data centers in Germany | Microsoft Azure, instance in Germany, region selectable since 09/2026 [Running on Azure](https://www.parloa.com/labs/insights/building-parloa-zones-repeatable-regional-deployments-with-central-control/) [Parloa Zones](https://www.parloa.com/blog/parloa-zones-deploy-ai-globally-with-data-residency-you-can-prove/) | enneo vorn |
| Daten & Sicherheit | **On-premises** | Possible for large volumes | Not found, regions only in the Azure cloud [Parloa Zones](https://www.parloa.com/blog/parloa-zones-deploy-ai-globally-with-data-residency-you-can-prove/) | enneo vorn |
| Daten & Sicherheit | **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001, 42001, SOC 2, PCI DSS, HIPAA. No C5 [Trust Center](https://trust.parloa.com/) [Security](https://www.parloa.com/platform/enterprise-security-governance/) | Parloa klar vorn |
| Preis & Vertrag | **Pricing** | Package prices per ticket and voice minute | Per minute or interaction, rate based on complexity, volume commitment [Pricing](https://www.parloa.com/de/plattform/preise/) | je nach Fall |

## Wo Parloa schwächer ist

- **Only phone and chat:** For email, letters and the agent workspace, the customer needs a second system. Even the new "Context Intelligence" (10/2026) talks about "any channel" but doesn't mention email.
- **Pricing hard to plan:** No price list. The rate per minute depends on the complexity of each use case and is set by sales.
- **Little that can be publicly verified:** The developer documentation is no longer public, and earlier pages lead nowhere. The Trust Center names only a "Major Cloud Provider" as hosting and lists the subprocessors (Google, Twilio, Datadog, MongoDB, Microsoft) without purpose or location.

## Einwände

- **"Parloa is the market leader and has many times the capital."** On capital and on the phone that's true, and we don't argue with it. What matters for you is which part of your volume it covers: Parloa lists phone and chat, while email and letters stay in a second system. With us, both run in one product.
- **"Parloa is cheaper per minute."** It may look that way in a first comparison. Ask which calls are billed, including those that are only transferred, and add the second system for written correspondence and agents. With us, inbox, agent workspace and telephony are included in the product.
- **"We can buy Parloa through our SAP contract."** Since October 2026, SAP sells Parloa itself, which makes purchasing easier. For email, letters and the agent workspace, you still need another system. With us, it's one product with one contract.

## Fragen an den Kunden

- **How do emails, letters and scans get into Parloa, and who handles them there?** Expected answer: a reference to chat and messaging, or to another system. Transition: "With us, email and letters are channels of their own, with AI through to the action in the target system."
- **Which system does your team work in when Parloa hands over to a human?** Expected answer: in the existing CRM or contact center, which the customer provides and licenses itself. Transition: "With us, the agent workspace is part of the product, with inbox, telephony and skill-based routing."
- **Which calls does Parloa bill, and which per-minute rate applies to your use cases?** Expected answer: the rate per use case only in the quote, billing is per call. Transition: "Let's compare the total cost, with all minutes and the second system for written correspondence."

## Intern

- **Specialist, cheaper in the standard calculation:** A prospect (retail) calls Parloa "not bad according to everyone" and "very specialized", and cheaper in its standard calculation. The higher price would have to be justified by enneo's email added value, since Parloa is "really only voice and chat". *Attio call, Jun 17, 2026, min. 22:28 and 5:41*
- **Every call is billed:** A partner (implementation partner of both vendors) explains the price gap in the same comparison: Parloa bills every incoming call regardless of what happens next, including those that are only transferred. Comparing per-minute prices one to one gives a skewed picture. *Attio call, Jun 17, 2026, min. 41:34*
- **Business unit against Parloa:** A partner (implementation partner) reports from an ongoing comparison: the prospect's business unit wants enneo, and Parloa is out on functionality "because Paloa can only do autopilot", meaning there is no mode in which the AI prepares the case for agents. Parloa is only still in the race on price. *Attio call, Aug 26, 2026, min. 14:28 and 15:29*
- **Channel silos at an existing customer:** An existing customer (utility, large account) uses Parloa for voice and chatbot and enneo for written correspondence. As a result, logic is rebuilt per channel, and it's hard to see which channels a customer came through before calling. *Attio call, Oct 27, 2026, min. 35:09*
- **Two service providers under review:** The same existing customer sees enneo's voice demo as "the counterpart to Paloa" and is checking whether it "makes no sense at all to run two service providers". *Attio call, Oct 27, 2026, min. 47:50 and 51:19*
- **Wins tenders on experience:** A partner (consultancy and integrator, Parloa is its largest partnership) says that in tenders people often ask why Parloa costs so much. In the end, though, "the winner is Palor", because of its experience with large volumes. *Attio call, Nov 3, 2026, min. 17:41 and 59:49*

## Fazit

We don't win against Parloa on the phone, on certifications or on integration with large contact centers. We can win where there is a lot of written correspondence and the customer doesn't want to run two systems: email and letters through to posting, multiple requests, agent workspace and AI in one product, stored with a German provider. Where Parloa is already in place on the phone, enneo is the obvious conversation for the written channel.

## Direktlinks

- [Trust Center](https://trust.parloa.com/)
- [Preise](https://www.parloa.com/de/plattform/preise/)
- [Release Notes](https://www.parloa.com/resources/innovation/)

## Quellen

- [Trust Center](https://trust.parloa.com/)
- [Subprocessors](https://trust.parloa.com/subprocessors)
- [Security](https://www.parloa.com/platform/enterprise-security-governance/)
- [Parloa Zones](https://www.parloa.com/blog/parloa-zones-deploy-ai-globally-with-data-residency-you-can-prove/)
- [Running on Azure](https://www.parloa.com/labs/insights/building-parloa-zones-repeatable-regional-deployments-with-central-control/)
- [Release 02/2026: EU speech synthesis, retention](https://www.parloa.com/blog/parloa_product_release_2026/)
- [Release notes](https://www.parloa.com/resources/innovation/)
- [Channels and telephony](https://www.parloa.com/platform/conversation-infrastructure/)
- [Integrations](https://www.parloa.com/platform/integrations/)
- [Pricing](https://www.parloa.com/de/plattform/preise/)
- [Pricing page since Oct 8, 2026](https://www.usagepricing.com/blueprint/activity/parloa-2026-10-08-per-minute-pricing-published)
- [Customers](https://www.parloa.com/customers/)
- [Series D](https://www.parloa.com/parloa-in-the-press/parloa-valued-at-3-billion-with-350m-series-d/)
- [SAP stake](https://www.parloa.com/de/presse/parloa-vertieft-partnerschaft-mit-sap-und-setzt-neue-massstaebe-fuer-kundenerlebnisse-mit-agentic-ai/)
- [SAP Solution Extension](https://www.parloa.com/parloa-in-the-press/SAP-conversational-agent-management-by-parloa/)
- [Legal notice](https://www.parloa.com/de/impressum/)
- [About Parloa](https://www.parloa.com/company/about/)
- [Founded as Future of Voice (deutsche-startups.de)](https://www.deutsche-startups.de/2023/06/23/parloa-kundenservice/)
- [Founding year 2018 (deutsche-startups.de)](https://www.deutsche-startups.de/2025/05/12/unicorn-parloa/)
- [Docs landing page, content login only](https://docs.parloa.com/)
- [enneo resolution plan](https://docs.enneo.ai/en/ai-functions-agents/intent-lifecycle#smart-agent-v2)
