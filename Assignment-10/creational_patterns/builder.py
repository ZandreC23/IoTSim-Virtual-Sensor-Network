"""
Builder Pattern
Construct complex SensorReading objects step by step.
"""

from datetime import datetime
from src.sensor_reading import SensorReading


class SensorReadingBuilder:
    """Builder for creating SensorReading objects with optional fields."""
    
    def __init__(self):
        """Initialize builder with default values."""
        self._reading_id = None
        self._sensor_id = None
        self._sensor_type = None
        self._value = None
        self._timestamp = None
    
    def set_reading_id(self, reading_id: str):
        """Set the reading ID."""
        self._reading_id = reading_id
        return self
    
    def set_sensor_id(self, sensor_id: str):
        """Set the sensor ID."""
        self._sensor_id = sensor_id
        return self
    
    def set_sensor_type(self, sensor_type: str):
        """Set the sensor type."""
        self._sensor_type = sensor_type
        return self
    
    def set_value(self, value: float):
        """Set the reading value."""
        self._value = value
        return self
    
    def set_timestamp(self, timestamp: datetime):
        """Set a custom timestamp."""
        self._timestamp = timestamp
        return self
    
    def build(self) -> SensorReading:
        """
        Build and return the SensorReading object.
        
        Returns:
            SensorReading: Constructed reading object
            
        Raises:
            ValueError: If required fields are missing
        """
        if not self._reading_id:
            raise ValueError("reading_id is required")
        if not self._sensor_id:
            raise ValueError("sensor_id is required")
        if not self._sensor_type:
            raise ValueError("sensor_type is required")
        if self._value is None:
            raise ValueError("value is required")
        
        reading = SensorReading(
            self._reading_id,
            self._sensor_id,
            self._sensor_type,
            self._value
        )
        
        # Override timestamp if custom one was set
        if self._timestamp:
            reading._timestamp = self._timestamp
        
        return reading


class SensorReadingDirector:
    """Director that orchestrates the builder for common reading types."""
    
    def __init__(self, builder: SensorReadingBuilder):
        self._builder = builder
    
    def build_temperature_reading(self, sensor_id: str, value: float) -> SensorReading:
        """Build a standard temperature reading."""
        return (self._builder
                .set_reading_id(f"temp_{sensor_id}")
                .set_sensor_id(sensor_id)
                .set_sensor_type("temperature")
                .set_value(value)
                .build())
    
    def build_humidity_reading(self, sensor_id: str, value: float) -> SensorReading:
        """Build a standard humidity reading."""
        return (self._builder
                .set_reading_id(f"hum_{sensor_id}")
                .set_sensor_id(sensor_id)
                .set_sensor_type("humidity")
                .set_value(value)
                .build())
    
    def build_water_reading(self, sensor_id: str, value: float) -> SensorReading:
        """Build a standard water flow reading."""
        return (self._builder
                .set_reading_id(f"water_{sensor_id}")
                .set_sensor_id(sensor_id)
                .set_sensor_type("water")
                .set_value(value)
                .build())


# Example usage
if __name__ == "__main__":
    builder = SensorReadingBuilder()
    director = SensorReadingDirector(builder)
    
    temp_reading = director.build_temperature_reading("temp_1", 22.5)
    humidity_reading = director.build_humidity_reading("hum_1", 55.0)
    water_reading = director.build_water_reading("water_1", 15.0)
    
    print(f"Temperature reading: {temp_reading.get_value()}°C")
    print(f"Humidity reading: {humidity_reading.get_value()}%")
    print(f"Water flow reading: {water_reading.get_value()} L/min")