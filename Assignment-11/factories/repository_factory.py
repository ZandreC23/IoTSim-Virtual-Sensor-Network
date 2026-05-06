"""
Repository Factory Pattern
Creates the appropriate repository implementation based on storage type.
"""

from repositories.sensor_reading_repository import SensorReadingRepository
from repositories.configuration_repository import ConfigurationRepository
from repositories.inmemory.inmemory_sensor_reading_repository import InMemorySensorReadingRepository
from repositories.inmemory.inmemory_configuration_repository import InMemoryConfigurationRepository


class RepositoryFactory:
    """Factory for creating repository instances."""
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern for factory."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._storage_type = "MEMORY"
    
    def set_storage_type(self, storage_type: str) -> None:
        """
        Set the storage type for future repository creation.
        
        Args:
            storage_type: "MEMORY", "FILE", "DATABASE"
        """
        self._storage_type = storage_type
    
    def get_sensor_reading_repository(self) -> SensorReadingRepository:
        """Create and return a SensorReadingRepository."""
        if self._storage_type == "MEMORY":
            return InMemorySensorReadingRepository()
        elif self._storage_type == "FILE":
            # Stub for future implementation
            raise NotImplementedError("File storage not yet implemented")
        elif self._storage_type == "DATABASE":
            # Stub for future implementation
            raise NotImplementedError("Database storage not yet implemented")
        else:
            raise ValueError(f"Unknown storage type: {self._storage_type}")
    
    def get_configuration_repository(self) -> ConfigurationRepository:
        """Create and return a ConfigurationRepository."""
        if self._storage_type == "MEMORY":
            return InMemoryConfigurationRepository()
        elif self._storage_type == "FILE":
            raise NotImplementedError("File storage not yet implemented")
        elif self._storage_type == "DATABASE":
            raise NotImplementedError("Database storage not yet implemented")
        else:
            raise ValueError(f"Unknown storage type: {self._storage_type}")


# Global factory instance
repository_factory = RepositoryFactory()