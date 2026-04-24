
## Step 5: Create `REFLECTION-ASSIGNMENT-9.md`

# Reflection: Assignment 9 - Domain Modeling and Class Diagram

## Challenges Faced in Designing the Domain Model

The hardest part of this assignment was deciding on the right level of abstraction. I had to ask myself: what belongs in the domain model and what is just implementation detail?

### Challenge 1: Abstract Sensor vs Concrete Sensor Types

I initially created separate classes for TemperatureSensor, HumiditySensor, and WaterFlowSensor without a base class. But then I noticed they share common attributes (sensorId, isEnabled, currentValue) and common methods (enable(), disable(), getStatus()). This was code duplication waiting to happen.

I decided to create an abstract Sensor class with a abstract `generateReading()` method. This follows the Template Method pattern. Each sensor type implements its own generation logic. The downside is more files, but the upside is that adding a new sensor type (e.g., PressureSensor) requires no changes to existing code.

**Trade-off:** Inheritance vs Composition
I chose inheritance (Sensor → TemperatureSensor) because the relationship is clearly "is-a" (TemperatureSensor is a Sensor). Composition would not make sense here because a TemperatureSensor does not "have" a Sensor.

### Challenge 2: SensorReading Relationship

I initially considered composition between Sensor and SensorReading, because a sensor logically produces readings. However, in the final design I modeled this as an association.

- **Association (Sensor → SensorReading):** Sensors generate readings over time, but readings are independent data records that can exist in storage and analytics systems.

- **Aggregation (CSVStorage → SensorReading):** CSVStorage is responsible for storing readings persistently after they are generated.

This approach better reflects the real-world data flow of a monitoring system where readings are produced continuously and stored externally.

### Challenge 3: Configuration Coupling

The Configuration class controls almost every other class. It tells sensors when to generate data, what ranges to use, and whether deterministic mode is on. This creates high coupling.

I considered using the Observer pattern where sensors listen for configuration changes. But that seemed over-engineered for my simple simulator. Instead, the simulator reads config on each cycle. This is simpler but less efficient.

## Alignment with Previous Assignments

### Assignment 4 (Functional Requirements)

Every functional requirement maps to a class method:
- FR-01 (temperature daily cycle) → TemperatureSensor.calculateDailyCycle()
- FR-02 (humidity random variations) → HumiditySensor.validateChange()
- FR-03 (water flow spikes) → WaterFlowSensor.shouldSpike()
- FR-07 to FR-10 (CSV storage) → CSVStorage methods
- FR-11 to FR-16 (dashboard) → Dashboard methods

### Assignment 5 (Use Cases)

Use cases map to class interactions:
- UC-01 (Configure Simulation) → Configuration.loadConfig() + Configuration.applySettings()
- UC-02, UC-03, UC-04 (Generate Data) → Sensor.generateReading() implementations
- UC-05 (Save to CSV) → CSVStorage.appendReading()
- UC-06 to UC-09 (View Dashboard) → Dashboard methods

### Assignment 8 (State Diagrams)

Each state diagram has a corresponding class:
- Sensor State Diagram → Sensor class
- SensorData State Diagram → SensorReading class
- CSVFile State Diagram → CSVStorage class
- Dashboard State Diagram → Dashboard class
- Configuration State Diagram → Configuration class

The state transitions I modeled in Assignment 8 become methods in the class diagram. For example, the transition from "Enabled" to "Generating" in the Sensor state diagram is triggered by the `generateReading()` method.

## Trade-offs Made

| Trade-off | My Choice | Why |
|-----------|-----------|-----|
| Inheritance vs Composition for sensors | Inheritance | Sensors are clearly "is-a" relationships |
| Association for runtime generation, aggregation for persistence | Both | Association for runtime generation, aggregation for persistence |
| High coupling vs Simplicity | Simplicity | Configuration directly controls sensors |
| Abstract class vs Interface | Abstract class | Sensors share common attributes and methods |
| Public vs Private attributes | Private with public getters | Encapsulation |

## Lessons Learned About Object-Oriented Design

1. **Start with the domain model before coding.** It forces you to think about relationships before implementation.

2. **Use abstract classes when objects share behavior.** My three sensor types share enable/disable logic but have different data generation logic.

3. **Composition is stronger than aggregation.** I used composition for Sensor → SensorReading because readings don't make sense without a sensor.

4. **Multiplicity matters.** A single configuration object controls multiple sensors (1 to 1..*). One dashboard reads from one CSV file (1 to 1).

5. **Traceability keeps you honest.** Mapping each class to functional requirements, use cases, and state diagrams helped me ensure nothing was missing.

## Summary

This assignment taught me that a good class diagram is not just a collection of boxes and arrows. It must capture the essence of the domain, enforce business rules, and align with requirements from previous assignments. My class diagram has 8 classes (1 abstract, 7 concrete), multiple relationships including inheritance, association, aggregation, and multiplicity constraints.
