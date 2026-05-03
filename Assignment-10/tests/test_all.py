"""
Unit tests for all creational patterns and classes.
Run with: python -m pytest tests/test_all.py -v
"""

import unittest
import sys
import os
import threading
import tempfile
import csv

# Add the Assignment-10 directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.temperature_sensor import TemperatureSensor
from src.humidity_sensor import HumiditySensor
from src.water_flow_sensor import WaterFlowSensor
from src.sensor_reading import SensorReading
from src.csv_storage import CSVStorage
from src.dashboard import Dashboard
from src.configuration import Configuration
from creational_patterns.simple_factory import SensorFactory
from creational_patterns.factory_method import (TemperatureSensorCreator, 
                                                 HumiditySensorCreator, 
                                                 WaterFlowSensorCreator)
from creational_patterns.abstract_factory import CSVStorageFactory, JSONStorageFactory
from creational_patterns.builder import SensorReadingBuilder, SensorReadingDirector
from creational_patterns.prototype import (TemperatureSensorPrototype, 
                                           HumiditySensorPrototype, 
                                           WaterFlowSensorPrototype,
                                           SensorCache)
from creational_patterns.singleton import ConfigurationManager, DatabaseConnection


# ============================================================
# TEST CLASS 1: Sensor Classes
# ============================================================

class TestSensorClasses(unittest.TestCase):
    """Test basic sensor classes and edge cases."""
    
    def test_temperature_sensor_creation(self):
        sensor = TemperatureSensor("temp_1", 18, 25)
        self.assertEqual(sensor.get_sensor_id(), "temp_1")
        self.assertEqual(sensor.get_sensor_type(), "temperature")
        self.assertEqual(sensor.get_status(), "Enabled")
    
    def test_temperature_sensor_generate_reading(self):
        sensor = TemperatureSensor("temp_1", 18, 25)
        reading = sensor.generate_reading()
        self.assertGreaterEqual(reading, 18)
        self.assertLessEqual(reading, 25)
    
    def test_temperature_sensor_disable(self):
        sensor = TemperatureSensor("temp_1", 18, 25)
        sensor.disable()
        self.assertEqual(sensor.get_status(), "Disabled")
        with self.assertRaises(RuntimeError):
            sensor.generate_reading()
    
    def test_temperature_sensor_out_of_range(self):
        sensor = TemperatureSensor("temp_1", 18, 25)
        self.assertTrue(sensor.validate_reading(20.0))
        self.assertFalse(sensor.validate_reading(99.0))
        self.assertFalse(sensor.validate_reading(10.0))
    
    def test_humidity_sensor_creation(self):
        sensor = HumiditySensor("hum_1", 30, 70)
        self.assertEqual(sensor.get_sensor_id(), "hum_1")
        self.assertEqual(sensor.get_sensor_type(), "humidity")
    
    def test_humidity_sensor_change_limit(self):
        sensor = HumiditySensor("hum_1", 30, 70)
        sensor._previous_value = 50
        self.assertTrue(sensor.validate_change(52.0))
        self.assertFalse(sensor.validate_change(60.0))
    
    def test_water_flow_sensor_creation(self):
        sensor = WaterFlowSensor("water_1", 0, 100)
        self.assertEqual(sensor.get_sensor_id(), "water_1")
        self.assertEqual(sensor.get_sensor_type(), "water")
    
    def test_water_flow_spike_generation(self):
        """Edge case: Test that spikes are >= 50 L/min"""
        sensor = WaterFlowSensor("water_1", 0, 100)
        sensor.set_deterministic_mode(True)
        # Force spike by setting counter >= threshold
        sensor._spike_counter = 15
        sensor._spike_threshold = 15
        reading = sensor.generate_reading()
        self.assertGreaterEqual(reading, 50)
    
    def test_sensor_reading_creation(self):
        reading = SensorReading("read_1", "temp_1", "temperature", 22.5)
        self.assertEqual(reading.get_reading_id(), "read_1")
        self.assertEqual(reading.get_value(), 22.5)
    
    def test_sensor_reading_validation(self):
        valid_temp = SensorReading("r1", "s1", "temperature", 22.5)
        invalid_temp = SensorReading("r2", "s1", "temperature", 99.0)
        valid_humidity = SensorReading("r3", "s2", "humidity", 55.0)
        invalid_humidity = SensorReading("r4", "s2", "humidity", 99.0)
        
        self.assertTrue(valid_temp.validate())
        self.assertFalse(invalid_temp.validate())
        self.assertTrue(valid_humidity.validate())
        self.assertFalse(invalid_humidity.validate())
    
    def test_sensor_reading_to_csv(self):
        reading = SensorReading("read_1", "temp_1", "temperature", 22.5)
        csv_row = reading.to_csv_row()
        self.assertIn("22.5", csv_row)
        self.assertIn("temperature", csv_row)
        self.assertIn("temp_1", csv_row)
    
    def test_sensor_reading_anomaly_flag(self):
        reading = SensorReading("read_1", "temp_1", "temperature", 99.0)
        self.assertFalse(reading.is_anomaly())
        reading.flag_anomaly()
        self.assertTrue(reading.is_anomaly())


