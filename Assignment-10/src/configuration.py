"""
Configuration Class
Manages simulation settings and parameters.
"""

import json
import os
from typing import Dict, Any, List


class Configuration:
    """Manages configuration settings for the simulator."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._config_path = "config.json"
        self._update_frequency = 5
        self._temperature_range = {"min": 18.0, "max": 25.0}
        self._humidity_range = {"min": 30.0, "max": 70.0}
        self._water_flow_range = {"min": 0.0, "max": 100.0}
        self._deterministic_mode = False
        self._enabled_sensors = ["temperature", "humidity", "water"]
        self._initialized = True
    
    def load_config(self) -> None:
        if not os.path.exists(self._config_path):
            self.save_config()
            return
        
        with open(self._config_path, 'r') as f:
            data = json.load(f)
            self._update_frequency = data.get("update_frequency", 5)
            self._temperature_range = data.get("temperature_range", {"min": 18.0, "max": 25.0})
            self._humidity_range = data.get("humidity_range", {"min": 30.0, "max": 70.0})
            self._water_flow_range = data.get("water_flow_range", {"min": 0.0, "max": 100.0})
            self._deterministic_mode = data.get("deterministic_mode", False)
            self._enabled_sensors = data.get("enabled_sensors", ["temperature", "humidity", "water"])
    
    def save_config(self) -> None:
        data = {
            "update_frequency": self._update_frequency,
            "temperature_range": self._temperature_range,
            "humidity_range": self._humidity_range,
            "water_flow_range": self._water_flow_range,
            "deterministic_mode": self._deterministic_mode,
            "enabled_sensors": self._enabled_sensors
        }
        with open(self._config_path, 'w') as f:
            json.dump(data, f, indent=4)
    
    def validate_settings(self) -> bool:
        """Validate that all settings are within acceptable ranges."""
        try:
            if self._update_frequency < 1 or self._update_frequency > 60:
                return False
            if self._temperature_range["min"] >= self._temperature_range["max"]:
                return False
            if self._humidity_range["min"] >= self._humidity_range["max"]:
                return False
            if self._water_flow_range["min"] >= self._water_flow_range["max"]:
                return False
            return True
        except (KeyError, TypeError):
            return False
    
    def apply_settings(self) -> None:
        if self.validate_settings():
            self.save_config()
    
    def get_update_frequency(self) -> int:
        return self._update_frequency
    
    def set_update_frequency(self, value: int) -> None:
        if 1 <= value <= 60:
            self._update_frequency = value
    
    def get_temperature_range(self) -> dict:
        return self._temperature_range.copy()
    
    def get_humidity_range(self) -> dict:
        return self._humidity_range.copy()
    
    def get_water_flow_range(self) -> dict:
        return self._water_flow_range.copy()
    
    def is_deterministic_mode(self) -> bool:
        return self._deterministic_mode
    
    def set_deterministic_mode(self, value: bool) -> None:
        self._deterministic_mode = value
    
    def get_enabled_sensors(self) -> List[str]:
        return self._enabled_sensors.copy()