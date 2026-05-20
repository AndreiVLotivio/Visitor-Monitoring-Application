from interfaces import IMonitoringStrategy
from models import LogEntry


class DurationCalculator(IMonitoringStrategy):
    def calculate_duration(self, entry: LogEntry) -> str:
        if not entry.check_in_time or not entry.check_out_time:
            return "N/A"

        delta = entry.check_out_time - entry.check_in_time
        total_seconds = int(delta.total_seconds())

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        return f"{hours}h {minutes}m"