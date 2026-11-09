---
slug: "enterprisebot"
stand: "2026-11-09"
kurz: "Swiss AI platform for voice, email and chat"
---

## Eckdaten

| | | |
|---|---|---|
| Firma | **Zurich, 51 to 200 employees** | Enterprise Bot GmbH, Dufourstrasse 22, Zurich. Further offices in Bengaluru (development), Barcelona, Warsaw, London and Dover (US). In 2022 a total of USD 2.25m in capital, led by FiveT Fintech |
| Gegründet | **2016** | According to its own blog, founded in 2016 by Pranay Jain, Ravina Mutha and Sandeep Jayasankar. In 2019, Startupticker gave 2017 as the year and Zug as the place of founding |
| Ursprung | **AI from the start** | According to Startupticker, in 2019 the startup was building chatbots, an AI scheduling assistant and bots for sorting emails, already with SBB as a customer |
| Preise | **not public** | No price list, demo on request only. SourceForge mentions a trial version |
| Hosting | **selectable, including on-prem** | Managed hosting in the EU, Middle East, North America or Asia, plus own VPC or own data center. Kubernetes on AWS, Google Cloud or Azure in the EU or US. Operator of the standard hosting not named |
| Zertifikat | **SOC 2 according to website** | Logos for SOC, PCI DSS, HIPAA and "GDPR ready". No report, no Trust Center, ISO 27001 not found |

## Erster Satz

"Enterprise Bot is strong at voicebots in Swiss German and at connecting to existing contact centers. Email is where we come in: with us, one AI handles it from arrival to the booking in the target system, even with multiple requests in one reply."

## Das Wichtigste vorweg

Enterprise Bot is a Swiss vendor of AI agents for voice, email and chat, with references mainly at Swiss insurers, hospitals and transit companies. It is strong on speech services, model choice, on-premises operation and integration with Genesys, NICE or Luware. It does not describe a ticketing workspace of its own and sits on top of existing contact centers. For email, the public evidence covers sorting, reply drafts and a share of fully automated replies. Booking in the target system and multiple requests in one email are not documented.

## Unsere Verkaufsargumente

- **Email AI all the way into the target system:** With enneo, the AI recognizes the request and the customer, books in the ERP and replies, fully automated if desired. Enterprise Bot's email product ERA does mention full automation, but the public email references show sorting, drafts and, at BCD WTS, 21.4% of requests fully automated, with deeper integration into business systems only listed as an outlook.
- **Multiple requests, one reply:** enneo handles a meter reading, a new IBAN and a new installment in one email in a single pass with one reply. We found nothing on this for Enterprise Bot.
- **One system instead of an add-on:** With enneo, agent workspace, inbox, AI agents, knowledge, telephony and voicebot are one product with skill routing. Enterprise Bot builds on an existing contact center or CRM, and the website does not describe a ticketing workspace of its own.
- **Data protection you can read up on:** Our DPA, TOMs, subprocessors and SLA are public, and data is stored at Hetzner in Germany. At Enterprise Bot, the privacy policy names neither the storage location nor the subprocessors.
- **For utilities in addition:** Meter reading, installment and bank details are ready-made AI agents with plausibility checks at enneo. We did not find an energy reference from Enterprise Bot.

## Business-Impact

| With enneo | Outcome for the customer | How to say it |
|---|---|---|
| **Emails all the way to the booking in the ERP** | Standard cases run entirely hands-off, fewer agents needed for written correspondence | "With us, the email doesn't end with a draft. It ends with the booking in the ERP and the reply." |
| **All requests in one pass** | One complete reply instead of follow-up questions and follow-up tickets | "If your customer puts a meter reading, an IBAN and an installment into one email, they get one reply from us." |
| **One system for AI and team** | One contract and one system for tickets, AI and telephony, one point of contact | "Workspace, AI agents, knowledge and telephony are one product with us." |
| **Data protection documents public** | Data protection review without follow-up requests, because everything is available up front | "You can already read our DPA, TOMs, subprocessors and SLA yourself today." |
| **Storage in Germany** | Less back-and-forth with data protection and the works council on where data is stored | "Data is stored at Hetzner in Germany, with backups in Germany and Finland." |
| **Ready-made utility agents** | Meter reading, installment and bank details go live faster, only the ERP integration is built | "We bring the most important utility workflows ready-made, with plausibility checks." |

## Wo Enterprise Bot vorn liegt

