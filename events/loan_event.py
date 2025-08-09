"""
William Geary
Student Loan Planner
7 May 2025
--------------------------------------------------------------------------------
loan_event
"""

# Import modules
from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from events.loan_event_type import LoanEventType

# LoanEvent class
@dataclass
class LoanEvent(ABC):
    event_type: LoanEventType = field(init=False)
    remaining_balance: float
    remaining_principal: float
    remaining_interest: float
    remaining_fees: float
    timestamp: datetime = field(default_factory=datetime.now, init=False)