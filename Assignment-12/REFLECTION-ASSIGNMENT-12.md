# Reflection: Assignment 12 — Service Layer & REST API

## What I Built
I implemented a full service layer and REST API for the IoTSim Virtual Sensor Network Simulator using FastAPI. The system includes three services (SensorReadingService, ConfigurationService, SimulationLogService), a complete set of REST endpoints, and 21 passing tests.

## Challenges Faced
The biggest challenge was resolving Python module import conflicts between Assignment-11 and Assignment-12. The inmemory repositories from Assignment-11 were written for an older class-based model using getter methods (e.g., `get_reading_id()`), while Assignment-12 uses Pydantic models with direct attribute access. This required updating the repositories to work with the new models.

A secondary challenge was that pytest does not automatically add the project root to `sys.path`, which caused `ModuleNotFoundError` on every test run. This was solved using a `conftest.py` with `os.path.abspath` and a `pytest.ini` file.

## Decisions Made
- I chose FastAPI over Flask because it auto-generates Swagger/OpenAPI documentation, which directly satisfies the documentation requirement.
- I kept repositories in-memory rather than using a database, consistent with the approach established in Assignment-11.
- I separated business logic into service classes rather than putting it directly in the API routes, following the repository → service → API layered architecture pattern.

## What I Learned
- How to structure a layered Python application (repository → service → API)
- How FastAPI route ordering matters — more specific routes must be defined before wildcard routes
- How pytest resolves imports and why `conftest.py` is needed for path configuration
- How Swagger UI works and how to use it to test API endpoints interactively