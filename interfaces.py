from abc import ABC, abstractmethod
from typing import List
from models import LogEntry

class ILogReader(ABC):
    @abstractmethod
    def read_logs(self, file_path: str) -> List[LogEntry]:
        pass

class ILogWriter(ABC):
    @abstractmethod
    def save_logs(self, logs: List[LogEntry], file_path: str) -> bool:
        pass

class IMonitoringStrategy(ABC):
    @abstractmethod
    def calculate_duration(self, entry: LogEntry) -> str:
        pass