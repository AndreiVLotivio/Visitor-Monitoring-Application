import pytest
from models import LogEntry
from strategies import DurationCalculator
from datetime import datetime, timedelta


# 1. Test Encapsulation / Logic
def test_check_out_validation():
    entry = LogEntry("001", "Alice", "Meeting", "Bob")
    entry.check_in(datetime.now())

    # Should raise error if check_out is before check_in
    past_time = datetime.now() - timedelta(hours=1)
    with pytest.raises(ValueError):
        entry.check_out(past_time)


# 2. Test Duration Strategy
def test_duration_calculation():
    strategy = DurationCalculator()
    entry = LogEntry("002", "Bob", "Work", "HR")

    t_in = datetime(2023, 1, 1, 10, 0, 0)  # 10:00 AM
    t_out = datetime(2023, 1, 1, 12, 30, 0)  # 12:30 PM

    entry.check_in(t_in)
    entry.check_out(t_out)

    duration = strategy.calculate_duration(entry)
    assert duration == "2h 30m"


# 3. Test Status Logic
def test_status_update():
    entry = LogEntry("003", "Charlie", "Inspection", "Admin")
    assert entry.status == "Pre-Registered"

    entry.check_in(datetime.now())
    assert entry.status == "Inside"

    entry.check_out(datetime.now())
    assert entry.status == "Exited"


# 4. Test Double Check-Out Prevention
def test_double_check_out_prevention():
    entry = LogEntry("004", "Diana", "Audit", "Finance")
    entry.check_in(datetime.now())
    entry.check_out(datetime.now())

    # Should raise error when checking out an already-exited visitor
    with pytest.raises(ValueError, match="already checked out"):
        entry.check_out(datetime.now())


# 5. Test Check-In Validation
def test_check_in_updates_status():
    entry = LogEntry("005", "Eve", "Review", "Legal")
    assert entry.status == "Pre-Registered"

    entry.check_in(datetime(2023, 6, 1, 9, 0, 0))
    assert entry.status == "Inside"
    assert entry.check_in_time == datetime(2023, 6, 1, 9, 0, 0)


# 6. Test Duration for Active Visitor (no checkout)
def test_duration_without_checkout():
    strategy = DurationCalculator()
    entry = LogEntry("006", "Frank", "Tour", "Reception")
    entry.check_in(datetime(2023, 1, 1, 10, 0, 0))

    duration = strategy.calculate_duration(entry)
    assert duration == "N/A"