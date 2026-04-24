# Domain Model: IoTSim

## Traceability to Previous Assignments

| Entity | Functional Requirements | Use Cases | User Stories | State Diagrams |
|--------|------------------------|-----------|--------------|----------------|
| Sensor | FR-01, FR-02, FR-03, FR-06 | UC-02, UC-03, UC-04 | US-001, US-002, US-003, US-005 | Sensor State Diagram |
| TemperatureSensor | FR-01 | UC-02 | US-001 | Sensor State Diagram |
| HumiditySensor | FR-02 | UC-03 | US-002 | Sensor State Diagram |
| WaterFlowSensor | FR-03 | UC-04 | US-003 | Sensor State Diagram |
| SensorReading | FR-07, FR-08, FR-09, FR-10 | UC-05 | US-006 | SensorData State Diagram |
| CSVStorage | FR-07, FR-08, FR-09 | UC-05 | US-006 | CSVFile State Diagram |
| Dashboard | FR-11, FR-12, FR-13, FR-14, FR-15, FR-16 | UC-06, UC-07, UC-08, UC-09 | US-007, US-008, US-009 | Dashboard State Diagram |
| Configuration | FR-04, FR-05 | UC-01 | US-004 | Configuration State Diagram |

---

## Domain Entities

### Entity 1: Sensor (Abstract Base Class)

| Attribute | Type | Description |
|-----------|------|-------------|
| sensorId | String | Unique identifier (e.g., "temp_1") |
| sensorType | String | Type of sensor (temperature, humidity, water) |
| isEnabled | Boolean | Whether sensor is active |
| currentValue | Float | Most recent reading |
| lastUpdate | DateTime | Timestamp of last reading |

| Method | Description |
|--------|-------------|
| generateReading() | Produces a new sensor reading (abstract method) |
| enable() | Activates the sensor |
| disable() | Deactivates the sensor |
| getStatus() | Returns current sensor state |

**Relationships:**
- Sensor is inherited by TemperatureSensor, HumiditySensor, WaterFlowSensor
- Sensor produces SensorReading objects (composition)

**Business Rules:**
- A sensor can only generate readings when isEnabled = true
- Each sensor must have a unique sensorId
- sensorId format: [type]_[number] (e.g., "temp_1")

---

### Entity 2: TemperatureSensor (Concrete Class)

| Attribute | Type | Description |
|-----------|------|-------------|
| minTemp | Float | Minimum temperature value (18°C) |
| maxTemp | Float | Maximum temperature value (25°C) |
| timeOfDay | Integer | Current hour (0-23) for daily cycle |

| Method | Description |
|--------|-------------|
| generateReading() | Returns temperature based on sine wave |
| calculateDailyCycle() | Determines temperature based on time |
| validateReading(value) | Checks if value is within 18-25°C |

**Relationships:**
- Inherits from Sensor (inheritance)

**Business Rules:**
- Temperature follows sine wave: peak at 2pm (25°C), minimum at 4am (18°C)
- Values never outside 18-25°C range

---

### Entity 3: HumiditySensor (Concrete Class)

| Attribute | Type | Description |
|-----------|------|-------------|
| minHumidity | Float | Minimum humidity value (30%) |
| maxHumidity | Float | Maximum humidity value (70%) |
| previousValue | Float | Last reading for change calculation |

| Method | Description |
|--------|-------------|
| generateReading() | Returns random humidity value |
| validateChange(value) | Ensures change from previous ≤5% |
| regenerateIfNeeded() | Retries if change too large |

**Relationships:**
- Inherits from Sensor (inheritance)

**Business Rules:**
- Humidity must be between 30-70%
- Change from previous reading cannot exceed 5%
- If change >5%, regenerate until valid

---

### Entity 4: WaterFlowSensor (Concrete Class)

| Attribute | Type | Description |
|-----------|------|-------------|
| minFlow | Float | Minimum flow value (0 L/min) |
| maxFlow | Float | Maximum flow value (100 L/min) |
| spikeCounter | Integer | Tracks readings since last spike |
| spikeThreshold | Integer | When to trigger spike (10-20) |

