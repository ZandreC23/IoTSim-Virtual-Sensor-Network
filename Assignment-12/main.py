from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
import sys
import os

from repositories.inmemory.inmemory_sensor_reading_repository import InMemorySensorReadingRepository
from repositories.inmemory.inmemory_configuration_repository import InMemoryConfigurationRepository
from services.sensor_reading_service import SensorReadingService
from services.configuration_service import ConfigurationService
from services.simulation_log_service import SimulationLogService
from repositories.simulation_log_repository import SimulationLogRepository
from models import SensorReading, Configuration, SimulationLog

# Initialize repositories and services
sensor_repo = InMemorySensorReadingRepository()
config_repo = InMemoryConfigurationRepository()
log_repo = SimulationLogRepository()

sensor_service = SensorReadingService(sensor_repo)
config_service = ConfigurationService(config_repo)
log_service = SimulationLogService(log_repo)

app = FastAPI(title="IoTSim API", description="REST API for IoT Simulator", version="1.0.0")

# ========== SensorReading endpoints ==========
@app.post("/api/readings", response_model=SensorReading, status_code=status.HTTP_201_CREATED, tags=["Readings"])
def create_reading(reading: SensorReading):
    # Add validation for sensor_id
    if hasattr(reading, 'sensor_id') and reading.sensor_id is not None:
    if not reading.sensor_id.strip():
        raise HTTPException(status_code=400, detail="sensor_id cannot be empty")
    if len(reading.sensor_id) < 3:
        raise HTTPException(status_code=400, detail="sensor_id must be at least 3 characters long")

    try:
        return sensor_service.create_reading(reading)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/readings", response_model=List[SensorReading], tags=["Readings"])
def get_all_readings():
    return sensor_service.get_all_readings()

@app.get("/api/readings/anomalies", response_model=List[SensorReading], tags=["Readings"])
def get_anomalies():
    return sensor_service.get_anomalies()

@app.get("/api/readings/{reading_id}", response_model=SensorReading, tags=["Readings"])
def get_reading(reading_id: str):
    reading = sensor_service.get_reading(reading_id)
    if not reading:
        raise HTTPException(status_code=404, detail="Reading not found")
    return reading

@app.delete("/api/readings/{reading_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Readings"])
def delete_reading(reading_id: str):
    if not sensor_service.get_reading(reading_id):
        raise HTTPException(status_code=404, detail="Reading not found")
    sensor_service.delete_reading(reading_id)
    return JSONResponse(content=None, status_code=204)

# ========== Configuration endpoints ==========
@app.get("/api/config", response_model=Configuration, tags=["Configuration"])
def get_config():
    return config_service.get_config()

@app.put("/api/config", response_model=Configuration, tags=["Configuration"])
def update_config(config: Configuration):
    try:
        return config_service.update_config(config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ========== SimulationLog endpoints ==========
@app.post("/api/simulations/{log_id}/start", response_model=SimulationLog, tags=["Simulations"])
def start_simulation(log_id: str):
    try:
        return log_service.start_simulation(log_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/simulations/{log_id}/end", response_model=SimulationLog, tags=["Simulations"])
def end_simulation(log_id: str):
    try:
        return log_service.end_simulation(log_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/simulations", response_model=List[SimulationLog], tags=["Simulations"])
def get_all_simulations():
    return log_service.get_all_logs()

@app.get("/api/simulations/{log_id}", response_model=SimulationLog, tags=["Simulations"])
def get_simulation(log_id: str):
    log = log_service.get_log(log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Simulation log not found")
    return log