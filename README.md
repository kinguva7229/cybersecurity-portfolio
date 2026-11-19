# Cybersecurity Analytics Portfolio

Hands-on projects in **network forensics, SIEM operations and machine learning for security**, completed in CYBER 362 (Cybersecurity Analytics) at Penn State.

Each folder is a self-contained case study: the problem, the tools and method, the findings and what I took away from it.

## Projects

| # | Project | What I did | Tools |
|---|---|---|---|
| 01 | [Adware Incident Investigation](01-adware-incident-investigation/) · [Report](01-adware-incident-investigation/REPORT.md) | Four-person team investigation of a 62-hour, 1.4M-packet capture. I traced the adware infection from install to beaconing to cleanup. Teammates Steven Johnson, Allen Bejoy and Hunter Hayes covered the network-hygiene findings. | Wireshark, Python, pandas |
| 02 | [Malware Traffic Analysis](02-malware-traffic-analysis/) · [Report](02-malware-traffic-analysis/REPORT.md) | Identified infected Windows hosts in two packet captures and recovered malware downloads that were disguised as images. | Wireshark, Kerberos/NBNS/DHCP analysis |
| 03 | [SMS Spam Classifier](03-sms-spam-classifier/) | Built and compared TF-IDF + Logistic Regression and Decision Tree classifiers on 5,574 SMS messages. | Python, scikit-learn, pandas, seaborn |
| 04 | [Splunk SIEM](04-splunk-siem/) | Loaded web-store access logs into Splunk, then wrote SPL searches, enriched events with lookups, and built reports and a dashboard. | Splunk Enterprise, SPL |

## Skills shown

- **Network forensics:** packet capture triage, display filters, protocol hierarchy and conversation analysis, HTTP object export, identifying hosts and users from NBNS, DHCP and Kerberos traffic, spotting executables by their `MZ` header
- **Threat detection:** C2 beaconing analysis, IOC extraction, PUP/adware behavior, insecure protocol findings (SSLv2/v3, cleartext tokens, WPAD/LLMNR exposure)
- **SIEM:** Splunk data onboarding, SPL (`stats`, `top`, `chart`, `eval`, `lookup`, subsearches), reports and dashboards
- **Machine learning for security:** text classification with TF-IDF; evaluating models with confusion matrices, precision, recall and F1; why accuracy misleads on imbalanced data
- **Incident reporting:** professional incident reports with executive summaries, timelines, severity ratings, MITRE ATT&CK mapping, impact assessments, recommendations and defanged IOCs

## Safety note

Packet captures are **not** included in this repo because they contain live malware samples. Malicious domains, URLs and IPs in the write-ups are defanged (`hxxp://`, `example[.]com`) so they can't be clicked by accident.

## Academic note and how this was made

This is coursework. Project 01 was a team effort, and each teammate's contribution is credited in that project's README. Projects 02–04 were individual labs.

- **The work:** the analysis, code and results were done by me, and for project 01 by my team, following the course instructions and the instructor's sample code.
- **This portfolio:** the READMEs and incident reports were written afterward with help from an AI assistant (Claude). They are based on our original submissions and add no new findings.
- **Not included:** course-provided starter code and assignment text.
