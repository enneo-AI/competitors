---
slug: "sap"
stand: "2026-11-05"
kurz: "SAP Service Cloud V2 with Joule agents, closely tied to S/4HANA Utilities"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **SAP SE** | Service Cloud Version 2 is SAP's new CRM. According to an SAP presentation (June 2026), 624 customers are live with Sales and Service V2, marked by SAP as not an official reference |
| Preise | **€97 + €58** | List price Service Cloud €97 per user per month, Utilities add-on for S/4HANA Utilities €58, term 3 to 36 months, quote on request. AI agents billed via AI Units, price per AI Unit not public |
| Hosting | **AWS Frankfurt** | Service Cloud V2 runs on AWS, data centers in Frankfurt, Sydney, Virginia and São Paulo |
| Zertifikat | **C5, SOC 2** | C5 report (Type 1, reference date Mar 31, 2024) and SOC 2 report 2024 H1 for Service Cloud V2, available only under NDA |

## Erster Satz

"SAP Service Cloud is strong if you want the tight connection to S/4HANA Utilities. The interesting question is who already handles your emails all the way to the booking today."

## Das Wichtigste vorweg

SAP plays at utilities running SAP IS-U or S/4HANA Utilities. Service Cloud V2 with the Utilities add-on shows contract account, installation and move-ins and move-outs directly in the case, and master data is synchronized with S/4HANA. On the AI side, what is publicly documented today is mainly assistance for agents: an email becomes a case, AI determines the case type, summarizes it and suggests a draft reply. SAP has announced agents that handle cases on their own for 2026. We have not found any public documentation on fully automated email handling.

## Unsere Verkaufsargumente

- **Fully automated email, today:** At enneo, the AI reads the email, identifies and verifies the customer, books in the target system and replies, even without agents. What SAP has publicly documented is AI case typing, a summary and a draft reply that an agent reviews. Agents for case handling appear in an SAP presentation with "General Availability Q2/Q3 2026", explicitly without commitment.
- **Multiple requests, attachments, photos:** Meter reading, new IBAN and new installment in one email: enneo handles all of it in one pass with one reply, and the AI also reads PDFs and meter photos. Neither is documented at SAP.
- **One product instead of a construction kit:** At enneo, agent workspace, AI agents, knowledge, telephony and voicebot are one system. At SAP, it is Service Cloud, the Utilities add-on, AI Units for Joule agents and a partner, Parloa, for voicebots.
- **Ready-made specialist agents for utilities:** Meter reading, installment and bank details with plausibility checks are ready at enneo. We build the connection to IS-U or S/4HANA per customer. According to ASUG, SAP's Utilities Customer Self-Service Agent knows contracts, tariffs and consumption. Which processes it completes and on which channels it runs is not publicly described.
- **Predictable AI costs:** enneo charges in packages per ticket and voice minute. SAP bills agents in AI Units per work step, a task takes several steps, and SAP does not disclose the price per AI Unit.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Fully automated email, today** | Standard requests go through without agents, instead of waiting for announced agents | "With us, the AI already books in the target system and replies today. At SAP, that is in a 2026 presentation with no commitment." |
| **Multiple requests and attachments in one pass** | Less rework and fewer follow-up questions on emails with meter reading, IBAN and photo | "An email with three requests and a meter photo, we handle in one pass with one reply." |
| **No new CRM required** | Automation starts without rolling out an entire system with its own master data sync | "You don't need to introduce a new CRM to automate your written correspondence." |
| **Packages per ticket instead of AI Units** | Predictable AI budget, no expiring unused units, no extra billing | "With us, you pay packages per ticket and voice minute, not work steps in AI Units that expire after twelve months." |
| **Telephony and voicebot in the same product** | One system and one contract instead of Service Cloud plus a partner for voice | "Phone and voicebot are in the same system with us. At SAP, the voicebot comes through a partner." |

## Wo SAP vorn liegt

