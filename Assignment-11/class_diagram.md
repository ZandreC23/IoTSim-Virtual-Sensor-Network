# Updated Class Diagram with Repository Layer

## Mermaid.js Class Diagram

```mermaid
classDiagram
    %% Repository Interfaces
    class Repository {
        <<interface>>
        +save(entity: T) void
        +find_by_id(id: ID) Optional[T]
        +find_all() List[T]
        +delete(id: ID) void
        +exists(id: ID) bool
        +count() int
    }

    class SensorReadingRepository {
        <<interface>>
        +find_by_sensor_id(sensor_id: str) List[SensorReading]
        +find_by_sensor_type(sensor_type: str) List[SensorReading]
        +find_by_timerange(start, end) List[SensorReading]
        +find_anomalies() List[SensorReading]
    }

    class ConfigurationRepository {
        <<interface>>
        +get_config() Optional[Configuration]
    }

    %% Concrete Implementations
    class InMemorySensorReadingRepository {
        -_storage: dict
        -_id_counter: int
        +save(entity) void
        +find_by_id(id) Optional[SensorReading]
        +find_all() List[SensorReading]
        +delete(id) void
        +exists(id) bool
        +count() int
        +find_by_sensor_id(sensor_id) List[SensorReading]
        +find_by_sensor_type(sensor_type) List[SensorReading]
        +find_by_timerange(start, end) List[SensorReading]
        +find_anomalies() List[SensorReading]
        +clear() void
    }

    class InMemoryConfigurationRepository {
        -_storage: dict
        -_current_config: Configuration
        +save(entity) void
        +find_by_id(id) Optional[Configuration]
        +find_all() List[Configuration]
        +delete(id) void
        +exists(id) bool
        +count() int
        +get_config() Optional[Configuration]
        +clear() void
    }

    %% Factory
    class RepositoryFactory {
        -_storage_type: str
        +set_storage_type(storage_type) void
        +get_sensor_reading_repository() SensorReadingRepository
        +get_configuration_repository() ConfigurationRepository
    }

    %% Domain Classes (from Assignment 10)
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

    class Configuration {
        -configPath: String
        -updateFrequency: Integer
        -temperatureRange: Object
        -humidityRange: Object
        -waterFlowRange: Object
        -deterministicMode: Boolean
        -enabledSensors: List
        +loadConfig() void
        +saveConfig() void
        +validateSettings() Boolean
        +applySettings() void
    }

    %% Inheritance Relationships
    Repository <|-- SensorReadingRepository
    Repository <|-- ConfigurationRepository
    SensorReadingRepository <|.. InMemorySensorReadingRepository
    ConfigurationRepository <|.. InMemoryConfigurationRepository

    %% Association Relationships
    RepositoryFactory --> SensorReadingRepository : creates
    RepositoryFactory --> ConfigurationRepository : creates
    InMemorySensorReadingRepository --> SensorReading : stores
    InMemoryConfigurationRepository --> Configuration : stores
```
## Repository Pattern

The repository layer abstracts storage details behind interfaces:

| Component | Purpose |
|---|---|
| `Repository<T, ID>` | Generic interface with CRUD operations |
| `SensorReadingRepository` | Entity-specific interface for sensor readings |
| `ConfigurationRepository` | Entity-specific interface for configuration |

### Implementations

| Implementation | Storage | Purpose |
|---|---|---|
| `InMemorySensorReadingRepository` | HashMap | Fast testing, no persistence |
| `InMemoryConfigurationRepository` | HashMap | Testing configuration storage |

---

## Factory Pattern

`RepositoryFactory` switches between storage backends:

- Set `storage_type = "MEMORY"` for in-memory storage
- Future: `"FILE"` for JSON file storage
- Future: `"DATABASE"` for SQL database storage

---

## Future-Proofing

New storage backends can be added by:

1. Creating a new class implementing the interface
2. Adding a new case in `RepositoryFactory`
3. No changes to existing code *(Open/Closed Principle)*
