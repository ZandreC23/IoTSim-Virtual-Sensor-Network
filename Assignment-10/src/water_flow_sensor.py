"""
Water Flow Sensor Class
Simulates water flow data with occasional spikes (every 10-20 readings).
"""

import random
from datetime import datetime
from src.sensor import Sensor


class WaterFlowSensor(Sensor):
    """Water flow sensor with baseline flow and occasional usage spikes."""
    
    def __init__(self, sensor_id: str, min_flow: float = 0.0, max_flow: float = 100.0):
        super().__init__(sensor_id, "water")
        self._min_flow = min_flow
        self._max_flow = max_flow
        self._spike_counter = 0
        self._spike_threshold = random.randint(10, 20)
        self._deterministic_mode = False
        self._fixed_seed = 42
    
    def set_deterministic_mode(self, enabled: bool) -> None:
        """Enable or disable deterministic mode for repeatable tests."""
        self._deterministic_mode = enabled
        if enabled:
            random.seed(self._fixed_seed)
            self._spike_threshold = 15
    
    def generate_reading(self) -> float:
        """Generate water flow reading (baseline or spike)."""
        if not self._is_enabled:
            raise RuntimeError(f"Sensor {self._sensor_id} is disabled.")
        
        # Check if spike should occur
        if self._spike_counter >= self._spike_threshold:
            # Generate spike value (50-100 L/min)
            value = random.uniform(50.0, self._max_flow)
            self._spike_counter = 0
            if not self._deterministic_mode:
                self._spike_threshold = random.randint(10, 20)
            else:
                self._spike_threshold = 15
        else:
            # Generate baseline value (0-20 L/min)
            value = random.uniform(self._min_flow, 20.0)
            self._spike_counter += 1
        
        self._current_value = value
        self._last_update = datetime.now()
        
        return value
    
    def should_spike(self) -> bool:
        """Check if spike counter reached threshold."""
        return self._spike_counter >= self._spike_threshold
    
    def reset_spike_counter(self) -> None:
        """Reset the spike counter after a spike occurs."""
        self._spike_counter = 0
        if not self._deterministic_mode:
            self._spike_threshold = random.randint(10, 20)
    
    def get_min_flow(self) -> float:
        return self._min_flow
    
    def get_max_flow(self) -> float:
        return self._max_flow