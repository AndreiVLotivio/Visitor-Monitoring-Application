from typing import List
from interfaces import ILogWriter
from models import LogEntry
import csv


class CSVLogWriter(ILogWriter):
    def save_logs(self, logs: List[LogEntry], file_path: str) -> bool:
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                fieldnames = ['entry_id', 'name', 'purpose', 'contact', 'check_in', 'check_out', 'status']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for entry in logs:
                    writer.writerow(entry.to_dict())
            return True
        except Exception as e:
            print(f"Error saving logs: {e}")
            return False