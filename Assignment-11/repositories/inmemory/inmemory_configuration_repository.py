"""
In-Memory Implementation of ConfigurationRepository
"""

from typing import List, Optional
from repositories.configuration_repository import ConfigurationRepository
from configuration import Configuration


class InMemoryConfigurationRepository(ConfigurationRepository):
    """In-memory HashMap implementation of ConfigurationRepository."""
    
    def __init__(self):
        self._storage: dict[str, Configuration] = {}
        self._current_config = None
    
    def save(self, entity: Configuration) -> None:
        """Save the configuration (only one instance)."""
        self._current_config = entity
        self._storage["singleton"] = entity
    
    def find_by_id(self, id: str) -> Optional[Configuration]:
        """Find configuration by ID."""
        return self._storage.get(id)
    
    def find_all(self) -> List[Configuration]:
        """Find all configurations (should be only one)."""
        return [self._current_config] if self._current_config else []
    
    def delete(self, id: str) -> None:
        """Delete the configuration."""
        if id in self._storage:
            del self._storage[id]
            self._current_config = None
    
    def exists(self, id: str) -> bool:
        """Check if configuration exists."""
        return id in self._storage
    
    def count(self) -> int:
        """Get the number of configurations (0 or 1)."""
        return len(self._storage)
    
    def get_config(self) -> Optional[Configuration]:
        """Get the single configuration instance."""
        return self._current_config
    
    def clear(self) -> None:
        """Clear all storage (for testing)."""
        self._storage.clear()
        self._current_config = None