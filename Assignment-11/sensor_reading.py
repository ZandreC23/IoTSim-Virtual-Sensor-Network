from datetime import datetime


class SensorReading:
    def __init__(self, reading_id: str, sensor_id: str, sensor_type: str, value: float):
        self._reading_id = reading_id
        self._sensor_id = sensor_id
        self._sensor_type = sensor_type
        self._value = value
        self._timestamp = datetime.now()
        self._is_anomaly = False
    
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