- **Deep integration with S/4HANA Utilities:** Contract account with deposit, installation with move-ins and move-outs, search across contracts and installations, master data sync via ready-made iFlows. What we build per customer is part of the add-on at SAP.
- **AI on billing data:** Since Q4 2025, an AI explains consumption fluctuations between bills. An agent for billing exception cases (BPEM) was announced for Q2 2026. It suggests a solution, people decide.
- **Certifications:** C5 and SOC 2 for Service Cloud V2. We have none of our own.
- **Broad platform:** Service, sales, field service and Joule across all SAP systems. For voice and chat, Parloa has been an SAP Solution Extension since Oct 26, 2026, with SAP support.
- **Public list price per seat:** €97 per user for Service Cloud, €58 for the Utilities add-on. According to SAP, the basic AI features ("Base AI") are included in every cloud subscription at no extra cost.

## Unterschiede auf einen Blick

| Topic | enneo | SAP | Einordnung |
|---|---|---|---|
| **AI handling of emails** | An AI reads, identifies the customer, books and replies, also fully automated | Email becomes a case, AI case typing, summary, draft reply for review. Agents for case handling announced for 2026 | enneo klar vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Reading attachments and photos** | PDFs and photos, e.g. meter photo | Not documented | enneo vorn |
| **One product** | Agent workspace, AI, knowledge, telephony in one system | Service Cloud, Utilities add-on, AI Units, Joule agents, voice via partner | enneo vorn |
| **Where data is stored** | Hetzner, German provider, on-premises possible | AWS Frankfurt | enneo vorn |
| **Ready-made processes for utilities** | Meter reading, installment, bank details ready, ERP connection per customer | Self-Service Agent for contracts, tariffs, consumption, processes and channels not documented | je nach Fall |
| **Voicebot** | Own telephony or SIP, OpenAI (USA) or Deepslate (EU) | Via partner Parloa as SAP Solution Extension | je nach Fall |
| **Price for the AI** | Package prices per ticket and voice minute (pricing model 2.2) | 0.02 or 0.05 AI Units per agent step, price per unit not public, units expire after 12 months | je nach Fall |
| **Agent Assist** | Draft, summary, live transcription | Summary, draft reply, solution suggestions, translation | gleich |
| **Connection to S/4HANA Utilities** | Built per customer | Utilities add-on: contract account, installation, master data sync via iFlow | SAP klar vorn |
| **Certifications** | None of our own, in progress. Hetzner ISO 27001 | C5 and SOC 2 for Service Cloud V2 | SAP klar vorn |
| **Platform and ecosystem** | API, MCP, code tools per customer | Sales, field service, Joule across all SAP systems, partners like Parloa | SAP vorn |

## Wo SAP schwächer ist

- **Much announced, little proven:** The agents for case handling and self-service appear in presentations targeting Q2/Q3 2026, with the note that none of it is a commitment. Dates differ between sources, for the Utilities agent between Q4 2025 and February 2026.
- **AI costs hard to plan:** AI Units are consumed per agent step, expire after 12 months, and overages are billed afterwards. SAP does not publicly disclose the euro price per unit.
- **Little public documentation:** For the Utilities Customer Self-Service Agent there is a demo and an event, but no description of channels and processes. The audit reports are only available under NDA.
- **A CRM project:** Service Cloud V2 is a new CRM with its own master data sync to S/4HANA. Anyone who only wants to automate email handling ends up rolling out an entire system.

## Einwände

- **"We're an SAP shop, everything should go into Service Cloud."** Understandable. The connection to S/4HANA Utilities is part of the add-on at SAP and a per-customer project with us. The difference is what the AI handles today: with us, the email runs all the way to the booking. At SAP, agents for that have been announced.
- **"SAP brings its own AI agents with Joule."** Yes, announced for Q2/Q3 2026, with the note that this is not a commitment, and with dates that differ by source. What is publicly documented today is case typing, summary and draft reply. We'll show you fully automated handling on one of your own emails.
- **"At SAP, the AI is included in the subscription at no extra cost."** That is true for the basic features. SAP bills agents in AI Units per work step, does not publicly disclose the price per unit, and units expire after twelve months. With us, it's packages per ticket and voice minute.

## Fragen an den Kunden

