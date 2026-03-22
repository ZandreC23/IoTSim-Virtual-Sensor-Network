# System Requirements Document: IoTSim - Virtual Sensor Network Simulator

## Document Information
- **Project:** IoTSim: Virtual Sensor Network Simulator
- **Author:** Zandre Coetzee
- **Date:** March 22, 2026

**Note:** This document describes what the system SHOULD do when it is built. I have not built or tested anything yet. These are the requirements I will use when I start coding.

---

## 1. Introduction

### 1.1 Purpose
This document lists what my IoT simulator needs to do. Every requirement connects back to the stakeholder analysis I did earlier. I will use this document as a checklist when I start coding.

### 1.2 Scope
IoTSim will be a digital twin IoT simulator that generates virtual sensor data (temperature, humidity, water flow) and displays it in a real-time dashboard. It is designed for developers who don't have access to physical sensors.

---

## 2. Functional Requirements

These are the "what" - what the system must do when I build it.

### 2.1 Sensor Simulation Module

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| FR-01 | The system shall simulate a temperature sensor with values between 18°C and 25°C that follows a daily cycle (warmer during day, cooler at night). | I will run the simulator and check that temperatures go up around 2pm and down around 4am. I will confirm values never go outside 18-25°C. | S1, S2, S7 |
| FR-02 | The system shall simulate a humidity sensor with values between 30% and 70% that changes randomly but stays realistic. | I will run the simulator and check that humidity changes by no more than 5% between readings. I will confirm values stay within 30-70% range. | S1, S2, S7 |
| FR-03 | The system shall simulate a water flow sensor with values between 0 L/min and 100 L/min that includes occasional spikes to simulate someone using water. | I will run the simulator and check that every 10-20 readings there is a spike. Regular readings should stay around lower values. | S1, S2, S7 |
| FR-04 | The system shall read simulation settings from a `config.json` file. | I will create a config file, change values, restart the simulator, and confirm the changes take effect. | S1, S4, S7 |
| FR-05 | The system shall let me enable or disable sensors without restarting the whole simulator. | I will edit the config file while the simulator is running and confirm sensors turn on/off on the next cycle. | S1, S4 |
| FR-06 | Each sensor gets a unique ID like `temp_1` or `humidity_2`. | I will run the simulator with multiple sensors and check the output file for duplicate IDs. | S1, S6 |

### 2.2 Data Storage Module

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| FR-07 | Every sensor reading shall save to a file called `sensor_data.csv`. | I will run the simulator and look for the file in the same folder. I will open it to see the readings. | S3, S5, S7 |
| FR-08 | If the CSV file doesn't exist, the system shall create it with headers. | I will delete the file, run the simulator, and confirm the file is recreated with headers: `timestamp,sensor_type,sensor_id,value`. | S3, S5 |
| FR-09 | New readings shall append to the file without deleting old data. | I will run the simulator for 1 hour and count the rows. With 3 sensors at 5-second intervals, I expect 3,600+ rows. Old data should still be there. | S2, S7 |
| FR-10 | Timestamps shall include milliseconds in ISO format: `YYYY-MM-DD HH:MM:SS.fff`. | I will check the CSV file and confirm timestamps look like `2026-03-22 14:30:15.123`. | S1, S2, S7 |

### 2.3 Dashboard Module

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| FR-11 | Dashboard shall check for new data every 2 seconds. | I will run the simulator and dashboard together. I will watch for new readings to appear on screen within 2 seconds of them being written to CSV. | S1, S4 |
| FR-12 | Dashboard shall show a line chart for temperature over the last 5 minutes. | I will run the simulator and look at the dashboard. I expect to see a chart with time on X-axis and °C on Y-axis that updates every 2 seconds. | S1, S4, S6 |
| FR-13 | Dashboard shall show a line chart for humidity over the last 5 minutes. | I will run the simulator and look at the dashboard. I expect to see a chart with time on X-axis and % on Y-axis that updates every 2 seconds. | S1, S4, S6 |
| FR-14 | Dashboard shall show a line chart for water flow over the last 5 minutes. | I will run the simulator and look at the dashboard. I expect to see a chart with time on X-axis and L/min on Y-axis that updates every 2 seconds. | S1, S4, S6 |
| FR-15 | Dashboard shall show current values for each sensor in big readable numbers. | I will run the simulator and look at the dashboard. I expect to see current temperature, humidity, and flow displayed prominently with units. | S1, S4, S6 |
| FR-16 | Dashboard shall refresh automatically without user interaction. | I will run the simulator and dashboard. I will not click anything and confirm new data appears automatically. | S1, S4 |

---

## 3. Non-Functional Requirements

These are the "how" - how well the system should perform when built.

