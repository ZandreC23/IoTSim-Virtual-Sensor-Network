import pytest
import sys
import os

# Force the current directory to be in the path
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import SensorReading, Configuration
from services.sensor_reading_service import SensorReadingService
from services.configuration_service import ConfigurationService
from services.simulation_log_service import SimulationLogService
from repositories.inmemory.inmemory_sensor_reading_repository import InMemorySensorReadingRepository
from repositories.inmemory.inmemory_configuration_repository import InMemoryConfigurationRepository
from repositories.simulation_log_repository import SimulationLogRepository


class TestSensorReadingService:
    def setup_method(self):
        self.repo = InMemorySensorReadingRepository()
        self.service = SensorReadingService(self.repo)
    
    def test_create_valid_reading(self):
        reading = SensorReading(reading_id="r1", sensor_id="s1", sensor_type="temperature", value=22.5)
        result = self.service.create_reading(reading)
        assert result.reading_id == "r1"
    
    def test_create_invalid_temperature(self):
        reading = SensorReading(reading_id="r2", sensor_id="s1", sensor_type="temperature", value=99.0)
        with pytest.raises(ValueError, match="Temperature must be between 18 and 25"):
            self.service.create_reading(reading)
    
    def test_get_all_readings(self):
        r1 = SensorReading(reading_id="r1", sensor_id="s1", sensor_type="temperature", value=22.5)
        r2 = SensorReading(reading_id="r2", sensor_id="s2", sensor_type="humidity", value=55.0)
        self.service.create_reading(r1)
        self.service.create_reading(r2)
        assert len(self.service.get_all_readings()) == 2
    
    def test_delete_reading(self):
        r1 = SensorReading(reading_id="r1", sensor_id="s1", sensor_type="temperature", value=22.5)
        self.service.create_reading(r1)
        self.service.delete_reading("r1")
        assert self.service.get_reading("r1") is None


class TestConfigurationService:
    def setup_method(self):
        self.repo = InMemoryConfigurationRepository()
        self.service = ConfigurationService(self.repo)
    
    def test_get_default_config(self):
        config = self.service.get_config()
        assert config.update_frequency == 5
    
    def test_update_config_valid(self):
        new_config = Configuration(update_frequency=10)
        updated = self.service.update_config(new_config)
        assert updated.update_frequency == 10
    
    def test_update_config_invalid_frequency(self):
        new_config = Configuration(update_frequency=100)
        with pytest.raises(ValueError, match="Update frequency must be between 1 and 60"):
            self.service.update_config(new_config)


class TestSimulationLogService:
    def setup_method(self):
        self.repo = SimulationLogRepository()
        self.service = SimulationLogService(self.repo)
    
    def test_start_simulation(self):
        log = self.service.start_simulation("log1")
        assert log.log_id == "log1"
        assert log.status == "running"
    
    def test_end_simulation(self):
        self.service.start_simulation("log2")
        ended = self.service.end_simulation("log2")
        assert ended.status == "completed"
        assert ended.end_time is not None
    
    def test_end_nonexistent_log(self):
        with pytest.raises(ValueError, match="Simulation log not found"):
            self.service.end_simulation("unknown")
    
    def test_double_start(self):
        self.service.start_simulation("log3")
        with pytest.raises(ValueError, match="Simulation already running"):
            self.service.start_simulation("log3")