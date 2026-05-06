# IoTSim: Virtual Sensor Network Simulator

A digital twin IoT simulator that generates virtual sensor data streams for testing IoT systems without physical sensors.

## Project Overview

This system will simulate various sensors including:
- **Temperature sensors** (18-25°C with daily cycle - warmer during day, cooler at night)
- **Humidity sensors** (30-70% with realistic random variations)  
- **Water flow sensors** (0-100 L/min with occasional spikes for usage patterns)

The architecture is a simple three-component pipeline: Sensor Simulator (Python) → CSV File Storage → Dashboard (Streamlit)


---

## Assignments Documentation

### Assignment 3: System Specification and Architecture
- [System Specification](Assignment-3/SPECIFICATION.md)
- [Architecture Documentation](Assignment-3/ARCHITECTURE.md)

### Assignment 4: Stakeholder Analysis and Requirements
- [Stakeholder Analysis](Assignment-4/STAKEHOLDER-ANALYSIS.md)
- [System Requirements](Assignment-4/SYSTEM-REQUIREMENTS.md)
- [Reflection](Assignment-4/REFLECTION.md)

### Assignment 5: Use Case Modeling and Test Case Development
- [Use Case Diagram](Assignment-5/USE-CASE-DIAGRAM.md)
- [Use Case Specifications](Assignment-5/USE-CASE-SPECIFICATIONS.md)
- [Test Cases](Assignment-5/TEST-CASES.md)
- [Reflection](Assignment-5/REFLECTION-ASSIGNMENT-5.md)

### Assignment 6: Agile Planning - User Stories, Product Backlog, Sprint Planning
- [User Stories](Assignment-6/USER-STORIES.md)
- [Product Backlog](Assignment-6/PRODUCT-BACKLOG.md)
- [Sprint Planning](Assignment-6/SPRINT-PLANNING.md)
- [Reflection](Assignment-6/REFLECTION-ASSIGNMENT-6.md)

### Assignment 7: GitHub Project Templates and Kanban Board Implementation
- [Template Analysis](Assignment-7/template-analysis.md)
- [Kanban Explanation](Assignment-7/kanban-explanation.md)
- [Reflection](Assignment-7/reflection-assignment-7.md)
- [Kanban Board Screenshot](Assignment-7/kanban-board.png)

### Assignment 8: Object State Modeling and Activity Workflow Modeling
- [State Transition Diagrams](Assignment-8/STATE-TRANSITION-DIAGRAMS.md)
- [Activity Diagrams](Assignment-8/ACTIVITY-DIAGRAMS.md)
- [Reflection](Assignment-8/REFLECTION-ASSIGNMENT-8.md)

### Assignment 9: Domain Modeling and Class Diagram Development
- [Domain Model](Assignment-9/DOMAIN-MODEL.md)
- [Class Diagram](Assignment-9/CLASS-DIAGRAM.md)
- [Reflection](Assignment-9/REFLECTION-ASSIGNMENT-9.md)
  
### Assignment 10: From Class Diagrams to Code with All Creational Patterns

**Language Choice:** Python 3.x

**Why Python?** Python was chosen for its simplicity, readability, and extensive testing libraries (unittest, pytest). The syntax allows clear implementation of all six creational patterns.

**Class Implementations (from UML diagram):**
**Source Code:** [src/](Assignment-10/src/)

| Class | File | Description |
|-------|------|-------------|
| Sensor (abstract) | `src/sensor.py` | Base class for all sensors |
| TemperatureSensor | `src/temperature_sensor.py` | Simulates daily temperature cycle (18-25°C) |
| HumiditySensor | `src/humidity_sensor.py` | Simulates humidity with ≤5% change per reading |
| WaterFlowSensor | `src/water_flow_sensor.py` | Simulates water flow with spikes every 10-20 readings |
| SensorReading | `src/sensor_reading.py` | Individual sensor data point |
| CSVStorage | `src/csv_storage.py` | Handles CSV file operations |
| Dashboard | `src/dashboard.py` | Simulates real-time data visualization |
| Configuration | `src/configuration.py` | Manages simulation settings (Singleton) |

**Creational Patterns Implemented:**
**Patterns:** [creational_patterns/](Assignment-10/creational_patterns/)

| Pattern | File | Use Case |
|---------|------|----------|
| Simple Factory | `creational_patterns/simple_factory.py` | Centralized sensor creation |
| Factory Method | `creational_patterns/factory_method.py` | Delegate instantiation to subclasses |
| Abstract Factory | `creational_patterns/abstract_factory.py` | Create families of storage objects |
| Builder | `creational_patterns/builder.py` | Construct complex SensorReading objects |
| Prototype | `creational_patterns/prototype.py` | Clone sensors without costly initialization |
| Singleton | `creational_patterns/singleton.py` | Ensure one ConfigurationManager instance |

**Unit Tests:**
**Tests:** [tests/](Assignment-10/tests/)

**Documentation:** [Changelog](CHANGELOG.md) | [Reflection](Assignment-10/REFLECTION-ASSIGNMENT-10.md)

### Assignment 11: Implementing a Persistence Repository Layer
- [Repository Layer Source Code](Assignment-11/repositories/)
- [Repository Factory](Assignment-11/factories/)
- [Unit Tests](Assignment-11/tests/)
- [Future Storage Stub](Assignment-11/future_storage_stub.py)
- [Updated Class Diagram](Assignment-11/class_diagram.md)
- [SensorReading Model](Assignment-11/sensor_reading.py)
- [Configuration Model](Assignment-11/configuration.py)
- [Reflection](Assignment-11/REFLECTION-ASSIGNMENT-11.md)

## Technology Stack
- **Simulator**: Python
- **Data Storage**: CSV files
- **Dashboard**: Streamlit
- **Version Control**: Git/GitHub

## Getting Started
*The system has been fully implemented. All 6 creational patterns and 8 classes are complete with 55 passing unit tests.*