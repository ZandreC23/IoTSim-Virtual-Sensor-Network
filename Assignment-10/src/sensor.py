"""
Sensor Abstract Base Class
Represents the base class for all sensors in the IoTSim system.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class Sensor(ABC):
    """Abstract base class for all sensor types."""
    
    def __init__(self, sensor_id: str, sensor_type: str):
        """
        Initialize a new sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor (e.g., "temp_1")
            sensor_type: Type of sensor (temperature, humidity, water)
        """
        self._sensor_id = sensor_id
        self._sensor_type = sensor_type
        self._is_enabled = True
        self._current_value = 0.0
        self._last_update: Optional[datetime] = None
    
    @abstractmethod
    def generate_reading(self) -> float:
        """
        Generate a new sensor reading.
        Must be implemented by concrete sensor classes.
        
        Returns:
            float: The generated sensor reading value
        """
        pass
    
    def enable(self) -> None:
        """Activate the sensor."""
        self._is_enabled = True
    
    def disable(self) -> None:
        """Deactivate the sensor."""
        self._is_enabled = False
    
    def get_status(self) -> str:
        """
        Get the current sensor status.
        
        Returns:
            str: "Enabled" if sensor is active, "Disabled" otherwise
        """
        return "Enabled" if self._is_enabled else "Disabled"
    
    def get_sensor_id(self) -> str:
        """Return the sensor's unique identifier."""
        return self._sensor_id
    
    def get_sensor_type(self) -> str:
        """Return the sensor type."""
        return self._sensor_type
    
    def get_current_value(self) -> float:
        """Return the most recent reading value."""
        return self._current_value
    
    def get_last_update(self) -> Optional[datetime]:
        """Return the timestamp of the last reading."""
        return self._last_update
    
    def set_current_value(self, value: float) -> None:
        """Set the current value and update timestamp."""
        self._current_value = value
        self._last_update = datetime.now()