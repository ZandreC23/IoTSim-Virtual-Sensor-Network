"""
Factory Method Pattern
Delegate instantiation to subclasses.
"""

from abc import ABC, abstractmethod
from src.temperature_sensor import TemperatureSensor
from src.humidity_sensor import HumiditySensor
from src.water_flow_sensor import WaterFlowSensor
from src.sensor import Sensor


class SensorCreator(ABC):
    """Abstract creator class with factory method."""
    
    @abstractmethod
    def create_sensor(self, sensor_id: str) -> Sensor:
        """Factory method to create a sensor."""
        pass
    
    def get_sensor_info(self, sensor_id: str) -> dict:
        """Template method that uses the factory method."""
        sensor = self.create_sensor(sensor_id)
        return {
            "id": sensor.get_sensor_id(),
            "type": sensor.get_sensor_type(),
            "status": sensor.get_status()
        }


class TemperatureSensorCreator(SensorCreator):
    """Concrete creator for temperature sensors."""
    
    def __init__(self, min_temp: float = 18.0, max_temp: float = 25.0):
        self._min_temp = min_temp
        self._max_temp = max_temp
    
    def create_sensor(self, sensor_id: str) -> Sensor:
        return TemperatureSensor(sensor_id, self._min_temp, self._max_temp)


class HumiditySensorCreator(SensorCreator):
    """Concrete creator for humidity sensors."""
    
    def __init__(self, min_humidity: float = 30.0, max_humidity: float = 70.0):
        self._min_humidity = min_humidity
        self._max_humidity = max_humidity
    
    def create_sensor(self, sensor_id: str) -> Sensor:
        return HumiditySensor(sensor_id, self._min_humidity, self._max_humidity)


class WaterFlowSensorCreator(SensorCreator):
    """Concrete creator for water flow sensors."""
    
    def __init__(self, min_flow: float = 0.0, max_flow: float = 100.0):
        self._min_flow = min_flow
        self._max_flow = max_flow
    
    def create_sensor(self, sensor_id: str) -> Sensor:
        return WaterFlowSensor(sensor_id, self._min_flow, self._max_flow)


# Example usage
if __name__ == "__main__":
    temp_creator = TemperatureSensorCreator(18, 25)
    humidity_creator = HumiditySensorCreator(30, 70)
    water_creator = WaterFlowSensorCreator(0, 100)
    
    temp_sensor = temp_creator.create_sensor("temp_1")
    humidity_sensor = humidity_creator.create_sensor("hum_1")
    water_sensor = water_creator.create_sensor("water_1")
    
    print(f"Factory Method created: {temp_sensor.get_sensor_id()} ({temp_sensor.get_sensor_type()})")
    print(f"Factory Method created: {humidity_sensor.get_sensor_id()} ({humidity_sensor.get_sensor_type()})")
    print(f"Factory Method created: {water_sensor.get_sensor_id()} ({water_sensor.get_sensor_type()})")