# ============================================================
# TEST CLASS 2: CSV Storage
# ============================================================

class TestCSVStorage(unittest.TestCase):
    """Test CSVStorage class with temporary files."""
    
    def setUp(self):
        """Create a temporary CSV file for testing"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_file.close()
        self.csv_storage = CSVStorage(self.temp_file.name)
    
    def tearDown(self):
        """Remove temporary file after test"""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)
    
    def test_csv_file_creation(self):
        """Test that CSV file is created with headers"""
        self.csv_storage.create_file()
        self.assertTrue(os.path.exists(self.temp_file.name))
        
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
            self.assertIn("timestamp", content)
            self.assertIn("sensor_type", content)
    
    def test_append_reading(self):
        """Test appending a reading to CSV file"""
        self.csv_storage.create_file()
        
        reading = SensorReading("r1", "temp_1", "temperature", 22.5)
        result = self.csv_storage.append_reading(reading)
        self.assertTrue(result)
        
        with open(self.temp_file.name, 'r') as f:
            lines = f.readlines()
            # Should be header + 1 data row
            self.assertGreaterEqual(len(lines), 2)
    
    def test_read_all_readings_empty(self):
        """Edge case: Read from empty CSV file"""
        self.csv_storage.create_file()
        readings = self.csv_storage.read_all_readings()
        self.assertEqual(len(readings), 0)
    
    def test_check_file_exists(self):
        """Test file existence check"""
        # File should not exist before creation
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)
        self.assertFalse(self.csv_storage.check_file_exists())
        self.csv_storage.create_file()
        self.assertTrue(self.csv_storage.check_file_exists())


# ============================================================
# TEST CLASS 3: Dashboard
# ============================================================

class TestDashboard(unittest.TestCase):
    """Test Dashboard class."""
    
    def setUp(self):
        """Create a temporary CSV storage for testing"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_file.close()
        self.csv_storage = CSVStorage(self.temp_file.name)
        self.csv_storage.create_file()
        self.dashboard = Dashboard(self.csv_storage)
    
    def tearDown(self):
        """Remove temporary file after test"""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)
    
    def test_dashboard_start_stop(self):
        self.dashboard.start()
        self.assertTrue(self.dashboard.is_running())
        self.dashboard.stop()
        self.assertFalse(self.dashboard.is_running())
    
    def test_dashboard_refresh_interval(self):
        self.assertEqual(self.dashboard.get_refresh_interval(), 2)
    
    def test_dashboard_load_data_empty(self):
        data = self.dashboard.load_data()
        self.assertEqual(len(data), 0)
    
    def test_dashboard_load_data_with_reading(self):
        reading = SensorReading("r1", "temp_1", "temperature", 22.5)
        self.csv_storage.append_reading(reading)
        data = self.dashboard.load_data()
        self.assertEqual(len(data), 1)


# ============================================================
# TEST CLASS 4: Configuration
# ============================================================

