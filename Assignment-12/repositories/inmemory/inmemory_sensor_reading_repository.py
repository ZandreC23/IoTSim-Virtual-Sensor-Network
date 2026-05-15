from typing import List, Optional
from datetime import datetime
from models import SensorReading


class InMemorySensorReadingRepository:
    def __init__(self):
        self._storage: dict[str, SensorReading] = {}

    def save(self, entity: SensorReading) -> None:
        self._storage[entity.reading_id] = entity

    def find_by_id(self, id: str) -> Optional[SensorReading]:
        return self._storage.get(id)

    def find_all(self) -> List[SensorReading]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def exists(self, id: str) -> bool:
        return id in self._storage

    def count(self) -> int:
        return len(self._storage)

    def find_anomalies(self) -> List[SensorReading]:
        return [r for r in self._storage.values() if r.is_anomaly]