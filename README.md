# IoTSim: Virtual Sensor Network Simulator

A digital twin IoT simulator that generates virtual sensor data streams for testing IoT systems without physical sensors.

## Project Overview

This system will simulate various sensors including:
- **Temperature sensors** (18-25°C with daily cycle - warmer during day, cooler at night)
- **Humidity sensors** (30-70% with realistic random variations)  
- **Water flow sensors** (0-100 L/min with occasional spikes for usage patterns)

The planned architecture is a simple three-component pipeline: Sensor Simulator (Python) → CSV File Storage → Dashboard (Streamlit)

I chose this simple architecture because it meets all stakeholder needs without requiring complex setup. More details in the stakeholder analysis and requirements documents.

## Documentation
- [System Specification](SPECIFICATION.md) - Assignment 3
- [Architecture Documentation](ARCHITECTURE.md) - Assignment 3 with C4 diagrams
- [Stakeholder Analysis](STAKEHOLDER-ANALYSIS.md) - Assignment 4
- [System Requirements](SYSTEM-REQUIREMENTS.md) - Assignment 4 (what the system will do when built)
- [Reflection](REFLECTION.md) - Assignment 4 (challenges in planning)

## Planned Technology Stack
- **Simulator**: Python (random, math, csv, json libraries)
- **Data Storage**: CSV files (built into Python, no database needed)
- **Dashboard**: Streamlit (simple pip install, auto-refresh, charts)
- **Version Control**: Git/GitHub

## Assignment Progress
- ✅ **Assignment 3:** System specification, C4 architecture diagrams (complete)
- ✅ **Assignment 4:** Stakeholder analysis, functional/non-functional requirements, reflection (complete - this is planning phase)
- ⏳ **Implementation:** Not started yet. I will use these requirements as my checklist when I start coding.

## Getting Started
*Setup instructions will be added when I start coding. The plan is to use Python and Streamlit with minimal dependencies.*

---

## Notes to the Marker

This assignment is the planning phase. I have not built the system yet. The requirements document describes what I will build, not what I have already built. The technologies listed are what I plan to use.