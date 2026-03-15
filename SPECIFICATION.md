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

1. **Modular Architecture**: The system can be built incrementally starting with basic sensor simulation, then adding processing capabilities, and finally the dashboard.

2. **Well-defined Components**:
   - **Sensor Simulator**: Can start with 1-2 sensor types (e.g., temperature only) and expand
   - **Processing Service**: Simple data validation, filtering, and aggregation
   - **Dashboard**: Basic web interface with charts and tables

3. **Existing Technologies**: Leverages Python (simulator), Flask/FastAPI (processing service), and basic web technologies (dashboard) - all with extensive documentation and community support.

4. **Clear Deliverables**: Each component can be developed and demonstrated independently.

5. **Time Allocation**: 12-14 weeks provides sufficient time for research, design, implementation, and documentation.

## 2. System Overview

The IoTSim system creates a complete end-to-end IoT data pipeline entirely in software:

### 2.1 Sensor Simulator
Generates virtual sensor readings at configurable intervals. Each simulated sensor has:
- Unique sensor ID
- Sensor type (water, temperature, humidity)
- Location metadata
- Current value with realistic variations
- Timestamp

### 2.2 Data Stream
Acts as a communication channel between simulator and processing service. Implements a publish-subscribe pattern where sensors publish data and the processing service subscribes to receive it.

### 2.3 Processing Service
Consumes raw sensor data and performs:
- Data validation (range checks, format validation)
- Anomaly detection (values outside normal ranges)
- Data aggregation (averages, min/max over time windows)
- Alert generation for threshold violations
- Storage preparation

### 2.4 Dashboard
Visualizes processed data through:
- Real-time sensor readings
- Historical data charts
- Sensor status indicators
- Alert notifications

## 3. Functional Requirements

### 3.1 Sensor Simulation Module
| ID | Requirement Description |
|----|------------------------|
| FR1 | The system shall simulate temperature sensors generating values between -10°C and 40°C with realistic variations |
| FR2 | The system shall simulate humidity sensors generating values between 0% and 100% with realistic variations |
| FR3 | The system shall simulate water sensors generating values (flow rate, pressure, or presence) |
| FR4 | The system shall allow configuration of simulation parameters (update frequency, value ranges) |
| FR5 | The system shall support adding/removing sensors dynamically |
| FR6 | Each simulated sensor shall have a unique identifier and metadata (location, type) |

### 3.2 Data Streaming Module
| ID | Requirement Description |
|----|------------------------|
| FR7 | The system shall publish sensor readings to a message queue in real-time |
| FR8 | The system shall ensure at-least-once delivery of sensor messages |
| FR9 | The system shall support multiple subscribers to the data stream |
| FR10 | The system shall include timestamps with each sensor reading |

### 3.3 Data Processing Module
| ID | Requirement Description |
|----|------------------------|
| FR11 | The system shall validate incoming sensor data for correct format and reasonable ranges |
| FR12 | The system shall detect and flag anomalous readings (sudden spikes, out-of-range values) |
| FR13 | The system shall calculate 1-minute, 5-minute, and 1-hour averages for each sensor |
| FR14 | The system shall generate alerts when sensor values exceed configurable thresholds |
| FR15 | The system shall store processed data in a time-series format |

### 3.4 Dashboard Module
| ID | Requirement Description |
|----|------------------------|
| FR16 | The dashboard shall display current readings from all active sensors |
| FR17 | The dashboard shall show historical trends using line charts |
| FR18 | The dashboard shall indicate sensor status (active/inactive/alerting) |
| FR19 | The dashboard shall display recent alerts with timestamps |
| FR20 | The dashboard shall update automatically as new data arrives |

## 4. Non-Functional Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| NFR1 | Performance | The system shall process at least 100 sensor readings per second |
| NFR2 | Scalability | The architecture shall support adding new sensor types without major redesign |
| NFR3 | Reliability | The system shall have 99% uptime during testing periods |
| NFR4 | Usability | The dashboard shall be accessible via web browser with intuitive interface |
| NFR5 | Maintainability | Code shall be modular with clear separation of concerns |
| NFR6 | Documentation | All components shall include inline documentation and setup guides |

## 5. Technology Stack

| Component | Technology Options | Selection Rationale |
|-----------|-------------------|---------------------|
| Sensor Simulator | Python, Node.js | Python's simplicity and rich ecosystem for simulation |
| Message Queue | RabbitMQ, Kafka, Redis | Lightweight, easy to set up for development |
| Processing Service | FastAPI, Flask, Node.js | FastAPI offers async support and automatic API docs |
| Database | InfluxDB, PostgreSQL, MongoDB | InfluxDB optimized for time-series data |
| Dashboard | React, Vue.js, Dash | Plotly Dash for Python-based visualization |
| Deployment | Docker, Docker Compose | Containerization for consistent environments |

## 6. Constraints and Assumptions

### Constraints
- Development timeline: 14 weeks
- Individual developer
- Open-source technologies only
- Local deployment (cloud deployment optional)

### Assumptions
- Users have basic understanding of IoT concepts
- Development environment can be set up on standard laptops
- Internet connection available for documentation and libraries
- Browser supports modern JavaScript features

## 7. Success Criteria

The project will be considered successful when:

1. All four architectural components are implemented and integrated
2. At least three sensor types are simulated
3. Data flows from simulator to dashboard in real-time
4. Dashboard displays live and historical data
5. System runs for 24 hours without failure
6. Documentation is complete with setup instructions