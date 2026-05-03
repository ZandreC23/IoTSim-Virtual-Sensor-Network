"""
Singleton Pattern
Ensure only one instance of a class exists globally.
"""

import threading


class ConfigurationManager:
    """
    Singleton class for managing configuration.
    Thread-safe implementation with double-checked locking.
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Thread-safe singleton creation."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize the singleton instance only once."""
        if self._initialized:
            return
        
        self._config = {
            "update_frequency": 5,
            "temperature_range": (18.0, 25.0),
            "humidity_range": (30.0, 70.0),
            "water_flow_range": (0.0, 100.0),
            "deterministic_mode": False
        }
        self._initialized = True
    
    def get_config(self, key: str):
        """Get a configuration value."""
        return self._config.get(key)
    
    def set_config(self, key: str, value):
        """Set a configuration value."""
        self._config[key] = value
    
    def get_all_config(self) -> dict:
        """Get all configuration as a dictionary."""
        return self._config.copy()


class DatabaseConnection:
    """
    Singleton for database connections (demonstration).
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
        return cls._instance
    
    def connect(self, connection_string: str) -> bool:
        """Simulate database connection."""
        if not self._connected:
            print(f"Connecting to: {connection_string}")
            self._connected = True
            self._connection_string = connection_string
        return True
    
    def disconnect(self) -> None:
        """Simulate disconnection."""
        if self._connected:
            print(f"Disconnecting from: {self._connection_string}")
            self._connected = False
    
    def is_connected(self) -> bool:
        return self._connected


# Example usage
if __name__ == "__main__":
    # Test ConfigurationManager Singleton
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    
    print(f"config1 is config2: {config1 is config2}")
    
    config1.set_config("update_frequency", 10)
    print(f"config2 sees update_frequency: {config2.get_config('update_frequency')}")
    
    # Test DatabaseConnection Singleton
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 is db2: {db1 is db2}")
    
    db1.connect("localhost:5432")
    print(f"db2 is connected: {db2.is_connected()}")