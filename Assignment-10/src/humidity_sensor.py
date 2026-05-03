"""
Humidity Sensor Class
Simulates humidity data with random variations (≤5% change per reading).
"""

import random
from src.sensor import Sensor
from datetime import datetime


class HumiditySensor(Sensor):
    """Humidity sensor with realistic random variations."""
    
    def __init__(self, sensor_id: str, min_humidity: float = 30.0, max_humidity: float = 70.0):
        super().__init__(sensor_id, "humidity")
        self._min_humidity = min_humidity
        self._max_humidity = max_humidity
        self._previous_value = (min_humidity + max_humidity) / 2
        self._deterministic_mode = False
        self._fixed_seed = 42
    
    def set_deterministic_mode(self, enabled: bool) -> None:
        """Enable or disable deterministic mode for repeatable tests."""
        self._deterministic_mode = enabled
        if enabled:
            random.seed(self._fixed_seed)
    
    def generate_reading(self) -> float:
        """Generate humidity reading with ≤5% change from previous."""
        if not self._is_enabled:
            raise RuntimeError(f"Sensor {self._sensor_id} is disabled.")
        
        # Generate random value within range
        value = random.uniform(self._min_humidity, self._max_humidity)
        
        # Ensure change is ≤5%
        change = abs(value - self._previous_value)
        if change > 5.0:
            # Regenerate until change is acceptable
            for _ in range(10):
                value = random.uniform(self._min_humidity, self._max_humidity)
                change = abs(value - self._previous_value)
                if change <= 5.0:
                    break
        
        self._current_value = value
        self._last_update = self._last_update  # Keep timestamp
        self._previous_value = value
        
        return value
    
    def validate_change(self, value: float) -> bool:
        """Check if change from previous reading is ≤5%."""
        return abs(value - self._previous_value) <= 5.0
    
    def regenerate_if_needed(self) -> float:
        """Regenerate value if change is too large."""
        value = random.uniform(self._min_humidity, self._max_humidity)
        if self.validate_change(value):
            return value
        return self.regenerate_if_needed()
    
    def get_min_humidity(self) -> float:
        return self._min_humidity
    
    def get_max_humidity(self) -> float:
        return self._max_humidity