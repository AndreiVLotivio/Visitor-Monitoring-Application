from datetime import datetime


class LogEntry:
    def __init__(self, entry_id: str, name: str, purpose: str, contact: str):
        self._entry_id = entry_id
        self._name = name
        self._purpose = purpose
        self._contact = contact
        self._check_in_time: datetime = None
        self._check_out_time: datetime = None
        self._status: str = "Pre-Registered"

    @property
    def entry_id(self):
        return self._entry_id

    @property
    def name(self):
        return self._name

    @property
    def purpose(self):
        return self._purpose

    @property
    def contact(self):
        return self._contact

    @property
    def check_in_time(self):
        return self._check_in_time

    @property
    def check_out_time(self):
        return self._check_out_time

    @property
    def status(self):
        return self._status

    def check_in(self, time: datetime):
        self._check_in_time = time
        self._status = "Inside"

    def check_out(self, time: datetime):
        if self._check_in_time is None:
            raise ValueError("Cannot check out without checking in.")
        if time < self._check_in_time:
            raise ValueError("Check-out time cannot be earlier than check-in time.")

        self._check_out_time = time
        self._status = "Exited"

    def to_dict(self):
        return {
            'entry_id': self._entry_id,
            'name': self._name,
            'purpose': self._purpose,
            'contact': self._contact,
            'check_in': self._check_in_time.strftime('%Y-%m-%d %H:%M:%S') if self._check_in_time else '',
            'check_out': self._check_out_time.strftime('%Y-%m-%d %H:%M:%S') if self._check_out_time else '',
            'status': self._status
        }