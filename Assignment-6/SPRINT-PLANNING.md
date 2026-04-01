# Sprint Planning: IoTSim

## Sprint Goal

**"Implement core sensor simulation with temperature, humidity, and water flow data, saved to CSV file, and display basic dashboard with live charts."**

This sprint delivers the Minimum Viable Product (MVP): a working system that generates realistic sensor data, saves it to CSV, and displays it in a dashboard. All Must-have stories are included to create a complete end-to-end data pipeline from simulation to visualization.

---

## Sprint Details
- **Sprint Duration:** 2 weeks (10 working days)
- **Sprint Goal:** Core sensor simulation, CSV storage, and dashboard
- **Total Stories:** 6
- **Total Story Points:** 18

---

## Selected Stories for Sprint

| Story ID | User Story | MoSCoW Priority | Story Points | Dependencies |
|----------|------------|-----------------|--------------|--------------|
| US-001 | Generate realistic temperature data with daily cycle | Must-have | 3 | None |
| US-002 | Generate realistic humidity data with random variations | Must-have | 2 | None |
| US-003 | Generate water flow data with usage spikes | Must-have | 2 | None |
| US-004 | Configure simulation parameters via config file | Must-have | 3 | None |
| US-006 | Save all sensor readings to CSV file | Must-have | 3 | US-001, US-002, US-003 |
| US-007 | Dashboard with live temperature, humidity, water flow charts | Must-have | 5 | US-006 |

---

## Sprint Backlog with Tasks

| Task ID | Task Description | Story ID | Estimated Hours | Status |
|---------|------------------|----------|-----------------|--------|
| **Setup & Environment** ||||
| T-001 | Install Python 3.8+ and verify installation | All | 1 | To Do |
| T-002 | Install Streamlit and required libraries | US-007 | 1 | To Do |
| T-003 | Create project folder structure | All | 1 | To Do |
| **Configuration Module** ||||
| T-004 | Create `config.json` template with default values | US-004 | 2 | To Do |
| T-005 | Implement JSON config file reader | US-004 | 2 | To Do |
| T-006 | Implement default config generator if file missing | US-004 | 2 | To Do |
| **Sensor Simulation Module** ||||
| T-007 | Create base `Sensor` class with common attributes | US-001, US-002, US-003 | 3 | To Do |
| T-008 | Implement `TemperatureSensor` with daily cycle (sine wave) | US-001 | 4 | To Do |
| T-009 | Implement `HumiditySensor` with random variations (≤5% change) | US-002 | 3 | To Do |
| T-010 | Implement `WaterFlowSensor` with spike counter logic | US-003 | 3 | To Do |
| T-011 | Implement `SensorManager` to run all sensors in loop | US-001, US-002, US-003 | 4 | To Do |
| **CSV Storage Module** ||||
| T-012 | Create CSV file with headers if not exists | US-006 | 2 | To Do |
| T-013 | Implement append functionality for each reading | US-006 | 2 | To Do |
| T-014 | Add timestamp in ISO format with milliseconds | US-006 | 1 | To Do |
| **Dashboard Module** ||||
| T-015 | Create basic Streamlit dashboard layout | US-007 | 3 | To Do |
| T-016 | Implement CSV file reader that polls every 2 seconds | US-007 | 3 | To Do |
| T-017 | Create temperature line chart with 5-minute window | US-007 | 3 | To Do |
| T-018 | Create humidity line chart with 5-minute window | US-007 | 2 | To Do |
| T-019 | Create water flow line chart with 5-minute window | US-007 | 2 | To Do |
| **Integration & Testing** ||||
| T-020 | Integrate simulator and dashboard | All | 4 | To Do |
| T-021 | Test end-to-end data flow (simulator → CSV → dashboard) | All | 3 | To Do |
| T-022 | Verify all acceptance criteria | All | 2 | To Do |
| **Total Hours** ||| **51** | |

---

## Sprint Timeline (2 Weeks)

| Week | Days | Focus | Tasks |
|------|------|-------|-------|
| Week 1 | Days 1-2 | Setup + Configuration | T-001 to T-006 |
| Week 1 | Days 3-4 | Sensor Simulation | T-007 to T-011 |
| Week 1 | Day 5 | CSV Storage | T-012 to T-014 |
| Week 2 | Days 6-7 | Dashboard | T-015 to T-019 |
| Week 2 | Days 8-9 | Integration | T-020 to T-021 |
| Week 2 | Day 10 | Testing + Bug Fixes | T-022 |

---

## Why This Sprint Contributes to MVP

| Component | Delivered | Why It's MVP |
|-----------|-----------|--------------|
| **Sensor Simulation** | US-001, US-002, US-003 | Core functionality: generates data |
| **Configuration** | US-004 | Allows users to customize behavior |
| **CSV Storage** | US-006 | Saves data for verification and analysis |
| **Dashboard** | US-007 | Visualizes data for demos and teaching |

**End-to-end pipeline:** Simulator → CSV → Dashboard is complete and working.

---

## Acceptance Criteria for Sprint

- [ ] Temperature data follows daily cycle (peak at 2pm, minimum at 4am)
- [ ] Humidity data stays within 30-70% with ≤5% change per reading
- [ ] Water flow data shows spikes every 10-20 readings
- [ ] Configuration file can modify update frequency and sensor ranges
- [ ] CSV file created with headers and appends data
- [ ] Dashboard displays three line charts that update every 2 seconds
- [ ] All data stays local with no internet connection required