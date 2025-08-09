"""
William Geary
Student Loan Planner
27 July 2025
--------------------------------------------------------------------------------
utils
"""

# Import modules
from datetime import date, datetime
from dateutil.parser import parse

# Date utils
def to_date(d, dayfirst=False) -> date | None:
    if d is None:
        return None
    if isinstance(d, datetime):
        return d.date()
    if isinstance(d, date):
        return d
    elif isinstance(d, str):
        return parse(d, dayfirst=dayfirst).date()
    else:
        raise TypeError(f"Expected a date, datetime, or str. Received a {type(d)}")

def to_datetime(d, dayfirst=False) -> datetime | None:
    if d is None:
        return None
    if isinstance(d, datetime):
        return d
    if isinstance(d, date):
        return datetime.combine(d, datetime.min.time())
    elif isinstance(d, str):
        return parse(d, dayfirst=dayfirst)
    else:
        raise TypeError(f"Expected a date, datetime, or str. Received a {type(d)}")