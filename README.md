# Cybersecurity Analytics Portfolio

Hands-on projects in **network forensics, SIEM operations and machine learning for security**, completed in CYBER 362 (Cybersecurity Analytics) at Penn State.

Each folder is a self-contained case study: the problem, the tools and method, the findings and what I took away from it.

## Projects

| # | Project | What I did | Tools |
|---|---|---|---|
| 01 | [Adware Incident Investigation](01-adware-incident-investigation/) | Four-person team investigation of a 62-hour, 1.4M-packet capture. I traced the adware infection from install to beaconing to cleanup. Teammates Steven Johnson, Allen Bejoy and Hunter Hayes covered the network-hygiene findings. | Wireshark, Python, pandas |
| 02 | [Malware Traffic Analysis](02-malware-traffic-analysis/) | Identified infected Windows hosts in two packet captures and recovered malware downloads that were disguised as images. | Wireshark, Kerberos/NBNS/DHCP analysis |
| 03 | [SMS Spam Classifier](03-sms-spam-classifier/) | Built and compared TF-IDF + Logistic Regression and Decision Tree classifiers on 5,574 SMS messages. | Python, scikit-learn, pandas, seaborn |
| 04 | [Splunk SIEM](04-splunk-siem/) | Loaded web-store access logs into Splunk, then wrote SPL searches, enriched events with lookups, and built reports and a dashboard. | Splunk Enterprise, SPL |

## Skills shown

- **Network forensics:** packet capture triage, display filters, protocol hierarchy and conversation analysis, HTTP object export, identifying hosts and users from NBNS, DHCP and Kerberos traffic, spotting executables by their `MZ` header
- **Threat detection:** C2 beaconing analysis, IOC extraction, PUP/adware behavior, insecure protocol findings (SSLv2/v3, cleartext tokens, WPAD/LLMNR exposure)
- **SIEM:** Splunk data onboarding, SPL (`stats`, `top`, `chart`, `eval`, `lookup`, subsearches), reports and dashboards
- **Machine learning for security:** text classification with TF-IDF; evaluating models with confusion matrices, precision, recall and F1; why accuracy misleads on imbalanced data
- **Reporting:** writing incident findings with severity, evidence and recommendations

## Safety note

Packet captures are **not** included in this repo because they contain live malware samples. Malicious domains, URLs and IPs in the write-ups are defanged (`hxxp://`, `example[.]com`) so they can't be clicked by accident.

## Academic note

This is coursework. Project 01 was a team effort, and each teammate's contribution is credited in that project's README. Projects 02–04 were individual labs. The write-ups describe our methods and findings. Course-provided starter code and assignment text are not reproduced here.
