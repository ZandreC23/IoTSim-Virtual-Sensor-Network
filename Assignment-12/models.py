"""
Pydantic models for Assignment 12.
Defines SensorReading, Configuration, and SimulationLog.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class SensorReading(BaseModel):
    reading_id: str
    sensor_id: str
    sensor_type: str
    value: float
    timestamp: datetime = Field(default_factory=datetime.now)
    is_anomaly: bool = False


class Configuration(BaseModel):
    update_frequency: int = 5
    temperature_range: dict = {"min": 18.0, "max": 25.0}
    humidity_range: dict = {"min": 30.0, "max": 70.0}
    water_flow_range: dict = {"min": 0.0, "max": 100.0}
    pressure_range: dict = {"min": 950.0, "max": 1050.0}
    deterministic_mode: bool = False
    enabled_sensors: List[str] = ["temperature", "humidity", "water", "pressure"]


class SimulationLog(BaseModel):
    log_id: str
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    status: str = "running"
    total_readings: int = 0