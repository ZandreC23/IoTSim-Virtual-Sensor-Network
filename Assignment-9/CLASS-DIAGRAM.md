# Class Diagram: IoTSim

## Mermaid.js Class Diagram

```mermaid
classDiagram

%% =========================
%% ABSTRACT BASE CLASS
%% =========================
class Sensor {
    <<abstract>>
    -sensorId: String
    -sensorType: String
    -isEnabled: Boolean
    -currentValue: Float
    -lastUpdate: DateTime
    +generateReading() Float
    +enable() void
    +disable() void
    +getStatus() String
}

%% =========================
%% SENSOR TYPES
%% =========================
class TemperatureSensor {
    -minTemp: Float
    -maxTemp: Float
    -timeOfDay: Integer
    +generateReading() Float
    +calculateDailyCycle() Float
    +validateReading(value: Float) Boolean
}

class HumiditySensor {
    -minHumidity: Float
    -maxHumidity: Float
    -previousValue: Float
    +generateReading() Float
    +validateChange(value: Float) Boolean
    +regenerateIfNeeded() Float
}

class WaterFlowSensor {
    -minFlow: Float
    -maxFlow: Float
    -spikeCounter: Integer
    -spikeThreshold: Integer
    +generateReading() Float
    +shouldSpike() Boolean
    +resetSpikeCounter() void
}

%% =========================
%% SUPPORTING CLASSES
%% =========================
class SensorReading {
    -readingId: String
    -sensorId: String
    -sensorType: String
    -value: Float
    -timestamp: DateTime
    -isAnomaly: Boolean
    +toCSVRow() String
    +validate() Boolean
    +flagAnomaly() void
}

class CSVStorage {
    -fileName: String
    -headers: List~String~
    -isWritable: Boolean
    +createFile() void
    +appendReading(reading: SensorReading) void
    +readAllReadings() List~SensorReading~
    +checkFileExists() Boolean
}

class Dashboard {
    -refreshInterval: Integer
    -dataWindow: Integer
    -csvFilePath: String
    -isRunning: Boolean
    +loadData() List~SensorReading~
    +updateCharts() void
    +updateCurrentValues() void
    +autoRefresh() void
}

class Configuration {
    -configPath: String
    -updateFrequency: Integer
    -temperatureRange: Object
    -humidityRange: Object
    -waterFlowRange: Object
    -deterministicMode: Boolean
    -enabledSensors: List~String~
    +loadConfig() void
    +saveConfig() void
    +validateSettings() Boolean
    +applySettings() void
}

%% =========================
%% INHERITANCE RELATIONSHIPS
%% =========================
Sensor <|-- TemperatureSensor
Sensor <|-- HumiditySensor
Sensor <|-- WaterFlowSensor

%% =========================
%% CLASS RELATIONSHIPS
%% =========================
Sensor "1" --> "0..*" SensorReading : generates
CSVStorage "1" o-- "0..*" SensorReading : stores
Dashboard "1" --> "1" CSVStorage : reads from
Configuration "1" --> "1..*" Sensor : controls
```

## Key Design Decisions

### 1. Abstract Sensor Class
I made Sensor an abstract class because no generic sensor exists in the system. Every sensor must be a specific type (Temperature, Humidity, or WaterFlow). The `generateReading()` method is abstract because each sensor type generates data differently:

- **Temperature** uses sine wave for daily cycle
- **Humidity** uses random with change limits (≤5%)
- **Water flow** uses baseline with occasional spikes (every 10-20 readings)

**Alternative considered:** Making Sensor a concrete class with a type parameter. But this would violate the Open/Closed Principle because adding a new sensor type would require modifying the Sensor class. The abstract class approach allows extension without modification.

### 2. Association vs Aggregation

**Association (Sensor → SensorReading):**  
A Sensor generates zero or many SensorReading objects over time. Each reading is linked to the sensor that created it.

**Aggregation (CSVStorage → SensorReading):** SensorReading can exist independently of CSVStorage. Readings are stored in the CSV file, but they exist before being saved. This is represented by `CSVStorage "1" o-- "0..*" SensorReading : stores` in the diagram above.

### 3. Multiplicity Decisions

| Relationship | Multiplicity | Reason |
|-------------|-------------|---------|
| Sensor to SensorReading | 1 → 0..* | One sensor produces zero or many readings over time |
| CSVStorage to SensorReading | 1 → 0..* | Storage can have zero readings initially |
| Configuration to Sensor | 1 → 1..* | One config controls multiple sensors |
| Dashboard to CSVStorage | 1 → 1 | Dashboard reads from one CSV file |

### 4. Attribute Visibility

| Symbol | Meaning | Used For |
|--------|---------|----------|
| + | Public | Methods that external classes need to call |
| - | Private | Internal state that should not be directly modified |
| # | Protected | Attributes shared with child classes (not used here) |

### 5. Alignment with Previous Assignments

| Assignment | How Class Diagram Aligns |
|-----------|-------------------------|
| Assignment 4 (FRs) | All FRs map to class methods (FR-01 → TemperatureSensor.generateReading()) |
| Assignment 5 (Use Cases) | Each use case maps to one or more classes (UC-05 → CSVStorage methods) |
| Assignment 6 (User Stories) | User stories map to class responsibilities (US-007 → Dashboard.updateCharts()) |
| Assignment 8 (State Diagrams) | Each state diagram has a corresponding class (Sensor, SensorReading, CSVStorage, Dashboard, Configuration) |

### 6. Business Rules Enforced

| Business Rule | Implemented In |
|--------------|----------------|
| Temperature 18-25°C with daily cycle | TemperatureSensor.calculateDailyCycle() |
| Humidity change ≤5% | HumiditySensor.validateChange() |
| Water flow spikes every 10-20 readings | WaterFlowSensor.shouldSpike() |
| CSV file created with headers | CSVStorage.createFile() |
| Dashboard refreshes every 2 seconds | Dashboard.autoRefresh() |
| Configuration changes apply on next cycle | Configuration.applySettings() |
