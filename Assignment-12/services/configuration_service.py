from typing import Optional
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repositories.inmemory.inmemory_configuration_repository import InMemoryConfigurationRepository
from models import Configuration


class ConfigurationService:
    def __init__(self, repository: InMemoryConfigurationRepository):
        self.repo = repository
    
    def get_config(self) -> Configuration:
        config = self.repo.get_config()
        if not config:
            config = Configuration()
            self.repo.save(config)
        return config
    
    def update_config(self, new_config: Configuration) -> Configuration:
        if new_config.update_frequency < 1 or new_config.update_frequency > 60:
            raise ValueError("Update frequency must be between 1 and 60 seconds")
        self.repo.save(new_config)
        return new_config