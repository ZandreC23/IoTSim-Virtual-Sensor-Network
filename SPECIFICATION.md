# System Specification: IoTSim - Virtual Sensor Network Simulator

## 1. Introduction

### Project Title
**IoTSim: Virtual Sensor Network Simulator**

### Domain
**IoT Systems / Smart Infrastructure**

This project operates in the Internet of Things (IoT) domain, specifically focusing on smart infrastructure monitoring. IoT systems are networks of interconnected devices (sensors, actuators) that collect and exchange data. Smart infrastructure refers to applying IoT technology to physical infrastructure like buildings, water systems, and environmental monitoring to improve efficiency, safety, and decision-making.

### Problem Statement
Developers and researchers working on IoT systems face a significant challenge: they cannot easily test their applications without access to physical sensors. Physical sensors are expensive, require installation, and may not be available during early development stages. Additionally, testing edge cases (like extreme temperature readings or water leak scenarios) is difficult with real sensors as these conditions cannot be reliably reproduced on demand.

The purpose of this system is to solve this problem by creating a **Digital Twin IoT Simulator** that generates realistic virtual sensor data streams. This allows developers to:
- Test IoT applications without physical hardware
- Simulate various environmental conditions
- Generate consistent, repeatable test data
- Validate data processing pipelines before deployment
- Demonstrate IoT concepts in educational settings

### Individual Scope
This project is feasible for an individual student to complete within one semester for the following reasons:

1. **Modular Architecture**: The system can be built incrementally starting with basic sensor simulation, then adding the dashboard.

2. **Well-defined Components**:
   - **Sensor Simulator**: Start with 1-2 sensor types (e.g., temperature only) and expand
   - **CSV Storage**: Simple file-based storage built into Python
   - **Dashboard**: Basic web interface with charts using Streamlit

3. **Existing Technologies**: Leverages Python (simulator) and Streamlit (dashboard) - both with extensive documentation and community support.

4. **Clear Deliverables**: Each component can be developed and demonstrated independently.

5. **Time Allocation**: 12-14 weeks provides sufficient time for research, design, implementation, and documentation.

## 2. System Overview

The IoTSim system creates a simple, three-component architecture:

### 2.1 Sensor Simulator
A Python script that runs continuously, generating virtual sensor readings at configurable intervals (default: every 5 seconds). Each simulated sensor has:
- Unique sensor ID
- Sensor type (temperature, humidity, water)
- Current value with realistic variations
- Timestamp

### 2.2 Data Storage (CSV File)
All sensor readings are appended to a CSV file (`sensor_data.csv`) with the following format:
- timestamp,sensor_type,sensor_id,value

This simple file-based approach requires no additional software and acts as the communication channel between simulator and dashboard.

### 2.3 Dashboard
A Streamlit web application that:
- Reads the CSV file every 2 seconds
- Displays real-time line charts of sensor readings
- Shows current values for each sensor
- Auto-refreshes to show new data

## 3. Functional Requirements

### 3.1 Sensor Simulation Module
| ID | Requirement Description |
|----|------------------------|
| FR1 | The system shall simulate temperature sensors generating values between -10°C and 40°C with realistic variations |
| FR2 | The system shall simulate humidity sensors generating values between 0% and 100% with realistic variations |
| FR3 | The system shall simulate water sensors generating flow rate values between 0-100 L/min |
| FR4 | The system shall allow configuration of simulation parameters (update frequency, value ranges) |
| FR5 | The system shall support adding/removing sensors dynamically |
| FR6 | Each simulated sensor shall have a unique identifier and sensor type |

### 3.2 Data Storage Module
| ID | Requirement Description |
|----|------------------------|
| FR7 | The system shall save each sensor reading to a CSV file with timestamp |
| FR8 | The system shall create a new CSV file with headers if one doesn't exist |
| FR9 | The system shall append readings to the CSV file without overwriting existing data |
| FR10 | Each CSV row shall include timestamp, sensor type, sensor ID, and value |

### 3.3 Data Processing Module
| ID | Requirement Description |
|----|------------------------|
| FR11 | The dashboard shall read the CSV file and parse its contents correctly |
| FR12 | The dashboard shall calculate and display rolling averages (optional) |
| FR13 | The dashboard shall identify and highlight values outside normal ranges |
| FR14 | The system shall store all raw data in the CSV file for historical analysis |

### 3.4 Dashboard Module
| ID | Requirement Description |
|----|------------------------|
| FR15 | The dashboard shall display current readings from all active sensors |
| FR16 | The dashboard shall show historical trends using line charts |
| FR17 | The dashboard shall indicate sensor status (active/inactive) |
| FR18 | The dashboard shall update automatically every 2 seconds as new data arrives |

## 4. Non-Functional Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| NFR1 | Performance | The simulator shall generate at least 3 sensor readings per second |
| NFR2 | Scalability | The architecture shall support adding new sensor types without major redesign |
| NFR3 | Reliability | The system shall have 99% uptime during testing periods |
| NFR4 | Usability | The dashboard shall be accessible via web browser with intuitive interface |
| NFR5 | Maintainability | Code shall be modular with clear separation of concerns |
| NFR6 | Documentation | All components shall include inline documentation and setup guides |

## 5. Technology Stack

| Component | Technology | Selection Rationale |
|-----------|------------|---------------------|
| Sensor Simulator | Python | Simple syntax, extensive libraries, already installed |
| Data Storage | CSV Files | Built into Python, no setup required, human-readable |
| Dashboard | Streamlit | Minimal code, automatic refresh, beautiful charts with 10 lines of code |
| Version Control | Git/GitHub | Industry standard, free hosting, assignment submission platform |
| Development | VS Code | Free, excellent Python support, already in use |

## 6. Constraints and Assumptions

### Constraints
- Development timeline: 14 weeks
- Individual developer
- Open-source technologies only
- Local deployment only (no cloud services)
- All data stored in CSV files (no database setup)

### Assumptions
- Users have basic understanding of IoT concepts
- Python 3.8+ installed on development machine
- Internet connection available for installing libraries (Streamlit, Pandas)
- Browser supports modern web features

## 7. Success Criteria

The project will be considered successful when:

1. All three architectural components are implemented (Simulator → CSV → Dashboard)
2. Three sensor types are simulated (temperature, humidity, water)
3. Simulator writes readings to CSV file every 5 seconds
4. Dashboard reads CSV file and updates display every 2 seconds
5. Dashboard shows live line charts and current values
6. System runs for 1 hour without crashing
7. Documentation is complete with setup and run instructions