class TestConfiguration(unittest.TestCase):
    """Test Configuration class."""
    
    def test_configuration_set_update_frequency(self):
        config = Configuration()
        config.set_update_frequency(10)
        self.assertEqual(config.get_update_frequency(), 10)
    
    def test_configuration_invalid_update_frequency(self):
        config = Configuration()
        config.set_update_frequency(200)
        self.assertNotEqual(config.get_update_frequency(), 200)
    
    def test_configuration_validation(self):
        config = Configuration()
        config._update_frequency = 5
        config._temperature_range = {"min": 18, "max": 25}
        config._humidity_range = {"min": 30, "max": 70}
        config._water_flow_range = {"min": 0, "max": 100}
        self.assertTrue(config.validate_settings())
    
    def test_configuration_temperature_range_validation(self):
        config = Configuration()
        config._temperature_range = {"min": 30, "max": 20}
        self.assertFalse(config.validate_settings())
    
    def test_configuration_getters(self):
        config = Configuration()
        temp_range = config.get_temperature_range()
        humidity_range = config.get_humidity_range()
        water_range = config.get_water_flow_range()
        
        self.assertIn("min", temp_range)
        self.assertIn("max", humidity_range)
        self.assertIn("min", water_range)


# ============================================================
# TEST CLASS 5: Simple Factory
# ============================================================

class TestSimpleFactory(unittest.TestCase):
    def test_create_temperature_sensor(self):
        sensor = SensorFactory.create_sensor("temperature", "temp_1")
        self.assertEqual(sensor.get_sensor_type(), "temperature")
    
    def test_create_humidity_sensor(self):
        sensor = SensorFactory.create_sensor("humidity", "hum_1")
        self.assertEqual(sensor.get_sensor_type(), "humidity")
    
    def test_create_water_sensor(self):
        sensor = SensorFactory.create_sensor("water", "water_1")
        self.assertEqual(sensor.get_sensor_type(), "water")
    
    def test_create_unknown_sensor(self):
        with self.assertRaises(ValueError):
            SensorFactory.create_sensor("unknown", "unknown_1")
    
    def test_create_multiple_sensors(self):
        configs = [
            {"type": "temperature", "id": "temp_1"},
            {"type": "humidity", "id": "hum_1"},
            {"type": "water", "id": "water_1"}
        ]
        sensors = SensorFactory.create_multiple_sensors(configs)
        self.assertEqual(len(sensors), 3)


# ============================================================
# TEST CLASS 6: Factory Method
# ============================================================

class TestFactoryMethod(unittest.TestCase):
    def test_temperature_creator(self):
        creator = TemperatureSensorCreator(18, 25)
        sensor = creator.create_sensor("temp_1")
        self.assertEqual(sensor.get_sensor_type(), "temperature")
    
    def test_humidity_creator(self):
        creator = HumiditySensorCreator(30, 70)
        sensor = creator.create_sensor("hum_1")
        self.assertEqual(sensor.get_sensor_type(), "humidity")
    
    def test_water_creator(self):
        creator = WaterFlowSensorCreator(0, 100)
        sensor = creator.create_sensor("water_1")
        self.assertEqual(sensor.get_sensor_type(), "water")
    
    def test_creator_with_custom_ranges(self):
        creator = TemperatureSensorCreator(15, 35)
        sensor = creator.create_sensor("temp_1")
        self.assertEqual(sensor.get_min_temp(), 15)
        self.assertEqual(sensor.get_max_temp(), 35)


# ============================================================
# TEST CLASS 7: Abstract Factory
# ============================================================

class TestAbstractFactory(unittest.TestCase):
    def test_csv_storage_factory(self):
        factory = CSVStorageFactory()
        storage = factory.create_storage()
        self.assertIsNotNone(storage)
    
    def test_json_storage_factory(self):
        factory = JSONStorageFactory()
        storage = factory.create_storage()
        self.assertIsNotNone(storage)


# ============================================================
# TEST CLASS 8: Builder
# ============================================================

