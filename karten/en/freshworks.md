---
slug: "freshworks"
stand: "2026-11-05"
kurz: "Low-cost US helpdesk Freshdesk, AI agent Freddy billed per session"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **San Mateo, publicly listed** | Freshworks Inc., according to its own website 74,000+ customers, revenue Q3 2026: USD 245.4m |
| Preise | **€17 / €52 / €84** | Freshdesk Growth / Pro / Enterprise per agent per month, billed annually. AI agent Freddy: 500 sessions free once, then €45 per 100 sessions. Copilot €29 per agent |
| Hosting | **AWS, EU region selectable** | City not named, region can only be chosen when the account is created. AI via Microsoft Azure OpenAI (US and EU regions) |
| Zertifikat | **ISO 27001, SOC 2** | Plus ISO 27701, SOC 1 and SOC 3, CSA STAR Level 1. BSI C5 and ISO 42001 not found |

## Erster Satz

"Freshdesk is a good, low-cost helpdesk. The question is who resolves the cases in the emails, with attachments, multiple requests and the booking in the billing system."

## Das Wichtigste vorweg

Freshdesk is a broad, low-cost helpdesk, and the AI agent Freddy is billed per session. The email AI agent replies from the knowledge base and, according to the documentation, can call APIs through no-code workflows, so it can also write to third-party systems. Whether it reads attachments in customer emails and resolves multiple requests in one email is not stated anywhere in the documentation. Anyone working on Freshdesk today gets simple email automation there, but not a documented end-to-end journey like with enneo.

## Unsere Verkaufsargumente

- **Attachments and photos from the email:** enneo reads PDFs and photos, e.g. a photo of the meter. This is not documented for Freshdesk's email AI agent. According to the documentation, Freddy only processes files in the chat flow when it specifically asks for them, one file per step in the web widget.
- **Multiple requests, one reply:** enneo handles a meter reading, a new IBAN and a new installment in one email in a single pass with one reply. This is not described for Freshdesk. Freshworks even recommends testing "multi-part questions" as an edge case during setup.
- **APIs as code, preview without booking:** With enneo, any format and any logic is possible, and you see the solution plan before anything is booked. Freddy calls APIs without code, with JSON only. According to the documentation, test calls run with real values against the target system. For email, the confirmation step with the customer before an action is skipped, so safeguards have to be built at the API itself.
- **Ready for utilities:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. Freddy's 50+ ready-made workflows target retail (Shopify, Stripe, PayPal, FedEx, Wix). We did not find energy there.
- **Phone and email in one system:** enneo has its own telephony and voicebot. At Freshworks, phone AI runs through partners such as Synthflow or Squawkvoice, who bill separately.

## Business-Impact

| Difference | What it means for the customer | How to say it |
|---|---|---|
| **Attachments and photos from the email** | Nobody has to retype meter photos and PDFs anymore | "Our AI reads the meter photo in the attachment and takes over the value." |
| **Multiple requests, one reply** | Fewer follow-up questions and repeat contacts, one case instead of three | "enneo handles a meter reading, a new IBAN and a new installment in one email in a single pass with one reply." |
| **Preview without booking** | Less risk from incorrect bookings, no need to build your own safeguards at the API | "You see the solution plan and the extracted values before anything is booked." |
| **Ready-made workflows for utilities** | Shorter rollout, workflows don't have to be built from scratch | "Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo." |
| **Phone in the same product** | No partner product with separate billing to buy on top | "Voicebot and telephony are part of the same system as email and chat with us." |
| **German GmbH, storage in Germany** | Easier approval where a US company is not wanted | "We are a German GmbH and store data at Hetzner in data centers in Germany." |

## Wo Freshworks vorn liegt

- **Price and entry point:** Freshdesk from €17 per agent per month, AI sessions at €45 per 100. An email session covers 72 hours from the first customer email, and all AI replies within it count once. That's easy to calculate and inexpensive to start with.
- **Channels and customer portal:** The AI agent runs in inboxes, the customer portal and forms, and in chat also on WhatsApp, Instagram, Messenger, LINE, SMS and Apple Business Chat. We don't have a help center for end customers.
- **Certifications:** ISO 27001:2022, ISO 27701, SOC 1, SOC 2 and SOC 3. We have none of our own.
- **Ready-made building blocks for retail:** 50+ ready-made workflows, integrations with Shopify, Stripe, PayPal, FedEx and Wix, plus MCP actions. For retailers, Freddy is ready to go quickly.
- **Many customers, solid ratings:** 74,000+ customers according to Freshworks, 4.1 out of 5 on OMR from 47 reviews. Users praise value for money and ease of use.

