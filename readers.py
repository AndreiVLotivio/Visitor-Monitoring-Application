import csv
from datetime import datetime
from typing import List
from interfaces import ILogReader
from models import LogEntry


class CSVLogReader(ILogReader):
    def read_logs(self, file_path: str) -> List[LogEntry]:
        logs = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entry = LogEntry(row['entry_id'], row['name'], row['purpose'], row['contact'])

                    # Restore State
                    if row['check_in']:
                        entry._check_in_time = datetime.strptime(row['check_in'], '%Y-%m-%d %H:%M:%S')
                    if row['check_out']:
                        entry._check_out_time = datetime.strptime(row['check_out'], '%Y-%m-%d %H:%M:%S')

                    entry._status = row['status']
                    logs.append(entry)
        except FileNotFoundError:
            return []
        return logs