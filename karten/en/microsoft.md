---
slug: "microsoft"
stand: "2026-11-09"
kurz: "Dynamics 365 Contact Center with AI agents from Copilot Studio"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Microsoft, USA** | Dynamics 365 Customer Service and Contact Center, AI agents via Copilot Studio and the Power Platform |
| Gegründet | **1975** | Microsoft was founded in Albuquerque in 1975 and has been based in Redmond, Washington, since 1986 |
| Ursprung | **CRM since 2003** | Microsoft came from operating systems and Office, Microsoft CRM 1.0 was released in January 2003. Copilot as an AI assistant for Dynamics 365 was introduced in March 2023 |
| Lizenz | **€91 / €169 / €95.30** | Customer Service Enterprise / Premium / Contact Center per user per month, billed annually. AI via Copilot Credits at extra cost (pack of 25,000 credits: USD 200 per month), telephony via Azure Communication Services at extra cost |
| Hosting | **EU Data Boundary** | Environment in Europe can be selected, language models via Azure OpenAI in the EU. At peak load, "Flex Routing" can process outside the EU |
| Zertifikat | **ISO 27001, SOC 2, BSI C5** | Dynamics 365 within ISO 27001 scope, joint SOC 2 and C5 report for Azure, Dynamics 365 and Online Services |

## Erster Satz

"If Dynamics and Microsoft 365 are already in place at your company, Microsoft is the obvious choice. The only question is how many licenses and self-built agents you need before an email with three requests and a meter photo is actually posted."

## Das Wichtigste vorweg

Microsoft is the obvious choice for customers on Microsoft 365 and Dynamics. Since Sep 30, 2026, Dynamics 365 Customer Service answers incoming emails with AI, without agents if desired. Actions in the target system run through custom Copilot Studio agents or connectors, which is build work in the project. Microsoft leads on telephony, workforce management, certifications and ecosystem. We lead on the ready-made email flow with multiple requests, attachments and energy processes.

## Unsere Verkaufsargumente

- **One product instead of a license kit:** At enneo, agent workspace, AI agents, knowledge and telephony are one system. At Microsoft, autonomous email handling needs Customer Service, the Customer Intent Agent, the Case Management Agent, an Azure subscription for the credits, an inbox with an application user and, for actions, custom agents in Copilot Studio. Telephony comes on top as Contact Center and Azure Communication Services.
- **Multiple requests, one reply:** Meter reading, new IBAN and new installment in one email: enneo handles all of it in one pass with one reply. According to Microsoft's docs, its agent detects the intent of the email and calls the matching agent. For emails with two requests, Microsoft recommends rules for the order.
- **Attachments and photos:** enneo reads PDFs and photos, e.g. a meter photo. Attachments are not mentioned in Microsoft's documentation on email handling.
- **Ready for utilities:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. Microsoft learns intents from past cases and conversations. We found no ready-made energy processes.
- **Storage with a German provider:** enneo stores data at Hetzner, on-premises if desired. Microsoft keeps data within the EU Data Boundary. The email AI, however, requires allowing data for AI features to move between regions.

## Business-Impact

| With enneo | Outcome for the customer | How to say it |
|---|---|---|
| **Agent workspace, AI, knowledge and telephony in one** | One contract instead of user license plus credits plus telephony, costs easier to plan | "With us, agent workspace, AI agents, knowledge and telephony are one system with package prices per ticket and voice minute." |
| **Multiple requests in one pass** | Fewer follow-up questions and follow-up emails, one reply to the customer | "Meter reading, new IBAN and installment in one email: we handle it in one pass with one reply." |
| **Reading attachments and photos** | Nobody has to type up meter photos and PDFs anymore | "Our AI reads the meter photo and the attached PDF right along with the email." |
| **Ready-made specialist agents for utilities** | Shorter project, standard cases run without custom development | "We bring meter reading, installment and bank details as ready-made agents with plausibility checks. Only the connection to your ERP gets built." |
| **Storage with a German provider** | Privacy review without having to clarify data movement between regions | "We store data at Hetzner in Germany, and if you want EU language models, you get them under the DPA." |

## Wo Microsoft vorn liegt

- **Contact center and telephony:** Voice agents from Copilot Studio in the voice channel, German (de-DE) supported for voice dialog, context via SIP headers inbound and outbound, Teams Phone as telephony. With us, no context arrives from SIP headers on inbound calls, and Teams only via SIP.
- **Workforce management and quality:** Workforce Management with forecasting and shift planning generally available since Jun 30, 2026, included in Customer Service Enterprise and Premium. Plus a Quality Evaluation Agent that scores cases and conversations.
- **Certifications:** ISO 27001, SOC 2 and BSI C5. We have none of our own.
- **Microsoft ecosystem and testing tools:** Outlook inboxes, Dataverse, Power Platform connectors. The case agent can be simulated on up to 100 past cases and tested in shadow mode (both in preview).
- **Intents from history:** The Customer Intent Agent analyzes conversations up to two months old and suggests new intents from them daily.

