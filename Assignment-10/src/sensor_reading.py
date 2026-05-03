"""
Sensor Reading Class
Represents a single sensor reading with timestamp and anomaly flag.
"""

from datetime import datetime
from typing import Optional


class SensorReading:
    """Individual sensor reading data point."""
    
    def __init__(self, reading_id: str, sensor_id: str, sensor_type: str, value: float):
        """
        Initialize a sensor reading.
        
        Args:
            reading_id: Unique identifier for this reading
            sensor_id: ID of the sensor that generated this reading
            sensor_type: Type of sensor (temperature, humidity, water)
            value: The reading value
        """
        self._reading_id = reading_id
        self._sensor_id = sensor_id
        self._sensor_type = sensor_type
        self._value = value
        self._timestamp = datetime.now()
        self._is_anomaly = False
    
    def to_csv_row(self) -> str:
        """
        Format reading as CSV string.
        
        Returns:
            str: CSV formatted row: timestamp,sensor_type,sensor_id,value
        """
        timestamp_str = self._timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return f"{timestamp_str},{self._sensor_type},{self._sensor_id},{self._value}"
    
    def validate(self) -> bool:
        """
        Validate the reading based on sensor type.
        
        Returns:
            bool: True if reading is valid
        """
        if self._sensor_type == "temperature":
            return 18.0 <= self._value <= 25.0
        elif self._sensor_type == "humidity":
            return 30.0 <= self._value <= 70.0
        elif self._sensor_type == "water":
            return 0.0 <= self._value <= 100.0
        return False
    
    def flag_anomaly(self) -> None:
        """Mark this reading as an anomaly (out of normal range)."""
        self._is_anomaly = True
    
    def get_reading_id(self) -> str:
        return self._reading_id
    
    def get_sensor_id(self) -> str:
        return self._sensor_id
    
    def get_sensor_type(self) -> str:
        return self._sensor_type
    
    def get_value(self) -> float:
        return self._value
    
    def get_timestamp(self) -> datetime:
        return self._timestamp
    
    def is_anomaly(self) -> bool:
        return self._is_anomaly