class TestBuilder(unittest.TestCase):
    def test_builder_create_reading(self):
        builder = SensorReadingBuilder()
        reading = (builder
                   .set_reading_id("read_1")
                   .set_sensor_id("temp_1")
                   .set_sensor_type("temperature")
                   .set_value(22.5)
                   .build())
        self.assertEqual(reading.get_value(), 22.5)
    
    def test_builder_missing_reading_id(self):
        builder = SensorReadingBuilder()
        with self.assertRaises(ValueError):
            (builder
             .set_sensor_id("temp_1")
             .set_sensor_type("temperature")
             .set_value(22.5)
             .build())
    
    def test_builder_missing_sensor_id(self):
        builder = SensorReadingBuilder()
        with self.assertRaises(ValueError):
            (builder
             .set_reading_id("read_1")
             .set_sensor_type("temperature")
             .set_value(22.5)
             .build())
    
    def test_builder_missing_value(self):
        builder = SensorReadingBuilder()
        with self.assertRaises(ValueError):
            (builder
             .set_reading_id("read_1")
             .set_sensor_id("temp_1")
             .set_sensor_type("temperature")
             .build())
    
    def test_director_build_temperature(self):
        builder = SensorReadingBuilder()
        director = SensorReadingDirector(builder)
        reading = director.build_temperature_reading("temp_1", 22.5)
        self.assertEqual(reading.get_sensor_type(), "temperature")
    
    def test_director_build_humidity(self):
        builder = SensorReadingBuilder()
        director = SensorReadingDirector(builder)
        reading = director.build_humidity_reading("hum_1", 55.0)
        self.assertEqual(reading.get_sensor_type(), "humidity")
    
    def test_director_build_water(self):
        builder = SensorReadingBuilder()
        director = SensorReadingDirector(builder)
        reading = director.build_water_reading("water_1", 15.0)
        self.assertEqual(reading.get_sensor_type(), "water")


# ============================================================
# TEST CLASS 9: Prototype
# ============================================================

class TestPrototype(unittest.TestCase):
    def test_temperature_prototype_clone(self):
        original = TemperatureSensorPrototype("temp_1", 18, 25)
        clone = original.clone()
        self.assertEqual(original.get_min_temp(), clone.get_min_temp())
        self.assertEqual(original.get_max_temp(), clone.get_max_temp())
        self.assertIsNot(original, clone)
    
    def test_humidity_prototype_clone(self):
        original = HumiditySensorPrototype("hum_1", 30, 70)
        clone = original.clone()
        self.assertEqual(original.get_min_humidity(), clone.get_min_humidity())
        self.assertIsNot(original, clone)
    
    def test_water_prototype_clone(self):
        original = WaterFlowSensorPrototype("water_1", 0, 100)
        clone = original.clone()
        self.assertEqual(original.get_min_flow(), clone.get_min_flow())
        self.assertIsNot(original, clone)
    
    def test_sensor_cache(self):
        cache = SensorCache()
        prototype = TemperatureSensorPrototype("temp_1", 18, 25)
        cache.add_prototype("temp", prototype)
        clone1 = cache.get_clone("temp")
        clone2 = cache.get_clone("temp")
        self.assertIsNot(clone1, clone2)
    
    def test_cache_missing_key(self):
        cache = SensorCache()
        with self.assertRaises(ValueError):
            cache.get_clone("nonexistent")
    
    def test_prototype_independent_modification(self):
        original = TemperatureSensorPrototype("temp_1", 18, 25)
        clone = original.clone()
        clone._sensor_id = "cloned_temp"
        
        self.assertEqual(original.get_sensor_id(), "temp_1")
        self.assertEqual(clone.get_sensor_id(), "cloned_temp")
        self.assertNotEqual(original.get_sensor_id(), clone.get_sensor_id())


# ============================================================
# TEST CLASS 10: Singleton
# ============================================================

class TestSingleton(unittest.TestCase):
    def test_configuration_manager_singleton(self):
        config1 = ConfigurationManager()
        config2 = ConfigurationManager()
        self.assertIs(config1, config2)
    
    def test_configuration_manager_set_get(self):
        config = ConfigurationManager()
        config.set_config("test_key", "test_value")
        self.assertEqual(config.get_config("test_key"), "test_value")
    
    def test_database_connection_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)
    
    def test_database_connection_connect(self):
        db = DatabaseConnection()
        result = db.connect("localhost:5432")
        self.assertTrue(result)
    
    def test_singleton_thread_safety(self):
        instances = []
        
        def create_instance():
            instances.append(ConfigurationManager())
        
        threads = []
        for _ in range(10):
            t = threading.Thread(target=create_instance)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        first = instances[0]
        for instance in instances:
            self.assertIs(first, instance)
    
    def test_configuration_state_persistence(self):
        config1 = ConfigurationManager()
        config1.set_config("persistent_key", "persistent_value")
        
        config2 = ConfigurationManager()
        self.assertEqual(config2.get_config("persistent_key"), "persistent_value")


if __name__ == "__main__":
    unittest.main()