"""mock test for my_calendar"""
import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()

def is_weekday():
    """
    return true if weekday, false if not
    """
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5

# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert is_weekday()
