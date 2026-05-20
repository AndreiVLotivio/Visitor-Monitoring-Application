from typing import List, Optional
from interfaces import ILogReader, ILogWriter, IMonitoringStrategy
from models import LogEntry
from datetime import datetime
import uuid


class MonitoringEngine:
    def __init__(self, reader: ILogReader, writer: ILogWriter, strategy: IMonitoringStrategy):
        self._reader = reader
        self._writer = writer
        self._strategy = strategy

    def get_all_logs(self, file_path: str) -> List[LogEntry]:
        return self._reader.read_logs(file_path)

    def check_in(self, file_path: str, name: str, purpose: str, contact: str) -> LogEntry:
        logs = self.get_all_logs(file_path)

        # Generate unique ID
        entry_id = str(uuid.uuid4())[:8]
        new_entry = LogEntry(entry_id, name, purpose, contact)
        new_entry.check_in(datetime.now())

        logs.insert(0, new_entry)  # Add to top
        self._writer.save_logs(logs, file_path)
        return new_entry

    def check_out(self, file_path: str, entry_id: str) -> Optional[LogEntry]:
        logs = self.get_all_logs(file_path)
        found_entry = None

        for entry in logs:
            if entry.entry_id == entry_id:
                entry.check_out(datetime.now())
                found_entry = entry
                break

        if found_entry:
            self._writer.save_logs(logs, file_path)
        return found_entry

    def get_active_visitors(self, file_path: str) -> List[LogEntry]:
        logs = self.get_all_logs(file_path)
        return [e for e in logs if e.status == "Inside"]

    def get_calculated_duration(self, entry: LogEntry) -> str:
        return self._strategy.calculate_duration(entry)