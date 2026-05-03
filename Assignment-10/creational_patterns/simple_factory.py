"""
Simple Factory Pattern
Centralized object creation for different sensor types.
"""

from src.temperature_sensor import TemperatureSensor
from src.humidity_sensor import HumiditySensor
from src.water_flow_sensor import WaterFlowSensor
from src.sensor import Sensor


class SensorFactory:
    """Simple factory for creating sensor instances."""
    
    @staticmethod
    def create_sensor(sensor_type: str, sensor_id: str, **kwargs) -> Sensor:
        """
        Create a sensor based on type.
        
        Args:
            sensor_type: Type of sensor ("temperature", "humidity", "water")
            sensor_id: Unique identifier for the sensor
            **kwargs: Additional parameters (min_temp, max_temp, etc.)
            
        Returns:
            Sensor: Instance of the requested sensor type
            
        Raises:
            ValueError: If sensor_type is unknown
        """
        if sensor_type == "temperature":
            min_temp = kwargs.get("min_temp", 18.0)
            max_temp = kwargs.get("max_temp", 25.0)
            return TemperatureSensor(sensor_id, min_temp, max_temp)
        
        elif sensor_type == "humidity":
            min_humidity = kwargs.get("min_humidity", 30.0)
            max_humidity = kwargs.get("max_humidity", 70.0)
            return HumiditySensor(sensor_id, min_humidity, max_humidity)
        
        elif sensor_type == "water":
            min_flow = kwargs.get("min_flow", 0.0)
            max_flow = kwargs.get("max_flow", 100.0)
            return WaterFlowSensor(sensor_id, min_flow, max_flow)
        
        else:
            raise ValueError(f"Unknown sensor type: {sensor_type}")
    
    @staticmethod
    def create_multiple_sensors(sensor_configs: list) -> list:
        """
        Create multiple sensors from a list of configurations.
        
        Args:
            sensor_configs: List of dicts with "type", "id", and optional parameters
            
        Returns:
            list: List of created sensor instances
        """
        sensors = []
        for config in sensor_configs:
            sensor = SensorFactory.create_sensor(
                config["type"],
                config["id"],
                **config.get("params", {})
            )
            sensors.append(sensor)
        return sensors


# Example usage
if __name__ == "__main__":
    temp_sensor = SensorFactory.create_sensor("temperature", "temp_1", min_temp=18, max_temp=25)
    humidity_sensor = SensorFactory.create_sensor("humidity", "hum_1")
    water_sensor = SensorFactory.create_sensor("water", "water_1")
    
    print(f"Created: {temp_sensor.get_sensor_type()} - {temp_sensor.get_sensor_id()}")
    print(f"Created: {humidity_sensor.get_sensor_type()} - {humidity_sensor.get_sensor_id()}")
    print(f"Created: {water_sensor.get_sensor_type()} - {water_sensor.get_sensor_id()}")