| Method | Description |
|--------|-------------|
| generateReading() | Returns flow value (baseline or spike) |
| shouldSpike() | Checks if spike counter reached threshold |
| resetSpikeCounter() | Resets after spike occurs |

**Relationships:**
- Inherits from Sensor (inheritance)

**Business Rules:**
- Normal flow: 0-20 L/min
- Spikes: 50-100 L/min every 10-20 readings
- Spike counter resets after each spike

---

### Entity 5: SensorReading

| Attribute | Type | Description |
|-----------|------|-------------|
| readingId | String | Unique identifier |
| sensorId | String | References the sensor that generated it |
| sensorType | String | Type of sensor |
| value | Float | The sensor reading value |
| timestamp | DateTime | ISO format with milliseconds |
| isAnomaly | Boolean | Whether value is outside normal range |

| Method | Description |
|--------|-------------|
| toCSVRow() | Formats reading as CSV string |
| validate() | Checks if reading is valid |
| flagAnomaly() | Marks reading as anomaly if out of range |

**Relationships:**
- SensorReading is composed by Sensor (composition - Sensor cannot exist without readings)
- SensorReading is stored in CSVStorage

**Business Rules:**
- Each reading must have a valid timestamp
- timestamp format: YYYY-MM-DD HH:MM:SS.fff
- Temperature anomaly: outside 18-25°C
- Humidity anomaly: outside 30-70%
- Water flow anomaly: none (spikes are expected)

---

### Entity 6: CSVStorage

| Attribute | Type | Description |
|-----------|------|-------------|
| fileName | String | "sensor_data.csv" |
| headers | List | ["timestamp","sensor_type","sensor_id","value"] |
| isWritable | Boolean | File access status |

| Method | Description |
|--------|-------------|
| createFile() | Creates CSV file with headers |
| appendReading(reading) | Adds a new row to CSV file |
| readAllReadings() | Returns all readings from file |
| checkFileExists() | Verifies file on disk |

**Relationships:**
- CSVStorage stores SensorReading objects (aggregation)

**Business Rules:**
- File created with headers if not exists
- Readings appended, never overwritten
- File location: same directory as simulator

---

### Entity 7: Dashboard

| Attribute | Type | Description |
|-----------|------|-------------|
| refreshInterval | Integer | 2 seconds |
| dataWindow | Integer | Last 5 minutes of data |
| csvFilePath | String | Path to sensor_data.csv |
| isRunning | Boolean | Dashboard status |

| Method | Description |
|--------|-------------|
| loadData() | Reads CSV file |
| updateCharts() | Refreshes temperature, humidity, water flow charts |
| updateCurrentValues() | Displays latest readings |
| autoRefresh() | Loops every 2 seconds |

**Relationships:**
- Dashboard reads from CSVStorage
- Dashboard displays SensorReading data

**Business Rules:**
- Dashboard refreshes every 2 seconds
- Charts show last 5 minutes of data only
- Dashboard displays temperature (18-25°C), humidity (30-70%), water flow (0-100 L/min)

---

### Entity 8: Configuration

| Attribute | Type | Description |
|-----------|------|-------------|
| configPath | String | "config.json" |
| updateFrequency | Integer | Sensor generation interval (seconds) |
| temperatureRange | Object | minTemp, maxTemp |
| humidityRange | Object | minHumidity, maxHumidity |
| waterFlowRange | Object | minFlow, maxFlow |
| deterministicMode | Boolean | Fixed random seed |
| enabledSensors | List | Which sensors are active |

| Method | Description |
|--------|-------------|
| loadConfig() | Reads config.json file |
| saveConfig() | Writes to config.json |
| validateSettings() | Checks if values are valid |
| applySettings() | Updates simulation behavior |

**Relationships:**
- Configuration controls all Sensor objects

**Business Rules:**
- Default config created if file missing
- Invalid values revert to previous settings
- deterministic_mode = true uses fixed random seed

---