## Unterschiede auf einen Blick

| Topic | enneo | Freshworks | Assessment |
|---|---|---|---|
| **AI handling of emails** | One AI reads, identifies the customer, books and replies, fully automated if desired | Reply from the knowledge base, APIs possible in email workflows, without confirmation before the action | enneo vorn |
| **Multiple requests in one email** | Everything in one pass, one reply | Not documented | enneo vorn |
| **Attachments and photos in customer emails** | PDFs and photos, e.g. a photo of the meter | Not documented for email. In chat up to 3 files of 25 MB each, one in the web widget | enneo vorn |
| **Building API integrations** | As code, any format, any logic | No code, REST with JSON or MCP, one authentication per action | enneo vorn |
| **Testing before booking** | Solution plan, extracted values, preview without booking | Test calls with real values, documentation recommends your own test environment | enneo vorn |
| **Ready-made workflows for utilities** | Meter reading, installment, bank details ready, ERP integration per customer | 50+ ready-made workflows for retail, energy not found | enneo vorn |
| **Multiple inboxes or brands** | One AI agent per inbox with its own salutation and its own knowledge | One active AI agent per inbox, up to 50 agents per account | gleich |
| **Voicebot** | Own telephony or the customer's SIP trunk | Phone AI via partners (Synthflow, Squawkvoice). Own voicebot English only according to the documentation | enneo vorn |
| **Where data is stored** | Hetzner, German provider, on-premises possible | AWS, EU region, US company, AI via Azure OpenAI | enneo vorn |
| **Price** | Package prices per ticket and voice minute (pricing model 2.2) | From €17 per agent, AI €45 per 100 sessions, public | Freshworks vorn |
| **Channels and help center** | Email, letter, chat, WhatsApp, Telegram, phone, no help center | Plus Instagram, Messenger, LINE, SMS, customer portal | Freshworks vorn |
| **Certifications** | None of our own, in progress. Hetzner ISO 27001 | ISO 27001, 27701, SOC 1, SOC 2, SOC 3 | Freshworks klar vorn |

## Wo Freshworks schwächer ist

- **Email AI thinly documented:** The setup page for the email AI agent describes replies from the knowledge base, handoff and closing tickets. It says nothing about attachments or multiple requests. Workflows in natural language exist only in early access, and the documentation for them mentions only chat.
- **No confirmation before actions via email:** In chat, Freddy can check with the customer before a sensitive action. According to the documentation, this step is skipped in email workflows. Anyone automating bookings via email has to build the safeguards themselves.
- **Operational limits:** Only tickets created after activation are handled. Once the daily limit is reached, the AI stops replying. A new ticket on the same topic starts without prior context.
- **Phone AI not from a single source:** No AI voicebot of Freddy's own is documented. According to the documentation, Freshcaller's older voicebot can only do English. Otherwise, partners with separate billing step in.

## Einwände

- **"Freshdesk is much cheaper."** On license price that's true, and Freshdesk is inexpensive to start with. But compare what happens after the ticket: Copilot and AI sessions cost extra at Freshworks, and phone AI runs through partners with separate billing. With enneo, inbox, AI agents and telephony are one product, billed in packages per ticket and voice minute.
- **"We already have Freshdesk, Freddy just gets added."** For replies from the knowledge base, Freddy is often enough. Test it on real emails with attachments and multiple requests, which Freddy is not documented for in email. That is exactly where enneo comes in, all the way to the booking in the target system.
- **"Freshworks is a large, publicly listed company."** That's a fair point, and Freshworks is also ahead on certifications. enneo is a German GmbH without investors, stores data at Hetzner in Germany, and the DPA, TOMs, subprocessors and SLA are public. Where a US company is not wanted, that often tips the balance.

## Fragen an den Kunden