- **Which emails does Service Cloud handle for you today without agents, all the way to the booking in IS-U or S/4HANA?** Expected answer: None, the AI suggests case type and reply, agents have been announced. Transition: "That exact step is what we do today. Let's show it on one of your emails."
- **What does an automatically handled email cost in AI Units, and what happens to units you don't use within the year?** Expected answer: The price per unit only appears in the quote, unused units expire after twelve months. Transition: "With us, you see the price per ticket up front in the package."
- **When will Service Cloud and Joule agents be in production for you, and who handles the written correspondence until then?** Expected answer: After the S/4HANA migration, the agents are announced, until then agents do the work. Transition: "With enneo, you automate email and letters without waiting for that. We build the connection to your SAP per customer."

## Intern

- **Service Cloud too big for many:** A partner (SAP consultancy for utilities) says not every SAP customer rolls out Sales and Service Cloud, because it is "quite expensive" and "quite big". Many stay with SAP interfaces without ticketing and without phone or channel integration. *Attio call, Feb 27, 2026, min. 6:56*
- **With Service Cloud, everything is supposed to go into one interface:** Same partner: whoever rolls out Service Cloud usually wants all agents to work in it. enneo would then have to plug in or work upstream. *Attio call, Feb 27, 2026, min. 6:08*
- **Chat and voice did not come from SAP:** For chatbots, the partner relied on another provider, "SAP doesn't deliver anything there anyway". As of February 2026, before the Parloa partnership. *Attio call, Feb 27, 2026, min. 7:50*
- **Customer service comes after S/4HANA:** A partner (SAP consultancy for utilities) observes that utilities first complete the S/4HANA migration and tackle customer service afterwards. Several municipal utilities are currently rolling out Sales and Service Cloud as part of this. *Attio call, Sep 2, 2026, min. 12:01*
- **Joule not that far yet, according to a partner:** A partner (SAP consultancy with its own AI) says Joule needs "about two more years", by their own account internal info from SAP. Not verifiable. *Attio call, Oct 29, 2026, min. 32:32*

## Fazit

SAP wins where a utility is rolling out Service Cloud V2 anyway and wants the tight connection to S/4HANA Utilities, and on certifications. We can win on fully automated handling of email and letters that works today, with multiple requests and attachments, and with telephony in the same product. With SAP customers, enneo alongside the SAP system is often the faster conversation than waiting for announced agents.

## Quellen

- [Service Cloud pricing](https://www.sap.com/germany/products/crm/service-cloud/pricing.html)
- [Service Cloud features](https://www.sap.com/products/crm/service-cloud/features.html)
- [SAP Business AI pricing and AI Units](https://www.sap.com/products/artificial-intelligence/pricing.html)
- [C5 report Service Cloud V2](https://www.sap.com/about/trust-center/certification-compliance/sap-sales-cloud-service-cloud-v2-c5-2024-h1.html)
- [SOC 2 report Service Cloud V2](https://www.sap.com/about/trust-center/certification-compliance/sap-sales-cloud-service-cloud-v2-soc-2-2024-h1.html)
- [Service Cloud with S/4HANA Utilities (SAP Learning)](https://learning.sap.com/courses/configuring-master-data-and-basic-functions-in-sap-s-4hana-utilities/attending-the-customer-with-service-cloud)
- [SAP presentation Autonomous Sales & Service (June 2026)](https://assets.dm.ux.sap.com/nl-sap-connect-day-for-cx-nl/pdfs/sap_autonomous_salesandservice_cx_connectday_nl.pdf)
- [Demo Utilities Customer Self-Service Agent](https://www.sap.com/assetdetail/2026/05/141be6bd-527f-0010-bca6-c68f7e60039b.html)
- [ASUG: Joule for utilities](https://www.asug.com/insights/sap-positions-joule-as-a-process-native-copilot-for-the-utilities-value-chain)
- [Joule agents at SAP Connect 2025](https://thelettertwo.com/2025/10/06/sap-joule-new-ai-agents-connect-2025/)
- [Joule Agents](https://www.sap.com/products/artificial-intelligence/ai-agents.html)
- [Parloa as SAP Solution Extension](https://www.parloa.com/de/presse/parloas-ai-agent-management-platform-ist-ab-sofort-als-sap-solution-extension-fuer-agentische-kundeninteraktionen-erhaeltlich/)
