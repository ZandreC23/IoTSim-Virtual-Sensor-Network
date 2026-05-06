"""
SensorReading Repository Interface
"""

from abc import abstractmethod
from typing import List
from datetime import datetime
from repositories.repository_interface import Repository
from sensor_reading import SensorReading


class SensorReadingRepository(Repository[SensorReading, str]):
    """Repository interface for SensorReading entities."""
    
    @abstractmethod
    def find_by_sensor_id(self, sensor_id: str) -> List[SensorReading]:
        """Find all readings from a specific sensor."""
        pass
    
    @abstractmethod
    def find_by_sensor_type(self, sensor_type: str) -> List[SensorReading]:
        """Find all readings of a specific sensor type."""
        pass
    
    @abstractmethod
    def find_by_timerange(self, start_time: datetime, end_time: datetime) -> List[SensorReading]:
        """Find readings within a time range."""
        pass
    
    @abstractmethod
    def find_anomalies(self) -> List[SensorReading]:
        """Find all readings marked as anomalies."""
        pass