# Reflection: Class Diagram Design - IoTSim

## Challenges Faced in Designing the Domain Model

The hardest part of this assignment was deciding on the right level of abstraction. I had to carefully distinguish between what belongs in the domain model versus what is implementation detail.

### Challenge 1: Abstract Sensor vs Concrete Sensor Types

I initially created separate classes for TemperatureSensor, HumiditySensor, and WaterFlowSensor without a base class. However, I noticed they share common attributes (sensorId, isEnabled, currentValue) and methods (enable(), disable(), getStatus()), which led to duplication.

To resolve this, I introduced an abstract Sensor class with an abstract generateReading() method. This follows the Template Method pattern, where each sensor type implements its own data generation logic.

**Trade-off: Inheritance vs Composition**  
I chose inheritance (Sensor → TemperatureSensor, etc.) because the relationship is clearly "is-a". A TemperatureSensor is a Sensor, making inheritance the most appropriate and clean design choice.

### Challenge 2: SensorReading Relationship Design

A key design decision was how Sensor relates to SensorReading.

I modeled this relationship as an association because SensorReading represents generated data records that exist independently after creation.

- **Association (Sensor → SensorReading)**: Sensors generate readings over time, but readings are independent data objects that can exist in storage and analytics systems.
- **Aggregation (CSVStorage → SensorReading)**: CSVStorage is responsible for persisting SensorReading objects after they are generated.

This accurately reflects the real-world IoT data flow where sensors generate data continuously and storage systems manage persistence separately.

### Challenge 3: Configuration Coupling

The Configuration class influences system behaviour by defining sensor ranges, update frequency, and operational settings.

Instead of using a complex Observer pattern, I opted for a simpler design where configuration values are loaded and applied during system execution.

**Trade-off: Simplicity vs Flexibility**  
I prioritised simplicity and maintainability over advanced decoupling patterns, as it is sufficient for the scope of this simulator.

## Alignment with Previous Assignments

### Assignment 4 (Functional Requirements)

Each functional requirement maps to class methods:

- FR-01 (temperature cycle) → TemperatureSensor.calculateDailyCycle()
- FR-02 (humidity variation) → HumiditySensor.validateChange()
- FR-03 (water flow spikes) → WaterFlowSensor.shouldSpike()
- FR-07–FR-10 (CSV storage) → CSVStorage methods
- FR-11–FR-16 (dashboard features) → Dashboard methods

### Assignment 5 (Use Cases)

Use cases map to class interactions:

- UC-01 (Configure Simulation) → Configuration.loadConfig() + applySettings()
- UC-02–UC-04 (Generate sensor data) → Sensor.generateReading()
- UC-05 (Store data) → CSVStorage.appendReading()
- UC-06–UC-09 (Dashboard viewing) → Dashboard methods

### Assignment 8 (State Diagrams)

Each state diagram maps directly to a class:

- Sensor State Diagram → Sensor class
- SensorData State Diagram → SensorReading class
- CSVFile State Diagram → CSVStorage class
- Dashboard State Diagram → Dashboard class
- Configuration State Diagram → Configuration class

State transitions identified in Assignment 8 are implemented as methods in the class diagram. For example, transitioning from an active sensor state to data generation is represented by the generateReading() method.

## Trade-offs Made

| Trade-off | Decision | Reason |
|-----------|----------|---------|
| Inheritance vs Composition (Sensors) | Inheritance | Sensors clearly follow an "is-a" relationship |
| Sensor → SensorReading relationship | Association | Readings are generated objects that exist independently |
| CSVStorage → SensorReading | Aggregation | Storage manages persistence of generated data |
| Complexity vs Simplicity | Simplicity | Avoided unnecessary design patterns |
| Abstract class vs Interface | Abstract class | Shared state and behaviour required |
| Encapsulation | Private attributes + public methods | Controlled access to data |

## Lessons Learned About Object-Oriented Design

1. Designing a system starts with understanding the domain, not the code.
2. Abstract classes are useful when multiple entities share behaviour but differ in implementation.
3. Association is appropriate when objects interact but do not share lifecycle dependency.
4. Aggregation is useful for representing persistence or external storage relationships.
5. Multiplicity is important in modelling real-world relationships (e.g., 1 sensor → many readings).
6. Consistency across diagrams and explanations is essential for academic correctness.
7. Traceability ensures every class is justified by requirements, use cases, or user stories.

## Summary

This assignment helped me translate system requirements into a structured object-oriented domain model.

The final class diagram consists of 8 classes (1 abstract, 7 concrete) with clear inheritance, association, and aggregation relationships.

All classes are traceable to functional requirements, use cases, and state diagrams, ensuring consistency across the entire IoTSim system design.

The final design balances simplicity, correctness, and extensibility while accurately modelling a real-world IoT sensor simulation system.