- **What happens today with the meter photo or PDF attached to a customer email?** Expected answer: an agent opens the attachment and types in the value. Reading attachments is not documented for Freshdesk's email AI agent. Transition: "With us, the AI reads the value from the photo and books it."
- **How do you make sure the AI doesn't trigger an incorrect booking via email?** Expected answer: through your own checks at the API, because Freddy acts without confirmation in email workflows and test calls run with real values. Transition: "With enneo, you see the solution plan and the extracted values up front, with a preview without booking."
- **Who answers your calls, and should the AI also resolve cases there?** Expected answer: Freshcaller or a partner like Synthflow with separate billing. Transition: "With us, the voicebot runs in the same system as email and chat."

## Intern

- **Price anchor in the competition:** A prospect (telecommunications distribution, 45 service seats) had offers from Freshdesk and Zendesk at around €33k to €34k per year, and our offer was well above that. He called Freshdesk "cool, middle-of-the-road" and Zendesk the market leader. *Attio call, Jun 25, 2026, min. 4:28 and 14:27*
- **Price beats enthusiasm:** The same prospect was convinced by enneo but said a young company could not challenge Freshdesk "on price". The business case has to be in place before the price comes up. *Attio call, Jun 25, 2026, min. 14:54 and 22:22*
- **US company as a reason for exclusion:** A partner (Freshworks implementation partner) reports prospects, mostly from public authorities, who rejected Freshdesk because it is an American company. *Attio call, Oct 20, 2026, min. 53:28*
- **Freddy barely used in small projects:** The same partner sees Freshdesk mainly as a ticketing system for customers who don't have one yet. At one small customer, Freshdesk was rolled out in a stripped-down version, and AI features were barely used. *Attio call, Oct 20, 2026, min. 41:32 and 54:35*

## Fazit

Against Freshworks, we don't win on price, channels or certifications. We can win where emails with attachments and multiple requests should be resolved all the way to the booking in the target system, especially for energy cases. For teams working on Freshdesk today, it pays to compare on real emails: that is exactly where Freddy is not documented.

## Quellen

- [Freshdesk pricing](https://www.freshworks.com/de/freshdesk/pricing/)
- [Freshdesk Omni pricing](https://www.freshworks.com/freshdesk/omni/pricing/)
- [Freddy AI Agent](https://www.freshworks.com/freshdesk/omni/freddy-ai-agent/)
- [Setting up the email AI agent](https://support.freshdesk.com/en/support/solutions/articles/50000013867)
- [AI Agent Studio](https://support.freshdesk.com/support/solutions/articles/50000011711-freddy-ai-agent-studio-configure-automate-and-scale-with-ai)
- [API actions](https://support.freshdesk.com/support/solutions/articles/50000011661-connect-to-external-systems-using-api-actions)
- [Workflows for AI agents](https://support.freshdesk.com/support/solutions/articles/50000011733-workflows-for-ai-agents-in-freshdesk)
- [No-code workflows](https://support.freshdesk.com/support/solutions/articles/50000011782-build-workflows-no-code-agentic-workflows)
- [Workflows in natural language](https://support.freshdesk.com/support/solutions/articles/50000014312-write-ai-agent-workflows-with-natural-language-workflows)
- [Data storage](https://support.freshdesk.com/support/solutions/articles/196893-data-storage-and-data-security-in-freshdesk)
- [Data centers](https://support.freshdesk.com/support/solutions/articles/235810-where-is-your-data-servers-located-)
- [Subprocessors](https://www.freshworks.com/privacy/sub-processor/)
- [Trust Center](https://trust.freshworks.com/)
- [Voice AI via partners](https://crmsupport.freshworks.com/support/solutions/articles/50000011867-voice-ai-agent-integration-in-freshcaller)
- [Freshcaller voicebot](https://support.freshcaller.com/support/solutions/articles/50000001662)
- [About Freshworks](https://www.freshworks.com/company/about/)
- [Quarterly results Q3 2026](https://www.sec.gov/Archives/edgar/data/0001544522/000154452226000170/q326quarterlyearningsrelea.htm)
- [Freddy for email, press](https://itbrief.co.uk/story/freshworks-expands-freddy-ai-with-email-workflows)
- [User reviews](https://omr.com/de/reviews/product/freshdesk)
