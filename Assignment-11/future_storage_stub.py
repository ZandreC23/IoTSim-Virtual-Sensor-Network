"""
Future Storage Stub - Placeholder for future database/file storage implementation.
This demonstrates how the system can be extended with new storage backends.
"""

from typing import List, Optional
from datetime import datetime
from repositories.sensor_reading_repository import SensorReadingRepository
from repositories.configuration_repository import ConfigurationRepository
from sensor_reading import SensorReading
from configuration import Configuration


class FileSystemSensorReadingRepository(SensorReadingRepository):
    """
    STUB: Future implementation for JSON file storage.
    
    To implement:
    1. Load all readings from JSON file on init
    2. Save to JSON file on each write operation
    3. Handle file locking for concurrent access
    """
    
    def __init__(self, file_path: str = "sensor_readings.json"):
        self._file_path = file_path
        self._storage: dict[str, SensorReading] = {}
        # TODO: Load from file
        # with open(self._file_path, 'r') as f:
        #     data = json.load(f)
    
    def save(self, entity: SensorReading) -> None:
        # TODO: Save to file
        pass
    
    def find_by_id(self, id: str) -> Optional[SensorReading]:
        # TODO: Read from file
        pass
    
    def find_all(self) -> List[SensorReading]:
        # TODO: Read all from file
        pass
    
    def delete(self, id: str) -> None:
        # TODO: Delete from file
        pass
    
    def exists(self, id: str) -> bool:
        # TODO: Check existence
        pass
    
    def count(self) -> int:
        # TODO: Return count
        pass
    
    # Entity-specific methods
    def find_by_sensor_id(self, sensor_id: str) -> List[SensorReading]:
        pass
    
    def find_by_sensor_type(self, sensor_type: str) -> List[SensorReading]:
        pass
    
    def find_by_timerange(self, start_time: datetime, end_time: datetime) -> List[SensorReading]:
        pass
    
    def find_anomalies(self) -> List[SensorReading]:
        pass


class DatabaseSensorReadingRepository(SensorReadingRepository):
    """
    STUB: Future implementation for SQL/NoSQL database storage.
    
    To implement:
    1. Connect to database (MySQL, PostgreSQL, MongoDB)
    2. Execute SQL queries for CRUD operations
    3. Handle connection pooling and transactions
    """
    
    def __init__(self, connection_string: str = "mysql://localhost:3306/sensors"):
        self._connection_string = connection_string
        # TODO: Establish database connection
        # import mysql.connector
        # self._conn = mysql.connector.connect(...)
    
    def save(self, entity: SensorReading) -> None:
        # TODO: INSERT or UPDATE in database
        # cursor.execute("INSERT INTO readings VALUES (%s, %s, %s, %s)", ...)
        pass
    
    def find_by_id(self, id: str) -> Optional[SensorReading]:
        # TODO: SELECT from database
        pass
    
    def find_all(self) -> List[SensorReading]:
        # TODO: SELECT all from database
        pass
    
    def delete(self, id: str) -> None:
        # TODO: DELETE from database
        pass
    
    def exists(self, id: str) -> bool:
        # TODO: Check existence in database
        pass
    
    def count(self) -> int:
        # TODO: SELECT COUNT from database
        pass
    
    def find_by_sensor_id(self, sensor_id: str) -> List[SensorReading]:
        pass
    
    def find_by_sensor_type(self, sensor_type: str) -> List[SensorReading]:
        pass
    
    def find_by_timerange(self, start_time: datetime, end_time: datetime) -> List[SensorReading]:
        pass
    
    def find_anomalies(self) -> List[SensorReading]:
        pass


# Future storage types can be added by:
# 1. Creating a new class implementing the repository interface
# 2. Adding a new case in RepositoryFactory
# 3. No changes needed to existing code (Open/Closed Principle)