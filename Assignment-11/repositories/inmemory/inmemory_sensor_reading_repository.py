"""
In-Memory Implementation of SensorReadingRepository
"""

from typing import List, Optional
from datetime import datetime
from repositories.sensor_reading_repository import SensorReadingRepository
from sensor_reading import SensorReading


class InMemorySensorReadingRepository(SensorReadingRepository):
    """In-memory HashMap implementation of SensorReadingRepository."""
    
    def __init__(self):
        self._storage: dict[str, SensorReading] = {}
        self._id_counter = 0
    
    def _generate_id(self) -> str:
        self._id_counter += 1
        return f"reading_{self._id_counter}"
    
    def save(self, entity: SensorReading) -> None:
        """Save a sensor reading."""
        if entity.get_reading_id() not in self._storage:
            # Create new reading with generated ID
            new_id = self._generate_id()
            # Since SensorReading doesn't have a setter, we'll store by reading_id
            self._storage[entity.get_reading_id()] = entity
        else:
            self._storage[entity.get_reading_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[SensorReading]:
        """Find a reading by its ID."""
        return self._storage.get(id)
    
    def find_all(self) -> List[SensorReading]:
        """Find all readings."""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete a reading by its ID."""
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        """Check if a reading exists."""
        return id in self._storage
    
    def count(self) -> int:
        """Get the number of readings."""
        return len(self._storage)
    
    def find_by_sensor_id(self, sensor_id: str) -> List[SensorReading]:
        """Find all readings from a specific sensor."""
        return [r for r in self._storage.values() if r.get_sensor_id() == sensor_id]
    
    def find_by_sensor_type(self, sensor_type: str) -> List[SensorReading]:
        """Find all readings of a specific sensor type."""
        return [r for r in self._storage.values() if r.get_sensor_type() == sensor_type]
    
    def find_by_timerange(self, start_time: datetime, end_time: datetime) -> List[SensorReading]:
        """Find readings within a time range."""
        return [r for r in self._storage.values() if start_time <= r.get_timestamp() <= end_time]
    
    def find_anomalies(self) -> List[SensorReading]:
        """Find all readings marked as anomalies."""
        return [r for r in self._storage.values() if r.is_anomaly()]
    
    def clear(self) -> None:
        """Clear all storage (for testing)."""
        self._storage.clear()