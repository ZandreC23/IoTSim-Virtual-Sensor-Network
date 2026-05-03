# Changelog

## [Assignment 10] - 2026-04-30

### Added
- Complete class implementations from UML diagram (8 classes):
  - `src/sensor.py` - Abstract base class for all sensors
  - `src/temperature_sensor.py` - Temperature sensor with daily cycle
  - `src/humidity_sensor.py` - Humidity sensor with ≤5% change limit
  - `src/water_flow_sensor.py` - Water flow sensor with spike patterns
  - `src/sensor_reading.py` - Individual sensor reading data point
  - `src/csv_storage.py` - CSV file operations for persistence
  - `src/dashboard.py` - Dashboard class for data visualization
  - `src/configuration.py` - Configuration management (Singleton)

### Added - Creational Patterns (All 6)
- `creational_patterns/simple_factory.py` - Simple Factory for sensor creation
- `creational_patterns/factory_method.py` - Factory Method pattern
- `creational_patterns/abstract_factory.py` - Abstract Factory for storage
- `creational_patterns/builder.py` - Builder pattern for SensorReading
- `creational_patterns/prototype.py` - Prototype pattern for cloning sensors
- `creational_patterns/singleton.py` - Singleton pattern for ConfigurationManager

### Added - Unit Tests
- `tests/test_all.py` - 23 unit tests covering all patterns and edge cases
- Test coverage: 23/23 tests passing

### Added - Documentation
- Updated `README.md` with language choice, pattern justifications, and test instructions
- `REFLECTION-ASSIGNMENT-10.md` - 550-word reflection on challenges and trade-offs

### Changed
- None

### Fixed
- None

### Known Issues
- None

---

## [Previous Assignments Summary]

### Assignment 9 - Domain Modeling and Class Diagram
- Domain model with 8 entities
- Mermaid.js class diagram with inheritance, association, aggregation
- Reflection on OO design decisions

### Assignment 8 - State and Activity Modeling
- State transition diagrams for 5 objects
- Activity diagrams for 8 workflows

### Assignment 7 - GitHub Project Templates and Kanban
- Basic Kanban template selection
- Custom columns (Testing, Blocked)
- Kanban board explanation

### Assignment 6 - Agile Planning
- 11 user stories with acceptance criteria
- Product backlog with MoSCoW prioritization
- Sprint planning with 2-week goal

### Assignment 5 - Use Case Modeling
- Use case diagram with 7 actors, 13 use cases
- 8 use case specifications
- Functional and non-functional test cases

### Assignment 4 - Stakeholder Analysis and Requirements
- 7 stakeholders with roles and concerns
- 16 functional requirements (FR-01 to FR-16)
- 13 non-functional requirements (NFR-01 to NFR-13)

### Assignment 3 - System Specification and Architecture
- System specification document
- C4 architecture diagrams (Context, Container, Component, Code)