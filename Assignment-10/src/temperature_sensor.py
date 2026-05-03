"""
Temperature Sensor Class
Simulates temperature data with daily cycle (warmer during day, cooler at night).
"""

import math
from datetime import datetime
from src.sensor import Sensor


class TemperatureSensor(Sensor):
    """Temperature sensor that follows a daily cycle pattern."""
    
    def __init__(self, sensor_id: str, min_temp: float = 18.0, max_temp: float = 25.0):
        """
        Initialize a temperature sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            min_temp: Minimum temperature value (default 18°C)
            max_temp: Maximum temperature value (default 25°C)
        """
        super().__init__(sensor_id, "temperature")
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._previous_value = (min_temp + max_temp) / 2  # Start at average
    
    def generate_reading(self) -> float:
        """
        Generate temperature reading based on daily cycle.
        Uses sine wave: peak at 2pm (14:00), minimum at 4am (04:00).
        
        Returns:
            float: Temperature value between min_temp and max_temp
        """
        if not self._is_enabled:
            raise RuntimeError(f"Sensor {self._sensor_id} is disabled. Cannot generate reading.")
        
        # Get current hour with decimal for smoother cycle
        now = datetime.now()
        hour = now.hour + now.minute / 60.0
        
        # Sine wave peaks at 14:00 (2pm), troughs at 4:00 (4am)
        # Formula: value = average + amplitude * sin(angle)
        # peak at 14:00 means angle = π/2 at hour = 14
        # period = 24 hours, so angle = π/2 + 2π * (hour - 14) / 24
        
        average = (self._min_temp + self._max_temp) / 2
        amplitude = (self._max_temp - self._min_temp) / 2
        
        # Calculate angle: peak at 14:00 (π/2), trough at 4:00 (3π/2)
        angle = math.pi / 2 + 2 * math.pi * (hour - 14) / 24
        
        value = average + amplitude * math.sin(angle)
        
        # Ensure value stays within bounds
        value = max(self._min_temp, min(self._max_temp, value))
        
        self._current_value = value
        self._last_update = datetime.now()
        self._previous_value = value
        
        return value
    
    def calculate_daily_cycle(self, hour: float) -> float:
        """
        Calculate temperature based on time of day.
        
        Args:
            hour: Time of day in hours (0.0 to 23.99)
            
        Returns:
            float: Expected temperature at that time
        """
        average = (self._min_temp + self._max_temp) / 2
        amplitude = (self._max_temp - self._min_temp) / 2
        angle = math.pi / 2 + 2 * math.pi * (hour - 14) / 24
        return average + amplitude * math.sin(angle)
    
    def validate_reading(self, value: float) -> bool:
        """
        Check if a temperature reading is within valid range.
        
        Args:
            value: Temperature value to validate
            
        Returns:
            bool: True if within min/max range
        """
        return self._min_temp <= value <= self._max_temp
    
    def get_min_temp(self) -> float:
        """Return the minimum temperature value."""
        return self._min_temp
    
    def get_max_temp(self) -> float:
        """Return the maximum temperature value."""
        return self._max_temp