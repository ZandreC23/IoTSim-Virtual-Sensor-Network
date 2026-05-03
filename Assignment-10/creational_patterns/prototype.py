"""
Prototype Pattern
Clone existing objects to avoid costly initialization.
"""

from abc import ABC, abstractmethod
from typing import Dict
import copy


class SensorPrototype(ABC):
    """Abstract prototype for sensor cloning."""
    
    @abstractmethod
    def clone(self):
        """Create a clone of the sensor."""
        pass


class TemperatureSensorPrototype(SensorPrototype):
    """Prototype for temperature sensors."""
    
    def __init__(self, sensor_id: str, min_temp: float = 18.0, max_temp: float = 25.0):
        self._sensor_id = sensor_id
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._sensor_type = "temperature"
    
    def clone(self):
        """Create a deep copy of this sensor."""
        return copy.deepcopy(self)
    
    def get_sensor_id(self):
        return self._sensor_id
    
    def get_sensor_type(self):
        return self._sensor_type
    
    def get_min_temp(self):
        return self._min_temp
    
    def get_max_temp(self):
        return self._max_temp


class HumiditySensorPrototype(SensorPrototype):
    """Prototype for humidity sensors."""
    
    def __init__(self, sensor_id: str, min_humidity: float = 30.0, max_humidity: float = 70.0):
        self._sensor_id = sensor_id
        self._min_humidity = min_humidity
        self._max_humidity = max_humidity
        self._sensor_type = "humidity"
    
    def clone(self):
        return copy.deepcopy(self)
    
    def get_sensor_id(self):
        return self._sensor_id
    
    def get_sensor_type(self):
        return self._sensor_type
    
    def get_min_humidity(self):
        return self._min_humidity
    
    def get_max_humidity(self):
        return self._max_humidity


class WaterFlowSensorPrototype(SensorPrototype):
    """Prototype for water flow sensors."""
    
    def __init__(self, sensor_id: str, min_flow: float = 0.0, max_flow: float = 100.0):
        self._sensor_id = sensor_id
        self._min_flow = min_flow
        self._max_flow = max_flow
        self._sensor_type = "water"
    
    def clone(self):
        return copy.deepcopy(self)
    
    def get_sensor_id(self):
        return self._sensor_id
    
    def get_sensor_type(self):
        return self._sensor_type
    
    def get_min_flow(self):
        return self._min_flow
    
    def get_max_flow(self):
        return self._max_flow


class SensorCache:
    """Cache for storing and cloning prototype sensors."""
    
    def __init__(self):
        self._prototypes: Dict[str, SensorPrototype] = {}
    
    def add_prototype(self, key: str, prototype: SensorPrototype):
        """Add a prototype to the cache."""
        self._prototypes[key] = prototype
    
    def get_clone(self, key: str) -> SensorPrototype:
        """Get a clone of the prototype."""
        prototype = self._prototypes.get(key)
        if not prototype:
            raise ValueError(f"No prototype found for key: {key}")
        return prototype.clone()


# Example usage
if __name__ == "__main__":
    cache = SensorCache()
    
    # Create and cache prototypes
    temp_prototype = TemperatureSensorPrototype("temp_1", 18, 25)
    humidity_prototype = HumiditySensorPrototype("hum_1", 30, 70)
    water_prototype = WaterFlowSensorPrototype("water_1", 0, 100)
    
    cache.add_prototype("temperature", temp_prototype)
    cache.add_prototype("humidity", humidity_prototype)
    cache.add_prototype("water", water_prototype)
    
    # Clone sensors
    clone1 = cache.get_clone("temperature")
    clone2 = cache.get_clone("temperature")
    clone3 = cache.get_clone("humidity")
    
    print(f"Original temp: {temp_prototype.get_sensor_id()}")
    print(f"Clone 1 temp: {clone1.get_sensor_id()}")
    print(f"Clone 2 temp: {clone2.get_sensor_id()}")
    print(f"Clone humidity: {clone3.get_sensor_id()}")
    
    # Verify clones are independent
    clone1._sensor_id = "cloned_temp_1"
    print(f"\nAfter modifying clone1: {clone1.get_sensor_id()}")
    print(f"Original unchanged: {temp_prototype.get_sensor_id()}")