"""
Abstract Factory Pattern
Create families of related objects (storage factories).
"""

from abc import ABC, abstractmethod
from typing import List
from src.sensor_reading import SensorReading


class Storage(ABC):
    """Abstract product for storage."""
    
    @abstractmethod
    def save(self, reading: SensorReading) -> bool:
        pass
    
    @abstractmethod
    def load_all(self) -> List[SensorReading]:
        pass


class CSVStorageAdapter(Storage):
    """Concrete product for CSV storage."""
    
    def __init__(self, file_name: str = "sensor_data.csv"):
        self._file_name = file_name
    
    def save(self, reading: SensorReading) -> bool:
        # Simplified save for demonstration
        print(f"Saving to CSV: {reading.to_csv_row()}")
        return True
    
    def load_all(self) -> List[SensorReading]:
        print(f"Loading from CSV: {self._file_name}")
        return []


class JSONStorageAdapter(Storage):
    """Concrete product for JSON storage (demonstration only)."""
    
    def __init__(self, file_name: str = "sensor_data.json"):
        self._file_name = file_name
    
    def save(self, reading: SensorReading) -> bool:
        print(f"Saving to JSON: {reading.get_value()}")
        return True
    
    def load_all(self) -> List[SensorReading]:
        print(f"Loading from JSON: {self._file_name}")
        return []


class StorageFactory(ABC):
    """Abstract factory for creating storage objects."""
    
    @abstractmethod
    def create_storage(self) -> Storage:
        pass


class CSVStorageFactory(StorageFactory):
    """Concrete factory for CSV storage."""
    
    def __init__(self, file_name: str = "sensor_data.csv"):
        self._file_name = file_name
    
    def create_storage(self) -> Storage:
        return CSVStorageAdapter(self._file_name)


class JSONStorageFactory(StorageFactory):
    """Concrete factory for JSON storage."""
    
    def __init__(self, file_name: str = "sensor_data.json"):
        self._file_name = file_name
    
    def create_storage(self) -> Storage:
        return JSONStorageAdapter(self._file_name)


def configure_storage(factory: StorageFactory) -> Storage:
    """Client code that uses the abstract factory."""
    return factory.create_storage()


# Example usage
if __name__ == "__main__":
    # Use CSV storage
    csv_factory = CSVStorageFactory()
    csv_storage = configure_storage(csv_factory)
    csv_storage.save(None)
    
    # Use JSON storage
    json_factory = JSONStorageFactory()
    json_storage = configure_storage(json_factory)
    json_storage.save(None)
    
    print("Abstract Factory pattern demonstrated with CSV and JSON storage options.")