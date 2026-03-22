# IoTSim: Virtual Sensor Network Simulator

A digital twin IoT simulator that generates virtual sensor data streams for testing IoT systems without physical sensors.

## Project Overview

This system will simulate various sensors including:
- **Temperature sensors** (18-25°C with daily cycle - warmer during day, cooler at night)
- **Humidity sensors** (30-70% with realistic random variations)  
- **Water flow sensors** (0-100 L/min with occasional spikes for usage patterns)

The architecture is a simple three-component pipeline: Sensor Simulator (Python) → CSV File Storage → Dashboard (Streamlit)

## Documentation
- [System Specification](SPECIFICATION.md)
- [Architecture Documentation](ARCHITECTURE.md)
- [Stakeholder Analysis](STAKEHOLDER-ANALYSIS.md)
- [System Requirements](SYSTEM-REQUIREMENTS.md)
- [Reflection](REFLECTION.md)

## Technology Stack
| Component | Technology |
|-----------|------------|
| Simulator | Python |
| Data Storage | CSV files |
| Dashboard | Streamlit |
| Version Control | Git/GitHub |

## Getting Started
*Setup instructions will be added when implementation begins.*