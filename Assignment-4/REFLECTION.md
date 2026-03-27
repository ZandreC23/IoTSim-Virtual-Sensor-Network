# Reflection: Balancing Stakeholder Needs in IoTSim

## Assignment Information
- **Project:** IoTSim: Virtual Sensor Network Simulator
- **Student:** Zandre Coetzee
- **Date:** March 22, 2026

---

## 1. Overview

This assignment was about planning before building. I had to identify stakeholders, understand what they actually need, and write requirements that I will use when I start coding. The hardest part was realizing that different stakeholders want different things, and sometimes those things conflict. I ended up with 7 stakeholders and 29 requirements.

---

## 2. The Hardest Conflicts I Found

### Conflict 1: Testers Want Predictable Data, Developers Want Realistic Data

**The Problem:**
- The Software Tester (S2) needs data that is the same every time the simulation runs. This is for regression testing. If data changes, tests might fail for no reason.
- The IoT Developer (S1) needs data that looks real. Random numbers that follow realistic patterns. If the data is too predictable, tests might miss real-world bugs.

**How I Plan to Solve It:**
I will add a setting in the config file called `deterministic_mode`. When it's on, the random number generator will use a fixed seed so data repeats. When it's off, it will use a random seed. This way the same code can serve both users.

**What I Learned:**
One feature can serve two different users if you think about it the right way. I almost made this a separate "test mode" but realized a config flag is simpler.

---

### Conflict 2: IT Wants No Dependencies, Product Manager Wants Fancy Visuals

**The Problem:**
- IT Department (S5) said the system should have zero external dependencies. No databases, no message queues, no internet calls.
- Product Manager (S4) wants a dashboard with live charts that looks professional for demos.

**How I Plan to Solve It:**
I spent time researching different options. I found Streamlit. It installs with just `pip` and creates nice charts with very few lines of code. For storage, I will use CSV files because Python handles them natively. No database needed.

**What I Learned:**
"Zero dependencies" doesn't mean you can't use any libraries. It means you shouldn't require the user to install and configure complex software like MySQL or RabbitMQ. Python libraries that install with pip are usually fine.

---

### Conflict 3: Admin Wants Simple Monitoring, PM Wants Rich Dashboard

**The Problem:**
- System Administrator (S3) just wants to know if the system is running and if there are errors.
- Product Manager (S4) wants the dashboard to look impressive with multiple charts and colors.

**How I Plan to Solve It:**
I realized these don't actually conflict. The dashboard can be for demos, and I can add a simple log file for the admin. The admin doesn't need to look at the dashboard. They just need to check a log file occasionally.

**What I Learned:**
Sometimes conflicts exist because you assume one thing must serve everyone. When you separate concerns, the conflict disappears.

---

## 3. Other Trade-offs I Had to Consider

| Trade-off | My Plan | Why |
|-----------|---------|-----|
| Complex vs Simple | I will keep it simple | I only have 14 weeks. If I try to build a system with message queues and databases, I might not finish. CSV files are good enough for this project. |
| Scalability vs Simplicity | I will prioritize simplicity | The system only needs to run for demos and testing, not for real production. CSV can handle 10+ sensors easily. |
| Security vs Features | I will make it local-only | No network calls means no security vulnerabilities to worry about. Also IT department will approve it faster. |
| Realism vs Determinism | I will add a config option | This was the hardest trade-off. Adding a config flag makes the code slightly more complex, but both users get what they need. |

---

## 4. What I Would Do Differently Next Time

| Mistake I Almost Made | What I Learned |
|----------------------|----------------|
| I almost started with complex technologies (RabbitMQ, InfluxDB, Docker) | Next time I will start with the simplest possible solution first. Only add complexity if it's really needed during development. |
| I almost forgot about IT department | I need to include operations stakeholders earlier. They have requirements that can completely change the architecture. |
| My first requirements were vague ("system should be fast") | I learned to add verification criteria immediately. "Fast" is meaningless. "Dashboard updates within 2 seconds" is something I can actually test. |

---

## 5. What I Think Will Work Well

| Approach | Why I Think It Will Work |
|----------|--------------------------|
| CSV for storage | No setup needed. I can open the file and see the data. Easy to debug. |
| Configuration file | I can change sensor behavior without editing code. This was a requirement from the researcher stakeholder. |
| Separate code files | I can work on the simulator without breaking the dashboard. Adding new sensor types will be easier. |
| Config flag for deterministic mode | Both testers and developers get what they need. This was a last-minute idea that saved me from picking one over the other. |

---

## 6. Traceability: Will I Address Stakeholder Needs?

| Stakeholder | Need | How I Plan to Address It |
|-------------|------|-------------------------|
| IoT Developer (S1) | Realistic data | FR-01 to FR-03, FR-11 to FR-16 |
| Software Tester (S2) | Repeatable data | Config flag + FR-09, FR-10 |
| System Admin (S3) | Simple installation | NFR-04, NFR-05 (no complex dependencies) |
| Product Manager (S4) | Demo-ready dashboard | FR-11 to FR-16, NFR-12, NFR-13 |
| IT Department (S5) | Local-only operation | NFR-05, NFR-09 (no network, no external services) |
| Academic Instructor (S6) | Clear documentation | NFR-06, NFR-07 (modular code, docstrings) |
| Researcher (S7) | Configurable parameters | FR-04, config file, CSV export |

---

## 7. Final Thoughts

This assignment made me realize that requirements don't come from nowhere. They come from real people with real problems. The IoT developer doesn't just want "sensor data" - they want data that looks real because their tests might fail with fake numbers. The IT department doesn't just want "security" - they want no external services because getting approval takes months.

If I had to do this again, I would try to interview actual stakeholders instead of imagining what they need. But for this project, I think I captured the main concerns.

The most important lesson: **start simple, add complexity only when needed.** I was tempted to plan a complex system with message queues and databases. But the stakeholder analysis showed that a simple CSV-based approach should satisfy everyone.

Now I need to actually build this. 