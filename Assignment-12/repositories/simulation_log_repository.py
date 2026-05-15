"""
In-memory repository for SimulationLog.
"""

from typing import List, Optional
from models import SimulationLog


class SimulationLogRepository:
    def __init__(self):
        self._storage: dict[str, SimulationLog] = {}
    
    def save(self, log: SimulationLog) -> None:
        self._storage[log.log_id] = log
    
    def find_by_id(self, log_id: str) -> Optional[SimulationLog]:
        return self._storage.get(log_id)
    
    def find_all(self) -> List[SimulationLog]:
        return list(self._storage.values())
    
    def delete(self, log_id: str) -> None:
        if log_id in self._storage:
            del self._storage[log_id]
    
    def exists(self, log_id: str) -> bool:
        return log_id in self._storage
    
    def count(self) -> int:
        return len(self._storage)