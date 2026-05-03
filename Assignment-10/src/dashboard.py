"""
Dashboard Class
Visualizes sensor data in real-time.
"""

from typing import List
from src.csv_storage import CSVStorage
from src.sensor_reading import SensorReading


class Dashboard:
    """Dashboard for displaying real-time sensor data."""
    
    def __init__(self, csv_storage: CSVStorage):
        """
        Initialize the dashboard.
        
        Args:
            csv_storage: CSVStorage instance to read data from
        """
        self._refresh_interval = 2  # seconds
        self._data_window = 300  # last 5 minutes of data
        self._csv_storage = csv_storage
        self._is_running = False
        self._current_data: List[SensorReading] = []
    
    def load_data(self) -> List[SensorReading]:
        """
        Load data from CSV storage.
        
        Returns:
            List[SensorReading]: All readings from storage
        """
        self._current_data = self._csv_storage.read_all_readings()
        return self._current_data
    
    def update_charts(self) -> None:
        """
        Update temperature, humidity, and water flow charts.
        Simulates chart updates by processing current data.
        """
        if not self._current_data:
            return
        
        temperature_readings = [r for r in self._current_data if r.get_sensor_type() == "temperature"]
        humidity_readings = [r for r in self._current_data if r.get_sensor_type() == "humidity"]
        water_readings = [r for r in self._current_data if r.get_sensor_type() == "water"]
        
        # In a real implementation, these would update UI charts
        # Here we just simulate the update
        self._latest_temperature = temperature_readings[-1].get_value() if temperature_readings else None
        self._latest_humidity = humidity_readings[-1].get_value() if humidity_readings else None
        self._latest_water_flow = water_readings[-1].get_value() if water_readings else None
    
    def update_current_values(self) -> dict:
        """
        Get the latest current values from each sensor type.
        
        Returns:
            dict: Dictionary with current values for each sensor type
        """
        return {
            "temperature": self._latest_temperature if hasattr(self, '_latest_temperature') else None,
            "humidity": self._latest_humidity if hasattr(self, '_latest_humidity') else None,
            "water_flow": self._latest_water_flow if hasattr(self, '_latest_water_flow') else None
        }
    
    def auto_refresh(self) -> None:
        """Simulate auto-refresh by reloading data and updating charts."""
        self.load_data()
        self.update_charts()
    
    def start(self) -> None:
        """Start the dashboard."""
        self._is_running = True
        self.auto_refresh()
    
    def stop(self) -> None:
        """Stop the dashboard."""
        self._is_running = False
    
    def get_refresh_interval(self) -> int:
        return self._refresh_interval
    
    def is_running(self) -> bool:
        return self._is_running