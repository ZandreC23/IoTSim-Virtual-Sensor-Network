# Stakeholder Analysis: IoTSim - Virtual Sensor Network Simulator

## Overview
For this assignment, I had to identify who would actually use or care about my IoT simulator project. I spent time thinking about different people who would interact with the system. I also asked a few classmates who work with IoT stuff and looked at online forums to understand what developers really struggle with when testing IoT applications. I ended up with 7 stakeholders. Some of them have conflicting needs which was interesting to figure out.

---

## Stakeholder Analysis Table

| ID | Stakeholder | Role | Key Concerns | Pain Points | Success Metrics |
|----|-------------|------|--------------|-------------|-----------------|
| S1 | IoT Developer | Uses simulated data to test IoT apps | • Data needs to feel realistic so tests are meaningful<br>• Should be able to simulate rare events like extreme temperatures<br>• Easy to connect to existing test code | • Don't have physical sensors during development<br>• Can't test edge cases because they don't happen naturally<br>• Buying sensors just for testing is expensive | • Can generate 3 different sensor types<br>• Dashboard updates within 2 seconds<br>• Can run 10+ sensors at once |
| S2 | Software Tester | Runs tests to catch bugs | • Tests should be repeatable every time<br>• Need predictable data for regression testing<br>• Should be easy to verify if outputs are correct | • Random data makes tests flaky and unreliable<br>• Hard to automate tests when data changes each run | • Same simulation produces identical data every time<br>• Tests finish in under 5 minutes<br>• 100% of data generation code is tested |
| S3 | System Administrator | Installs and maintains the system | • Installation should be quick and simple<br>• Shouldn't need lots of extra software<br>• Easy to see if something breaks | • Complex setups with databases are hard to maintain<br>• Configuration files scattered everywhere makes updates messy | • Install takes less than 10 minutes<br>• Works on Windows and Linux<br>• All errors go to one log file |
| S4 | Product Manager | Shows demo to clients, plans features | • Can quickly show working product to potential clients<br>• Real-time charts look impressive<br>• Easy to add new sensor types when clients ask | • Hard to demo IoT concepts without actual hardware<br>• Static data looks boring in demos<br>• Clients want to see live updates | • Can give full demo in under 5 minutes<br>• Add new sensor type in less than 1 hour<br>• Dashboard shows live updates |
| S5 | IT Department | Makes sure system is secure | • No security vulnerabilities<br>• No external services that need approval<br>• Should work without internet | • Installing message queues requires security review which takes weeks<br>• Cloud dependencies create compliance problems | • Works without internet connection<br>• All data stays on local machine<br>• Zero calls to external APIs |
| S6 | Academic Instructor | Teaches students with this project | • Clear documentation students can understand<br>• Shows complete end-to-end data pipeline<br>• Code is well-organized and separated | • Students struggle when architecture is too complex<br>• Hard to explain message queues to beginners | • Documentation covers everything clearly<br>• Architecture diagrams make sense<br>• Total code under 200 lines |
| S7 | Researcher | Uses system for experiments | • Can change simulation parameters easily<br>• Need to export data for analysis<br>• Experiments must be reproducible | • Changing sensor behavior requires modifying code<br>• Exporting data takes manual work | • All parameters in config file<br>• Data automatically saves to CSV<br>• Full experiment logs are saved |

---

## Stakeholder Priorities Summary

After analyzing everyone, I realized that developers and testers are the most critical users because without them the system wouldn't be used. IT department is also high priority because if they reject the system, it never gets deployed.

| Priority | Stakeholder | Key Requirement |
|----------|-------------|-----------------|
| Critical | IoT Developer | Realistic and configurable sensor data |
| Critical | Software Tester | Repeatable and predictable data |
| High | System Administrator | Simple installation and minimal dependencies |
| High | IT Department | Works offline with no external services |
| Medium | Product Manager | Quick demos and live dashboard |
| Medium | Academic Instructor | Clear documentation and simple code |
| Low | Researcher | Configurable parameters and data export |

---

## Stakeholder Conflicts I Had to Figure Out

| Conflicting Needs | How I Solved It |
|-------------------|-----------------|
| **Tester** wants predictable data (same every run) vs **Developer** wants realistic random data | I added a setting in the config file called `deterministic_mode`. When true, data is the same every time. When false, it's random. This way both get what they need. |
| **IT Department** wants no extra software vs **Product Manager** wants nice charts | I picked Streamlit for the dashboard because it installs with just `pip` and CSV for storage because it's already in Python. No databases or message queues needed. |
| **System Admin** wants simple monitoring vs **Product Manager** wants fancy visuals | I separated this: the dashboard handles visuals for demos, and errors just go to a simple log file for the admin to check. |

---

## Traceability to Requirements

I used this table to make sure every requirement I wrote later would actually address someone's needs. This helped me not waste time on features nobody asked for.

| Requirement Type | Stakeholders |
|------------------|--------------|
| Sensor simulation (FR-01 to FR-06) | S1, S2, S7 |
| CSV storage (FR-07 to FR-10) | S3, S5 |
| Dashboard (FR-11 to FR-16) | S1, S4, S6 |
| Performance (NFR-11 to NFR-13) | S1, S3 |
| Simplicity (NFR-04 to NFR-05) | S3, S5 |
| Documentation (NFR-06 to NFR-07) | S6 |

---

## What I Learned

Doing this stakeholder analysis taught me that requirements don't come out of nowhere. They come from real people with real problems. The IoT developer doesn't just want "sensor data" - they want realistic data because their tests fail with fake-looking numbers. The IT department doesn't just want "security" - they want no external services because getting approval takes forever.

Next time I would interview actual stakeholders instead of just imagining what they need. But for this project, I think I covered the main concerns.