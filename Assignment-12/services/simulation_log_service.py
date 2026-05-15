from typing import List, Optional
from datetime import datetime
import sys
import os

# Clear any cached repositories module to ensure we get the right one
if 'repositories' in sys.modules:
    del sys.modules['repositories']
if 'repositories.simulation_log_repository' in sys.modules:
    del sys.modules['repositories.simulation_log_repository']

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repositories.simulation_log_repository import SimulationLogRepository
from models import SimulationLog


class SimulationLogService:
    def __init__(self, repository: SimulationLogRepository):
        self.repo = repository
    
    def start_simulation(self, log_id: str) -> SimulationLog:
        existing = self.repo.find_by_id(log_id)
        if existing and existing.status == "running":
            raise ValueError("Simulation already running")
        log = SimulationLog(log_id=log_id, start_time=datetime.now(), status="running")
        self.repo.save(log)
        return log
    
    def end_simulation(self, log_id: str) -> SimulationLog:
        log = self.repo.find_by_id(log_id)
        if not log:
            raise ValueError("Simulation log not found")
        if log.status != "running":
            raise ValueError("Simulation already ended")
        log.end_time = datetime.now()
        log.status = "completed"
        self.repo.save(log)
        return log
    
    def get_all_logs(self) -> List[SimulationLog]:
        return self.repo.find_all()
    
    def get_log(self, log_id: str) -> Optional[SimulationLog]:
        return self.repo.find_by_id(log_id)