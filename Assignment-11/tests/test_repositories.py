"""
Unit tests for Repository layer.
Run with: python -m pytest tests/test_repositories.py -v
"""

import unittest
import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from local Assignment-11 files
from sensor_reading import SensorReading
from configuration import Configuration
from repositories.inmemory.inmemory_sensor_reading_repository import InMemorySensorReadingRepository
from repositories.inmemory.inmemory_configuration_repository import InMemoryConfigurationRepository
from factories.repository_factory import RepositoryFactory, repository_factory


class TestInMemorySensorReadingRepository(unittest.TestCase):
    """Test in-memory repository for SensorReading."""
    
    def setUp(self):
        self.repo = InMemorySensorReadingRepository()
        self.reading1 = SensorReading("r1", "temp_1", "temperature", 22.5)
        self.reading2 = SensorReading("r2", "hum_1", "humidity", 55.0)
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.reading1)
        found = self.repo.find_by_id(self.reading1.get_reading_id())
        self.assertIsNotNone(found)
        self.assertEqual(found.get_value(), 22.5)
    
    def test_find_all(self):
        self.repo.save(self.reading1)
        self.repo.save(self.reading2)
        all_readings = self.repo.find_all()
        self.assertEqual(len(all_readings), 2)
    
    def test_delete(self):
        self.repo.save(self.reading1)
        self.repo.delete(self.reading1.get_reading_id())
        found = self.repo.find_by_id(self.reading1.get_reading_id())
        self.assertIsNone(found)
    
    def test_exists(self):
        self.repo.save(self.reading1)
        self.assertTrue(self.repo.exists(self.reading1.get_reading_id()))
        self.assertFalse(self.repo.exists("nonexistent"))
    
    def test_count(self):
        self.repo.save(self.reading1)
        self.repo.save(self.reading2)
        self.assertEqual(self.repo.count(), 2)
    
    def test_find_by_sensor_id(self):
        self.repo.save(self.reading1)
        self.repo.save(self.reading2)
        readings = self.repo.find_by_sensor_id("temp_1")
        self.assertEqual(len(readings), 1)
    
    def test_clear(self):
        self.repo.save(self.reading1)
        self.repo.clear()
        self.assertEqual(self.repo.count(), 0)


class TestInMemoryConfigurationRepository(unittest.TestCase):
    """Test in-memory repository for Configuration."""
    
    def setUp(self):
        self.repo = InMemoryConfigurationRepository()
        self.config = Configuration()
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.config)
        found = self.repo.find_by_id("singleton")
        self.assertIsNotNone(found)
    
    def test_get_config(self):
        self.repo.save(self.config)
        config = self.repo.get_config()
        self.assertIsNotNone(config)
    
    def test_delete(self):
        self.repo.save(self.config)
        self.repo.delete("singleton")
        found = self.repo.find_by_id("singleton")
        self.assertIsNone(found)


class TestRepositoryFactory(unittest.TestCase):
    """Test Repository Factory pattern."""
    
    def test_factory_returns_memory_repository(self):
        factory = RepositoryFactory()
        factory.set_storage_type("MEMORY")
        repo = factory.get_sensor_reading_repository()
        self.assertIsNotNone(repo)
    
    def test_factory_singleton(self):
        factory1 = RepositoryFactory()
        factory2 = RepositoryFactory()
        self.assertIs(factory1, factory2)
    
    def test_invalid_storage_type(self):
        factory = RepositoryFactory()
        factory.set_storage_type("INVALID")
        with self.assertRaises(ValueError):
            factory.get_sensor_reading_repository()


if __name__ == "__main__":
    unittest.main()