### 3.1 Usability (How easy should it be to use?)

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| NFR-01 | Dashboard should work in Chrome, Firefox, Edge, and Safari. | I will open the dashboard in each browser and confirm it works. | S4, S6 |
| NFR-02 | Charts should show clear labels and units. | I will look at the dashboard and check that I see "°C", "%", and "L/min" labels. Text should be readable. | S4, S6 |
| NFR-03 | Command-line help should show all options. | I will type `python simulator.py --help` and see a list of parameters with examples. | S3, S6 |

### 3.2 Deployability (Where should it be able to run?)

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| NFR-04 | System should run on Windows 10/11 and Linux (Ubuntu). | I will test on my Windows laptop. I will also test on a Ubuntu virtual machine. Both should work. | S3, S5 |
| NFR-05 | No external services should be required (no databases, no internet). | I will turn off WiFi and run the system. Everything should work. Data should save to local CSV. | S5 |

### 3.3 Maintainability (Can someone else understand the code?)

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| NFR-06 | Code should be split into separate files: one for simulator, one for sensors, one for dashboard. | I will open the project folder and see `simulator.py`, `sensors.py`, `dashboard.py`. Each file should have its own responsibility. | S6 |
| NFR-07 | Every function should have a docstring explaining what it does. | I will open the code and hover over functions. Each should have a description. Example: `def generate_temp(): """Returns temperature between 18-25°C with daily cycle."""` | S6 |

### 3.4 Scalability (Should it be able to grow?)

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| NFR-08 | Adding a new sensor type should not require changing existing code. | I will create a new class that inherits from the base Sensor class. I should be able to run it without modifying `simulator.py`. | S4, S7 |

### 3.5 Security (Should it be safe?)

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| NFR-09 | No data should be sent over the network. | I will run the simulator and dashboard, then check with `netstat` to confirm no outbound connections are made. | S5 |
| NFR-10 | Config files should be plain text and not need admin permissions. | I will put the config file in the same folder as the simulator. I should be able to edit it with Notepad. | S3, S5 |

### 3.6 Performance (How fast should it be?)

| ID | Requirement | How I Will Verify When Built | Stakeholder |
|----|-------------|------------------------------|-------------|
| NFR-11 | Simulator should run 3+ sensors at 5-second intervals without lag. | I will run the simulator and check Task Manager for CPU usage. It should stay under 5%. I will let it run for 1 hour and check no readings were missed. | S1, S3 |
| NFR-12 | Dashboard should show updates within 2 seconds of CSV changes. | I will write a script that timestamps when CSV is written and when dashboard updates. The difference should be under 2 seconds. | S1, S4 |
| NFR-13 | System should start up in under 5 seconds. | I will time from pressing Enter to seeing first reading and dashboard loading. Should be under 5 seconds. | S4 |

---

## 4. Requirements Summary

| Category | Count |
|----------|-------|
| Functional Requirements | 16 |
| Non-Functional Requirements | 13 |
| **Total** | **29** |

### Requirements by Stakeholder

| Stakeholder | How Many Requirements Apply |
|-------------|----------------------------|
| IoT Developer (S1) | 16 |
| Software Tester (S2) | 6 |
| System Administrator (S3) | 8 |
| Product Manager (S4) | 14 |
| IT Department (S5) | 7 |
| Academic Instructor (S6) | 10 |
| Researcher (S7) | 9 |

---

## 5. Technologies I Plan to Use

| Component | Technology I Plan to Use | Why I Chose It |
|-----------|--------------------------|----------------|
| Sensor Simulator | Python | I already know Python. It has random, math, csv, and json libraries built in. No extra installs needed. |
| Data Storage | CSV files | Python can write CSV files without extra libraries. No database setup needed. I can open them in Excel to check data. |
| Dashboard | Streamlit | I learned about this from research. It installs with `pip`. I can make charts with very few lines of code. It auto-refreshes. |
| Configuration | JSON file | Python has a built-in json library. I can store settings like sensor ranges and update frequency here. |
| Version Control | Git/GitHub | Already using this for the assignment. |

---

## 6. What I Still Need to Figure Out

| Question | My Current Thinking |
|----------|---------------------|
| How exactly will the daily temperature cycle work? | I will use `math.sin()` to create a wave pattern. Peak at 2pm (value 25°C), minimum at 4am (value 18°C). |
| How will I add the deterministic mode for testers? | I will add a setting in config.json called `deterministic_mode`. When true, random seed is fixed. When false, random seed is random. |
| How will the dashboard read the CSV file continuously? | I will use Streamlit's `st.cache_data` with a short timeout. It will reload the file every 2 seconds. |
| How will I handle the config file changes without restart? | I need to research this. Maybe the simulator checks the config file timestamp each cycle. |

---

## 7. Next Steps

1. Set up Python and Streamlit on my laptop
2. Write the base Sensor class
3. Implement TemperatureSensor, HumiditySensor, WaterSensor
4. Write the SensorManager that runs the simulation loop
5. Add CSV writing functionality
6. Build the Streamlit dashboard that reads the CSV file
7. Test everything according to the requirements above