## Unterschiede auf einen Blick

| Area | Topic | enneo | Microsoft | Assessment |
|---|---|---|---|---|
| Kanäle | **Voice services on the phone** | Voicebot via OpenAI (USA) or Deepslate (EU) | Voice agents from Copilot Studio, de-DE, context via SIP headers [Voice agents](https://learn.microsoft.com/en-gb/dynamics365/customer-service/voice-channel-ivr-bots) [Languages](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-supported-languages) | Microsoft vorn |
| KI & Automatisierung | **AI handling of emails** | One AI reads, identifies the customer, posts and replies, fully automated if desired | Since Sep 30, 2026: detect intent, answer from knowledge, autonomous or with approval. Actions via custom agents or connectors [Email docs](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-email-resolution) [Announcement](https://mc.merill.net/message/MC1465523) [Custom agents](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/case-management-agent-integration) | enneo vorn |
| KI & Automatisierung | **Multiple requests in one email** | Everything in one pass, one reply | One intent per email described, double requests via rules for the order [Email docs](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-email-resolution) [Intent Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-customer-intent-agent) | enneo vorn |
| KI & Automatisierung | **Reading attachments and photos** | PDFs and photos, e.g. meter photo | Not mentioned in the email handling docs [Email docs](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-email-resolution) | enneo vorn |
| KI & Automatisierung | **Ready-made processes for utilities** | Meter reading, installment, bank details ready-made, ERP connection per customer | Intents learned from past cases, no energy processes found [Intent Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-customer-intent-agent) | enneo vorn |
| KI & Automatisierung | **Building and testing AI agents** | Describe in plain language, change via chat with Neo, test cases | Instructions per intent, Copilot Studio, simulation on 100 cases, shadow mode (preview) [Intent Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-customer-intent-agent) [Case agent](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-case-resolution-agent) | gleich |
| Arbeitsplatz & Anbindungen | **One product** | Agent workspace, AI, knowledge, telephony in one system | Customer Service, Contact Center, Copilot Studio, credits via Azure, telephony separate [Email docs](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-email-resolution) [CS pricing](https://www.microsoft.com/de-de/dynamics-365/products/customer-service/pricing) [Copilot Studio pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio) | enneo vorn |
| Arbeitsplatz & Anbindungen | **Building integrations** | As code, any format, any logic | Power Platform connectors and custom connectors, up to 30 per Intent Agent [Intent Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-customer-intent-agent) | je nach Fall |
| Arbeitsplatz & Anbindungen | **Workforce management and quality** | No WFM, scorecards | WFM included in Enterprise and Premium, Quality Evaluation Agent [WFM blog](https://www.microsoft.com/en-us/dynamics-365/blog/?p=202503) | Microsoft klar vorn |
| Daten & Sicherheit | **Where data is stored** | Hetzner, German provider, on-premises possible | EU Data Boundary, US company, Flex Routing possible at peak load [AI data flow](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot) [Regions](https://learn.microsoft.com/en-us/power-platform/admin/regions-overview) | je nach Fall |
| Daten & Sicherheit | **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001, SOC 2, BSI C5 [ISO 27001](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001) [BSI C5](https://learn.microsoft.com/en-us/compliance/regulatory/offering-c5-germany) | Microsoft klar vorn |
| Preis & Vertrag | **Price** | Package prices per ticket and voice minute (pricing model 2.2) | License per user, AI and telephony billed by usage on top [CS pricing](https://www.microsoft.com/de-de/dynamics-365/products/customer-service/pricing) [CC pricing](https://www.microsoft.com/de-de/dynamics-365/products/contact-center/pricing) [Copilot Studio pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio) | je nach Fall |

## Wo Microsoft schwächer ist

- **New and partly in preview:** Email handling without a case was still listed as preview in the docs in July 2026, generally available since Sep 30, 2026. Simulation and shadow mode are still in preview. We found no public references for AI email handling in energy or insurance in the DACH region.
- **Costs hard to predict:** License per user, plus Copilot Credits by usage via an Azure subscription, plus telephony via Azure Communication Services. Simulations and shadow mode also consume credits.
- **One language per email handling setup:** For email handling you choose one fixed language for all emails. If the case agent finds no valid language, it hands off to agents. Voice dialog on the phone lacks de-AT and de-CH.
- **Data flow needs explaining:** A prerequisite is approval to move data for AI features between regions. Flex Routing has been on by default for new tenants since Mar 25, 2026 and allows processing outside the EU at peak load.

## Einwände

- **"We already have Microsoft 365 and Dynamics, we don't want another system."** Understandable. But for autonomous email handling, Microsoft also needs several building blocks: Customer Service, the Intent and Case agents, credits via Azure and custom agents in Copilot Studio. Check how much of that is already licensed. With us, it is one system.
- **"We have a Copilot license, it already writes emails."** That is a writing assistant for agents. At enneo, the AI reads the email, identifies and verifies the customer, posts in the target system and replies, without agents if desired. Drafts and summaries for agents are available with us on top.
- **"Microsoft has ISO 27001, SOC 2 and C5, you don't."** That's true, we have no certifications of our own. ISO 27001 and SOC 2 are in progress, and Hetzner is ISO 27001 certified. In return, our DPA, TOMs, subprocessors and SLA are public, and data is stored with a German provider.

## Fragen an den Kunden

- **Which licenses, agents and Azure credits do you need at Microsoft for a fully automated email reply with posting, and what does that cost at your volume?** Expected answer: Unclear, because credits are billed by usage and actions in Copilot Studio have to be built first. Transition: "Let's put that side by side: with us it is one system with package pricing per ticket."
- **What does the Microsoft agent do with an email that contains a meter reading, a new IBAN and an installment at the same time?** Expected answer: It detects one intent, double requests need rules for the order. Transition: "With us, one resolution plan covers all requests and one reply goes out, fully automated if desired."
- **Does the Microsoft agent read attachments like meter photos or PDFs for you?** Expected answer: Unclear, it is not described in the email handling docs. Transition: "Our AI reads photos and PDFs along with the email. We're happy to show you on a real email."

## Intern

- **Copilot license as price anchor:** A prospect (telecommunications, Dynamics as CRM) compared the price per automatically handled email with his group-wide Microsoft Copilot license: "It already writes me pretty nice emails." He also asked whether our Copilot is the one from Microsoft. *Attio call, Nov 5, 2026, min. 89:40*
- **Lost to Dynamics on price:** A prospect with Dynamics as CRM compared a Dynamics offer of around €30,000 with around €40,000 at enneo. The AI was not included in the Dynamics price, but the counter-calculation never reached the board, and the deal was lost. *Attio call, Sep 9, 2026, min. 19:01*
- **Teams as a hurdle:** At one prospect (education provider), most conversations run via Teams. Live recommendations during Teams calls are not possible because Microsoft does not release the audio stream. One participant: "in this ecosystem Microsoft doesn't let anyone in either". *Attio call, Oct 6, 2026, min. 42:49*

## Fazit

Where Microsoft 365 and Dynamics are already in place, we won't win on telephony, workforce management, certifications or ecosystem. We can win where a lot of written correspondence with multiple requests and attachments has to be handled through to posting, especially for energy cases. Against Microsoft, it helps to compare how many licenses, agents and components the same flow requires.

## Direktlinks

- [Doku](https://learn.microsoft.com/en-us/dynamics365/customer-service/)
- [API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview)
- [Community](https://community.dynamics.com/)
- [Trust Center](https://www.microsoft.com/en-us/trust-center)
- [Preise](https://www.microsoft.com/de-de/dynamics-365/products/contact-center/pricing)
- [Release Notes](https://learn.microsoft.com/en-us/dynamics365/customer-service/implement/whats-new-customer-service)
- [Status](https://status.cloud.microsoft/)

## Quellen

- [Set up email handling](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-email-resolution)
- [Case agent: resolving cases](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-case-resolution-agent)
- [Case agent with Copilot Studio agents](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/case-management-agent-integration)
- [Customer Intent Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-customer-intent-agent)
- [General availability announcement](https://mc.merill.net/message/MC1465523)
- [Customer Service pricing](https://www.microsoft.com/de-de/dynamics-365/products/customer-service/pricing)
- [Contact Center pricing](https://www.microsoft.com/de-de/dynamics-365/products/contact-center/pricing)
- [Copilot Studio pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio)
- [Data flow for AI features](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot)
- [Regions](https://learn.microsoft.com/en-us/power-platform/admin/regions-overview)
- [Voice agents in the voice channel](https://learn.microsoft.com/en-gb/dynamics365/customer-service/voice-channel-ivr-bots)
- [Languages in the voice channel](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-supported-languages)
- [Workforce management and quality](https://www.microsoft.com/en-us/dynamics-365/blog/?p=202503)
- [ISO 27001](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001)
- [BSI C5](https://learn.microsoft.com/en-us/compliance/regulatory/offering-c5-germany)
- [Facts about Microsoft](https://news.microsoft.com/facts-about-microsoft/)
- [Microsoft CRM since January 2003](https://news.microsoft.com/?p=4043)
- [Introduction of Dynamics 365 Copilot (March 2023)](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2023/03/06/introducing-microsoft-dynamics-365-copilot-bringing-next-generation-ai-to-every-line-of-business/)
