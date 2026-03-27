# Use Case and Test Document: IoTSim - Virtual Sensor Network Simulator

## Document Information
- **Project:** IoTSim: Virtual Sensor Network Simulator
- **Author:** Zandre Coetzee
- **Date:** March 27, 2026
- **Assignment:** 5 - Use Case Modeling and Test Case Development

---

## 1. Use Case Diagram

### 1.1 Diagram

## 1. Use Case Diagram

### 1.1 Diagram

```mermaid
flowchart LR

    %% Actors
    A1([IoT Developer])
    A2([Software Tester])
    A3([System Administrator])
    A4([Product Manager])
    A5([IT Department])
    A6([Academic Instructor])
    A7([Researcher])

    %% System Boundary
    subgraph IoTSim System
        UC1((Configure Simulation))
        UC2((Generate Temperature Data))
        UC3((Generate Humidity Data))
        UC4((Generate Water Flow Data))
        UC5((Save Data to CSV))
        UC6((View Dashboard))
        UC7((View Temperature Chart))
        UC8((View Humidity Chart))
        UC9((View Water Flow Chart))
        UC10((Enable Deterministic Mode))
        UC11((Add New Sensor Type))
        UC12((View Log File))
        UC13((Export Data))
    end

    %% Relationships
    A1 --> UC1
    A1 --> UC2
    A1 --> UC3
    A1 --> UC4
    A1 --> UC6

    A2 --> UC10
    A2 --> UC5

    A3 --> UC1
    A3 --> UC12

    A4 --> UC6

    A5 --> UC5
    A5 --> UC1

    A6 --> UC6

    A7 --> UC1
    A7 --> UC5
    A7 --> UC13
    A7 --> UC11

    %% Include relationships
    UC6 --> UC7
    UC6 --> UC8
    UC6 --> UC9
    ```

### 1.2 Written Explanation

#### Actors and Their Roles

The system identifies seven primary actors, each representing a stakeholder group interacting with IoTSim:

| Actor | Role | Stakeholder ID |
|------|------|----------------|
| IoT Developer | Configures simulation parameters, generates sensor data, and monitors outputs to test IoT applications | S1 |
| Software Tester | Validates system behavior using deterministic mode and verifies correctness of generated data | S2 |
| System Administrator | Manages system configuration and monitors logs to ensure stable operation | S3 |
| Product Manager | Uses the dashboard to demonstrate system capabilities and real-time data visualization | S4 |
| IT Department | Ensures the system operates locally and manages file storage without external dependencies | S5 |
| Academic Instructor | Uses the dashboard as a teaching tool to demonstrate IoT data patterns and system behavior | S6 |
| Researcher | Configures experiments, exports datasets, and extends the system by adding new sensor types | S7 |

Each actor reflects a real-world stakeholder identified in Assignment 4, ensuring traceability between requirements and system interactions.

---

#### Relationships Between Actors and Use Cases

The use case diagram models several important UML relationships:

**1. Association Relationships:**  
Actors are connected to use cases they directly initiate. For example, the *IoT Developer* is associated with configuring simulations and generating sensor data, while the *Software Tester* is specifically associated with enabling deterministic mode. This ensures role-based interaction with the system.

**2. Include Relationships:**  
The *View Dashboard* use case includes *View Temperature Chart*, *View Humidity Chart*, and *View Water Flow Chart*. This reflects that the dashboard acts as a composite interface, where individual visualizations are mandatory components of the overall system view. This improves modularity and clarity in system design.

**3. Dependency Relationships:**  
The *Configure Simulation* use case directly influences all data generation use cases (*Generate Temperature Data*, *Generate Humidity Data*, and *Generate Water Flow Data*). This dependency ensures that simulation parameters such as ranges, intervals, and enabled sensors are consistently applied across the system.

**4. Constraint-Based Relationships:**  
The *Enable Deterministic Mode* use case modifies the behavior of data generation processes by enforcing a fixed random seed. This is critical for testing scenarios where repeatability is required.

---

#### Alignment with Stakeholder Requirements

The use case diagram directly addresses the functional and non-functional requirements defined in Assignment 4, ensuring that stakeholder concerns are fully represented:

| Stakeholder Concern | How It Is Addressed in the Diagram |
|--------------------|------------------------------------|
| S1 (Developer): Need for realistic and configurable data | Supported by *Configure Simulation* and sensor data generation use cases |
| S2 (Tester): Need for repeatable and testable outputs | Addressed by *Enable Deterministic Mode* |
| S3 (Admin): Need for system monitoring and reliability | Addressed by *View Log File* |
| S4 (Product Manager): Need for a clear and presentable interface | Addressed by *View Dashboard* and chart use cases |
| S5 (IT Department): Requirement for local-only execution | Addressed by *Save Data to CSV* without external dependencies |
| S6 (Instructor): Need for educational visualization tools | Addressed by dashboard and chart visualization use cases |
| S7 (Researcher): Need for extensibility and data export | Addressed by *Add New Sensor Type* and *Export Data* |

---

#### Justification of Design

The diagram balances abstraction and detail by grouping related functionality into meaningful use cases while avoiding unnecessary fragmentation. Core system operations such as data generation, configuration, visualization, and storage are clearly separated, improving maintainability and scalability.

Additionally, the inclusion of multiple actors demonstrates that the system supports diverse use cases, ranging from development and testing to education and research. This reinforces the system’s flexibility and real-world applicability.

Overall, the use case model provides a clear, structured representation of how stakeholders interact with IoTSim, ensuring that all critical system behaviors are captured and aligned with the original requirements.