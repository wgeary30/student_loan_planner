"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment
"""

# Import modules
from abc import abstractmethod
from actions.loan_action import LoanAction
from datetime import datetime
from events.loan_event import LoanEvent
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from loans.loan import Loan


# Payment class
class Payment(LoanAction):

    def __init__(self, amount_paid: float, timestamp: datetime):
        self.amount_paid = amount_paid
        self.timestamp = timestamp
        self.principal_paid = 0.0
        self.interest_paid = 0.0
        self.fees_paid = 0.0
        self.overpayment = 0.0

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - ${self.amount_paid} ({self.timestamp.date()})"

    @abstractmethod
    def apply_to(self, loan: "Loan") -> "LoanEvent":
        # Payment-specific application logic
        pass

    # Helper methods
    @abstractmethod
    def _create_event(self, loan: "Loan") -> "LoanEvent":
        # Payment-specific event creation logic
        pass