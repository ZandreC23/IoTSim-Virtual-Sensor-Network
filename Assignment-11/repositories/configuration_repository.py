"""
Configuration Repository Interface
"""

from abc import abstractmethod
from typing import Optional
from repositories.repository_interface import Repository
from configuration import Configuration

class ConfigurationRepository(Repository[Configuration, str]):
    """Repository interface for Configuration entity."""
    
    @abstractmethod
    def get_config(self) -> Optional[Configuration]:
        """Get the single configuration instance."""
        pass