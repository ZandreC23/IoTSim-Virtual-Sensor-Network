# Use Case and Test Document: IoTSim - Virtual Sensor Network Simulator

## Document Information
- **Project:** IoTSim: Virtual Sensor Network Simulator
- **Author:** Zandre Coetzee
- **Date:** March 27, 2026
- **Assignment:** 5 - Use Case Modeling and Test Case Development

---

## 1. Use Case Diagram

### 1.1 Diagram

```mermaid
graph TB
    subgraph Actors
        A1[IoT Developer]
        A2[Software Tester]
        A3[System Administrator]
        A4[Product Manager]
        A5[IT Department]
        A6[Academic Instructor]
        A7[Researcher]
    end

    subgraph System
        UC1[Configure Simulation]
        UC2[Generate Temperature Data]
        UC3[Generate Humidity Data]
        UC4[Generate Water Flow Data]
        UC5[Save Data to CSV]
        UC6[View Dashboard]
        UC7[View Temperature Chart]
        UC8[View Humidity Chart]
        UC9[View Water Flow Chart]
        UC10[Enable Deterministic Mode]
        UC11[Add New Sensor Type]
        UC12[View Log File]
        UC13[Export Data]
    end

    A1 --> UC1
    A1 --> UC2
    A1 --> UC3
    A1 --> UC4
    A1 --> UC6
    A1 --> UC7
    A1 --> UC8
    A1 --> UC9
    
    A2 --> UC10
    A2 --> UC5
    
    A3 --> UC1
    A3 --> UC12
    
    A4 --> UC6
    A4 --> UC7
    A4 --> UC8
    A4 --> UC9
    
    A5 --> UC5
    A5 --> UC1
    
    A6 --> UC6
    A6 --> UC7
    A6 --> UC8
    A6 --> UC9
    
    A7 --> UC1
    A7 --> UC5
    A7 --> UC13
    A7 --> UC11

1.2 Written Explanation
Actors and Their Roles:

Actor	Role	Stakeholder ID
IoT Developer	Configures simulation, generates sensor data, views dashboard to test IoT applications	S1
Software Tester	Enables deterministic mode for repeatable testing, verifies CSV output	S2
System Administrator	Configures simulation parameters, checks log files for errors	S3
Product Manager	Views dashboard to demonstrate live updates to clients	S4
IT Department	Ensures CSV storage works locally without external services	S5
Academic Instructor	Views dashboard to teach students about IoT data visualization	S6
Researcher	Configures parameters, exports data, adds new sensor types for experiments	S7
Relationships and Dependencies:

Relationship	Explanation
View Dashboard includes View Temperature Chart, View Humidity Chart, View Water Flow Chart	The dashboard is the main interface; all charts are part of it.
Generate Temperature Data, Generate Humidity Data, Generate Water Flow Data are independent	Each sensor type runs separately but all feed into Save Data to CSV.
Configure Simulation enables Generate Data use cases	Simulation parameters (frequency, ranges) control how data is generated.
Enable Deterministic Mode affects Generate Data use cases	When enabled, random seed is fixed so data repeats.
Alignment with Stakeholder Concerns:

Stakeholder Concern	Addressed By
S1 (Developer): Realistic data	Generate Temperature/Humidity/Water Flow with realistic patterns
S2 (Tester): Repeatable data	Enable Deterministic Mode use case
S3 (Admin): Simple monitoring	View Log File use case
S4 (PM): Demo-ready dashboard	View Dashboard and chart use cases
S5 (IT): Local-only operation	Save Data to CSV (no external services)
S6 (Instructor): Clear teaching	View Dashboard with visible charts
S7 (Researcher): Configurable experiments	Configure Simulation, Add New Sensor Type, Export Data
2. Use Case Specifications
Use Case 1: Configure Simulation
Field	Content
Use Case ID	UC-01
Use Case Name	Configure Simulation
Actors	IoT Developer, System Administrator, Researcher
Description	User modifies simulation parameters such as update frequency, sensor value ranges, and which sensors are enabled.
Preconditions	config.json file exists in the same directory as the simulator.
Postconditions	New settings are applied. Next simulation cycle uses updated values.
Basic Flow	1. User opens config.json in a text editor.
2. User modifies parameters (e.g., temperature range, update interval).
3. User saves the file.
4. Simulator detects file change on next cycle.
5. Simulator applies new settings.
Alternative Flow (File Not Found)	1. Simulator starts and config.json does not exist.
2. System creates default config file with standard values.
3. Use case continues with default settings.
Use Case 2: Generate Temperature Data
Field	Content
Use Case ID	UC-02
Use Case Name	Generate Temperature Data
Actors	IoT Developer, Researcher
Description	System generates temperature readings between 18-25°C following a daily cycle (warmer during day, cooler at night).
Preconditions	Simulation is running. Temperature sensor is enabled in config.
Postconditions	Temperature reading is generated with timestamp and added to data queue for CSV storage.
Basic Flow	1. Simulator timer reaches generation interval (default 5 seconds).
2. System calculates current time of day.
3. System calculates temperature using sine wave (peak at 2pm, minimum at 4am).
4. System assigns unique sensor ID (e.g., temp_1).
5. System adds timestamp in ISO format with milliseconds.
6. Reading is passed to Save Data to CSV.
Alternative Flow (Sensor Disabled)	1. User disables temperature sensor in config.
2. Simulator skips generation for this sensor type.
3. No temperature data is written.
Use Case 3: Generate Humidity Data
Field	Content
Use Case ID	UC-03
Use Case Name	Generate Humidity Data
Actors	IoT Developer, Researcher
Description	System generates humidity readings between 30-70% with random variations that change by no more than 5% per reading.
Preconditions	Simulation is running. Humidity sensor is enabled in config.
Postconditions	Humidity reading is generated with timestamp and added to data queue for CSV storage.
Basic Flow	1. Simulator timer reaches generation interval.
2. System generates random humidity value within 30-70% range.
3. System ensures change from previous reading ≤ 5%.
4. System assigns unique sensor ID (e.g., humidity_1).
5. System adds timestamp.
6. Reading is passed to Save Data to CSV.
Alternative Flow (Deterministic Mode)	1. deterministic_mode is set to true in config.
2. System uses fixed random seed.
3. Same humidity values are generated each run.
Use Case 4: Generate Water Flow Data
Field	Content
Use Case ID	UC-04
Use Case Name	Generate Water Flow Data
Actors	IoT Developer, Researcher
Description	System generates water flow readings between 0-100 L/min with occasional spikes (every 10-20 readings) to simulate usage.
Preconditions	Simulation is running. Water flow sensor is enabled in config.
Postconditions	Water flow reading is generated with timestamp and added to data queue for CSV storage.
Basic Flow	1. Simulator timer reaches generation interval.
2. System generates random baseline value (0-20 L/min).
3. System checks if spike counter reaches threshold.
4. If spike, value jumps to 50-100 L/min for one reading.
5. System assigns unique sensor ID (e.g., water_1).
6. System adds timestamp.
7. Reading is passed to Save Data to CSV.
Alternative Flow (Spike Occurs)	1. Spike counter reaches threshold.
2. System generates spike value (50-100 L/min).
3. Counter resets.
4. Next reading returns to baseline.
Use Case 5: Save Data to CSV
Field	Content
Use Case ID	UC-05
Use Case Name	Save Data to CSV
Actors	Software Tester, IT Department, Researcher
Description	System writes sensor readings to sensor_data.csv file with headers and timestamp.
Preconditions	Data is generated from sensor simulation.
Postconditions	Reading is appended to CSV file. File is saved to disk.
Basic Flow	1. System receives reading from sensor simulation.
2. System checks if sensor_data.csv exists.
3. If not, system creates file with headers: timestamp,sensor_type,sensor_id,value.
4. System appends new row with reading data.
5. System flushes write buffer to disk.
Alternative Flow (File Write Error)	1. File is locked or disk is full.
2. System logs error to log file.
3. Reading is not written.
4. Simulation continues without interruption.
Use Case 6: View Dashboard
Field	Content
Use Case ID	UC-06
Use Case Name	View Dashboard
Actors	IoT Developer, Product Manager, Academic Instructor
Description	User opens web dashboard to view live sensor data visualizations.
Preconditions	Dashboard server is running. sensor_data.csv exists or is being created.
Postconditions	Dashboard displays charts and current values. Auto-refresh every 2 seconds.
Basic Flow	1. User opens browser and navigates to dashboard URL (e.g., localhost:8501).
2. System reads sensor_data.csv for most recent 5 minutes of data.
3. Dashboard displays line charts for temperature, humidity, water flow.
4. Dashboard displays current values for each sensor.
5. Dashboard auto-refreshes every 2 seconds.
Alternative Flow (No Data)	1. CSV file is empty or does not exist.
2. Dashboard shows "Waiting for data" message.
3. Charts remain empty until data appears.
Use Case 7: Enable Deterministic Mode
Field	Content
Use Case ID	UC-07
Use Case Name	Enable Deterministic Mode
Actors	Software Tester
Description	User enables deterministic mode so that random number generation uses a fixed seed, producing identical data each simulation run.
Preconditions	Config file exists.
Postconditions	deterministic_mode is set to true. Random seed is fixed.
Basic Flow	1. User opens config.json.
2. User sets deterministic_mode: true.
3. User saves file.
4. Simulator reads new setting on next cycle.
5. Random number generator uses fixed seed.
6. All subsequent data is repeatable.
Alternative Flow (Disable Deterministic Mode)	1. User sets deterministic_mode: false.
2. Random seed uses current time.
3. Data varies each simulation run.
Use Case 8: Export Data
Field	Content
Use Case ID	UC-08
Use Case Name	Export Data
Actors	Researcher
Description	User exports sensor data from CSV file for external analysis (e.g., Excel, Python scripts).
Preconditions	CSV file contains sensor readings.
Postconditions	Data is available for external use.
Basic Flow	1. User locates sensor_data.csv in project folder.
2. User copies file to desired location.
3. User opens file in Excel, Python, or analysis tool.
4. Data is ready for analysis.
Alternative Flow (Large File)	1. CSV file becomes large (over 10,000 rows).
2. User opens file in Python with pandas for efficient handling.
3. Data analysis proceeds.
3. Test Cases
3.1 Functional Test Cases
Test Case ID	Requirement ID	Description	Steps	Expected Result	Actual Result	Status
TC-001	FR-01	Temperature sensor follows daily cycle	1. Run simulator at 2pm. 2. Record temperature. 3. Run simulator at 4am. 4. Record temperature.	Temperature higher at 2pm (near 25°C) than at 4am (near 18°C).	TBD	TBD
TC-002	FR-02	Humidity changes by ≤5% per reading	1. Run simulator for 10 readings. 2. Calculate difference between consecutive humidity values.	All differences ≤ 5%.	TBD	TBD
TC-003	FR-03	Water flow includes spikes	1. Run simulator for 50 readings. 2. Count readings > 50 L/min.	At least 2 spikes observed.	TBD	TBD
TC-004	FR-04	Config file settings applied	1. Set temperature range to 20-30°C in config. 2. Run simulator. 3. Check CSV values.	All temperature values between 20-30°C.	TBD	TBD
TC-005	FR-07	Data saves to CSV	1. Run simulator for 1 minute. 2. Open sensor_data.csv.	File exists and contains readings with timestamp, sensor_type, sensor_id, value.	TBD	TBD
TC-006	FR-11	Dashboard updates every 2 seconds	1. Run simulator and dashboard. 2. Time between CSV write and dashboard display.	Delay ≤ 2 seconds.	TBD	TBD
TC-007	FR-15	Dashboard shows current values	1. Run simulator. 2. View dashboard.	Current temperature, humidity, water flow displayed with units (°C, %, L/min).	TBD	TBD
TC-008	FR-16	Dashboard auto-refreshes	1. Run simulator and dashboard. 2. Do not click anything. 3. Watch for new data.	New data appears automatically without user interaction.	TBD	TBD
3.2 Non-Functional Test Cases
Test Case ID	Requirement ID	Category	Description	Steps	Expected Result	Actual Result	Status
NTC-001	NFR-05	Security	System runs without internet	1. Disable WiFi. 2. Run simulator and dashboard.	System starts and runs normally. All data saved locally. No network errors.	TBD	TBD
NTC-002	NFR-09	Security	No network connections	1. Run simulator and dashboard. 2. Run netstat -an in terminal.	No outbound connections to external IPs.	TBD	TBD
NTC-003	NFR-11	Performance	3 sensors at 5-second intervals	1. Run simulator for 1 hour. 2. Count rows in CSV.	Minimum 2,160 rows (3 sensors × 5 seconds × 60 minutes). CPU usage under 5%.	TBD	TBD
NTC-004	NFR-12	Performance	Dashboard updates within 2 seconds	1. Run simulator and dashboard. 2. Measure time from CSV write to dashboard display.	Difference ≤ 2 seconds.	TBD	TBD
NTC-005	NFR-13	Performance	System startup time	1. Start simulator. 2. Time from command execution to first reading.	First reading appears within 5 seconds.	TBD	TBD
NTC-006	NFR-04	Deployability	Runs on Windows and Linux	1. Test on Windows laptop. 2. Test on Ubuntu VM.	Both systems run without errors.	TBD	TBD
NTC-007	NFR-08	Scalability	Add new sensor type	1. Create new class inheriting from Sensor. 2. Add to config. 3. Run simulator.	New sensor data appears in CSV without modifying existing code.	TBD	TBD
NTC-008	NFR-01	Usability	Works in multiple browsers	1. Open dashboard in Chrome. 2. Open in Firefox. 3. Open in Edge.	Dashboard displays correctly in all browsers.	TBD	TBD
4. Reflection
4.1 What I Learned
This assignment required me to take the functional and non-functional requirements from Assignment 4 and translate them into use cases and test cases. The hardest part was deciding which use cases were most critical. I had 16 functional requirements, but I needed to select 8 use cases that captured the core system functionality.

4.2 Challenges Faced
Challenge 1: Determining Use Case Granularity

I initially created too many use cases (over 15). I had separate use cases for "Start Simulator," "Stop Simulator," and "Load Config." I realized these were too detailed and could be combined into "Configure Simulation." The final 8 use cases balance detail with clarity.

Challenge 2: Mapping Use Cases to Stakeholders

Not every use case maps to every stakeholder. I had to decide which stakeholders actually interact with each use case. For example, "Enable Deterministic Mode" is only used by Software Tester (S2), not by Product Manager. I made sure the use case diagram shows this clearly.

Challenge 3: Writing Test Cases Before Implementation

All test cases have "TBD" in Actual Result and Status because I haven't built the system yet. This is correct for this assignment - I am designing tests that will be used later when implementation starts.

Challenge 4: Balancing Non-Functional Test Coverage

I created 8 non-functional test cases covering 6 categories: Security (NTC-001, NTC-002), Performance (NTC-003, NTC-004, NTC-005), Deployability (NTC-006), Scalability (NTC-007), and Usability (NTC-008). This exceeds the requirement of 2 non-functional tests.

