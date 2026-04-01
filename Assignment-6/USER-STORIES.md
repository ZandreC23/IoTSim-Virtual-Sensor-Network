# User Stories: IoTSim

## Traceability to Requirements
All user stories are traceable to functional requirements from Assignment 4 and use cases from Assignment 5.

| Requirement ID | Use Case ID | User Story |
|----------------|-------------|------------|
| FR-01, FR-02, FR-03 | UC-02, UC-03, UC-04 | US-001, US-002, US-003 |
| FR-04, FR-05 | UC-01 | US-004 |
| FR-06 | UC-02, UC-03, UC-04 | US-005 |
| FR-07, FR-08, FR-09, FR-10 | UC-05 | US-006 |
| FR-11, FR-12, FR-13, FR-14, FR-15, FR-16 | UC-06, UC-07, UC-08, UC-09 | US-007, US-008, US-009 |
| NFR-05, NFR-09 | UC-05 | US-010 |
| NFR-08 | UC-11 | US-011 |

---

## User Stories

| ID | User Story | Acceptance Criteria | Priority | Traceability |
|----|------------|---------------------|----------|--------------|
| US-001 | As an IoT Developer, I want to generate realistic temperature data that follows a daily cycle so I can test how my application responds to changing environmental conditions. | Temperature values range between 18-25°C; peak at 2pm; minimum at 4am; updates every 5 seconds. | High | FR-01, UC-02 |
| US-002 | As an IoT Developer, I want to generate humidity data with realistic random variations so I can test my application under normal operating conditions. | Humidity values between 30-70%; changes by no more than 5% per reading; updates every 5 seconds. | High | FR-02, UC-03 |
| US-003 | As an IoT Developer, I want to generate water flow data with occasional usage spikes so I can test my application's response to sudden changes. | Water flow values between 0-100 L/min; spikes occur every 10-20 readings; updates every 5 seconds. | High | FR-03, UC-04 |
| US-004 | As a Researcher, I want to configure simulation parameters through a config file so I can run experiments with different sensor behaviors. | All parameters (update frequency, value ranges, enabled sensors) configurable in `config.json`; changes apply on restart. | High | FR-04, FR-05, UC-01 |
| US-005 | As a System Administrator, I want each sensor to have a unique ID so I can identify and track individual sensors in logs and data files. | Sensor IDs follow format `[type]_[number]` (e.g., `temp_1`, `humidity_2`); no duplicates. | Medium | FR-06, UC-02, UC-03, UC-04 |
| US-006 | As a Software Tester, I want all sensor readings saved to a CSV file so I can verify data integrity and run regression tests. | File `sensor_data.csv` created with headers; each reading appended; timestamps include milliseconds. | High | FR-07, FR-08, FR-09, FR-10, UC-05 |
| US-007 | As a Product Manager, I want a dashboard that shows live temperature, humidity, and water flow charts so I can demonstrate real-time IoT monitoring to clients. | Three separate line charts; update every 2 seconds; show last 5 minutes of data. | High | FR-11, FR-12, FR-13, FR-14, UC-06, UC-07, UC-08, UC-09 |
| US-008 | As a Product Manager, I want the dashboard to display current sensor values in large readable numbers so clients can immediately see the latest readings. | Current temperature, humidity, water flow displayed prominently with units (°C, %, L/min). | Medium | FR-15, UC-06 |
| US-009 | As an Academic Instructor, I want the dashboard to auto-refresh so students can see data updating in real-time without manual intervention. | Dashboard checks for new data every 2 seconds; updates automatically. | Medium | FR-16, UC-06 |
| US-010 | As an IT Department member, I want the system to run completely offline with no external dependencies so security approval is fast. | System runs without internet; no databases or message queues; all data stored locally in CSV. | High | NFR-05, NFR-09, UC-05 |
| US-011 | As a Researcher, I want to add new sensor types without modifying existing code so I can extend the system for new experiments. | New sensor class inherits from base Sensor class; no changes to `simulator.py`. | Medium | NFR-08, UC-11 |

---

## Summary

| Priority | Count |
|----------|-------|
| High | 6 |
| Medium | 5 |
| Low | 0 |
| **Total** | **11** |