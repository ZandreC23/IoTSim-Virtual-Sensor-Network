
# Reflection: Assignment 11 - Implementing a Persistence Repository Layer

## Overview

This assignment required me to design and implement a repository layer to persist domain model objects. The key goals were to abstract storage details behind interfaces, support CRUD operations, and use a factory pattern to switch between storage implementations.

## Challenges Faced

### Challenge 1: Generic Repository Interface

Designing a generic interface that works for different entity types (SensorReading, Configuration) was challenging. I used Python's `Generic[T, ID]` from the `typing` module to create type-safe repositories. This allows the same interface to work with any entity type.

**Trade-off:** Using generics adds complexity but eliminates code duplication across entity repositories.

### Challenge 2: In-Memory HashMap Implementation

Implementing the in-memory repository was straightforward but required careful handling of:
- ID generation for new entities
- Proper implementation of all CRUD operations
- Entity-specific query methods (find_by_sensor_id, find_by_timerange, etc.)

All 14 tests pass, confirming the implementation works correctly.

### Challenge 3: Factory Pattern for Storage Abstraction

The RepositoryFactory uses the Singleton pattern to ensure a single factory instance. It switches between storage types ("MEMORY", "FILE", "DATABASE") and returns the appropriate repository implementation.

**Future-proofing:** Adding a new storage backend only requires:
1. Creating a new class implementing the interface
2. Adding a new case in the factory's `if-elif` block

## Alignment with Previous Assignments

| Assignment | How This Aligns |
|------------|-----------------|
| Assignment 10 | Repository stores SensorReading and Configuration objects from Assignment 10 |
| Assignment 9 | Class diagram updated to show repository layer |
| Assignment 5 | CRUD operations map to use cases (Save Data, Load Data) |

## Testing

All 14 unit tests pass, covering:
- Save and find by ID
- Find all, delete, exists, count
- Entity-specific queries (by sensor ID, type, time range, anomalies)
- Factory pattern (storage type switching, singleton)

## Summary

The repository layer successfully abstracts storage details behind clean interfaces. The factory pattern allows easy switching between storage backends. Future storage options (file system, database) can be added without modifying existing code.

**What I would do differently:** Add more edge cases in tests and implement the file system stub fully.