- **Voicebot in Swiss German and many speech services:** At Generali Switzerland, the voicebot "Leonie" runs in Swiss German, according to the case study with 97 to 98% speech understanding and 22% fewer misroutes. Speech recognition and speech output are interchangeable (Deepgram, Google, Microsoft, ElevenLabs, Amazon Polly, Azure). With OpenAI and Deepslate, we have fewer options.
- **Integration with existing contact centers:** Genesys Cloud and Engage via AppFoundry, NICE CXone, Luware Nimbus with Microsoft Teams, Vier, Salesforce and BSI CRM. We have no native Teams integration, telephony only via SIP.
- **Free choice of operation and models:** SaaS, own VPC or Kubernetes in your own data center. Models from OpenAI, Google, Amazon Bedrock or your own open-source models. We offer on-premises only for large volumes.
- **References at Swiss insurers and hospitals:** Generali, SWICA, Kantonsspital Winterthur, plus the service provider Callpoint (around 600 employees) with 60% less onboarding time for new agents. According to its own homepage, G2 4.7 and Capterra 4.5.
- **Certification logos:** SOC, PCI DSS and HIPAA on the website. We have no certification of our own, ISO 27001 and SOC 2 are in progress.

## Unterschiede auf einen Blick

| Area | Topic | enneo | Enterprise Bot | Assessment |
|---|---|---|---|---|
| Kanäle | **Voicebot and speech services** | OpenAI or Deepslate (EU) | Many interchangeable providers (Deepgram, Google, Microsoft, ElevenLabs, Polly, Azure), Swiss German in production [Voicebot AIVA](https://www.enterprisebot.ai/products/voice-bot) | Enterprise Bot vorn |
| KI & Automatisierung | **Email through to action in the target system** | Full process through to booking and reply, fully automated if desired | ERA mentions draft, co-pilot or full automation. References: sorting and drafts (RMV), 21.4% fully automated and deeper integration as an outlook (BCD WTS) [ERA](https://www.enterprisebot.ai/products/email-response-automation) [Case RMV](https://www.enterprisebot.ai/case_study/rmv-0) [Case BCD](https://www.enterprisebot.ai/case_study/bcd-wts) | enneo vorn |
| KI & Automatisierung | **Multiple requests in one email** | One resolution plan, one reply | not found [ERA](https://www.enterprisebot.ai/products/email-response-automation) | enneo vorn |
| KI & Automatisierung | **Attachments and photos** | PDFs and photos, e.g. meter photo | PDFs, scans and screenshots via OCR [ERA](https://www.enterprisebot.ai/products/email-response-automation) | gleich |
| KI & Automatisierung | **Language models** | US providers, EU models possible under the DPA | OpenAI, Gemini, Bedrock or your own models [Technology](https://www.enterprisebot.ai/technology) | Enterprise Bot vorn |
| KI & Automatisierung | **Energy workflows** | Ready-made agents for meter reading, installment, bank details | No energy reference found [Case studies](https://www.enterprisebot.ai/case_study) | enneo klar vorn |
| Arbeitsplatz & Anbindungen | **Own agent workspace** | Ticketing, inbox, AI and telephony in one system | Add-on to existing contact centers and CRMs without a new interface. Live chat for agents, ticketing not found [Live Chat](https://www.enterprisebot.ai/products/live-chat) [Homepage](https://www.enterprisebot.ai) | enneo vorn |
| Arbeitsplatz & Anbindungen | **Contact center integration** | SIP, no native Teams integration | Genesys, NICE, Luware with Teams, Vier [Technology](https://www.enterprisebot.ai/technology) [Voicebot AIVA](https://www.enterprisebot.ai/products/voice-bot) | Enterprise Bot klar vorn |
| Daten & Sicherheit | **On-premises** | For large volumes | SaaS, VPC or own data center [Technology](https://www.enterprisebot.ai/technology) | Enterprise Bot vorn |
| Daten & Sicherheit | **Data protection documents** | DPA, TOMs, subprocessors, SLA public | Privacy policy without storage location or subprocessors [Privacy](https://get.enterprisebot.ai/legal/privacy-policy) | enneo klar vorn |
| Daten & Sicherheit | **Certifications** | None of our own, ISO 27001 and SOC 2 in progress | SOC 2 mentioned, logos for SOC, PCI DSS and HIPAA, report not public [Technology](https://www.enterprisebot.ai/technology) [Logos](https://www.enterprisebot.ai/hubfs/Group%20304%202.png) | Enterprise Bot vorn |

## Wo Enterprise Bot schwächer ist

- **Email references without booking:** At RMV, the email bot sorts requests and suggests drafts, with 86% accuracy in testing, and the case study only announces the launch. At BCD WTS, 21.4% of requests are fully automated after three months, and deeper integration into business systems is listed under outlook. We did not find a reference with booking in the target system.
- **Little that can be verified publicly:** No prices, no public documentation, no release notes. Several product pages still contain placeholder text ("Lorem Ipsum"), and the language figures vary between "50+" and "over 100".
- **Data protection only as a logo:** Certifications appear as logos without a report. The privacy policy names neither a company with an address nor a storage location, subprocessors or a DPA.
- **Little DACH outside Switzerland:** The only German reference is RMV (transit). Utilities don't appear on the website. According to join.com, six of seven open positions are in Bengaluru.

## Einwände

- **"Enterprise Bot can do email, chat and voice too."** True, all three channels are on offer, and voice is very strong there. For email, the public evidence is mainly sorting and reply drafts, with only a share of requests fully automated. Ask for a reference where emails with multiple requests run all the way to the booking in the target system.
- **"Enterprise Bot is SOC 2 certified, you're not."** The website shows the logo, and that's an advantage. On our side, ISO 27001 and SOC 2 are in progress, and Hetzner is ISO 27001 certified. In return, our DPA, TOMs, subprocessors and SLA are public, so your data protection team can review them right away.
- **"They work for Generali and SWICA, those are big names."** Those are good references, especially for voicebot and chat in Switzerland. We did not find a reference there for automated email handling or for utilities. That is exactly where our focus lies.

## Fragen an den Kunden

- **Which reference did Enterprise Bot show you where emails are booked into the target system without an agent?** Expected answer: more like sorting and drafts, or voice examples. Transition: "With us, you see that live with your own sample emails, from arrival to booking."
- **How does Enterprise Bot handle an email with three requests and a photo attached?** Expected answer: there's no clear statement on that yet. Transition: "We'd be happy to show you that with a real example."
- **Do you already have the DPA, subprocessor list and SOC 2 report, and where will your data be stored?** Expected answer: no, only on request. Transition: "Our documents are public, and data is stored at Hetzner in Germany."

## Intern

No internal insights in Attio yet (as of Nov 5, 2026).

## Fazit

Against Enterprise Bot, we don't win on a Swiss German voicebot, speech services, deployment options or integration with an existing contact center. We can win where a lot of written correspondence should be handled automatically all the way into the target system, with multiple requests, attachments and an agent workspace of its own in one product. With utilities and with customers who want to review data protection documents up front, we have a clear advantage.

## Quellen

- [Homepage](https://www.enterprisebot.ai)
- [Homepage in German](https://www.enterprisebot.ai/de/)
- [About us](https://www.enterprisebot.ai/company/about)
- [Legal notice](https://www.enterprisebot.ai/impressum)
- [Privacy policy](https://get.enterprisebot.ai/legal/privacy-policy)
- [Certification logos](https://www.enterprisebot.ai/hubfs/Group%20304%202.png)
- [Technology](https://www.enterprisebot.ai/technology)
- [Email automation ERA](https://www.enterprisebot.ai/products/email-response-automation)
- [Voicebot AIVA](https://www.enterprisebot.ai/products/voice-bot)
- [Live Chat](https://www.enterprisebot.ai/products/live-chat)
- [Agentic AI](https://www.enterprisebot.ai/products/agentic-ai)
- [Insurance](https://www.enterprisebot.ai/solutions/insurance-ai)
- [Case study Generali](https://www.enterprisebot.ai/case_study/generali_voice-0)
- [Case study RMV](https://www.enterprisebot.ai/case_study/rmv-0)
- [Case study SWICA](https://www.enterprisebot.ai/case_study/swica)
- [Case study Kantonsspital Winterthur](https://www.enterprisebot.ai/case_study/ksw)
- [Case study Callpoint](https://www.enterprisebot.ai/case_study/callpoint)
- [Case study BCD WTS](https://www.enterprisebot.ai/case_study/bcd-wts)
- [Case study SIX](https://www.enterprisebot.ai/case_study/six)
- [All case studies](https://www.enterprisebot.ai/case_study)
- [Funding 2022](https://enterprisebot.ai/blog/funding-raise)
- [Blog](https://www.enterprisebot.ai/blog)
- [Jobs on join.com](https://join.com/companies/enterprisebot)
- [Press release Advisory Board 2024](https://www.pressetext.com/news/20240701017)
- [Startupticker 2019: SBB chatbot](https://www.startupticker.ch/en/news/april-2019/sbb-answers-ticketing-questions-via-chatbot)
- [SourceForge](https://sourceforge.net/software/product/Enterprise-Bot/)
