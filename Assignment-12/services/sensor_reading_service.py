from typing import List, Optional
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repositories.inmemory.inmemory_sensor_reading_repository import InMemorySensorReadingRepository
from models import SensorReading


class SensorReadingService:
    def __init__(self, repository: InMemorySensorReadingRepository):
        self.repo = repository
    
    def create_reading(self, reading: SensorReading) -> SensorReading:
        # Business rule: validate value range
        if reading.sensor_type == "temperature" and not (18 <= reading.value <= 25):
            raise ValueError("Temperature must be between 18 and 25")
        if reading.sensor_type == "humidity" and not (30 <= reading.value <= 70):
            raise ValueError("Humidity must be between 30 and 70")
        if reading.sensor_type == "water" and not (0 <= reading.value <= 100):
            raise ValueError("Water flow must be between 0 and 100")
        self.repo.save(reading)
        return reading
    
    def get_all_readings(self) -> List[SensorReading]:
        return self.repo.find_all()
    
    def get_reading(self, reading_id: str) -> Optional[SensorReading]:
        return self.repo.find_by_id(reading_id)
    
    def delete_reading(self, reading_id: str) -> None:
        self.repo.delete(reading_id)
    
    def get_anomalies(self) -> List[SensorReading]:
        return self.repo.find_anomalies()