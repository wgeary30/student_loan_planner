"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment
"""

# Import modules
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

# Avoid circular imports
if TYPE_CHECKING:
    from loans.loan import Loan

# Payment class
class Payment(ABC):

    def __init__(self, amount_paid: float, timestamp: datetime) -> None:
        self.amount_paid = amount_paid
        self.timestamp = timestamp
        self.principal_paid = 0.0
        self.interest_paid = 0.0
        self.fees_paid = 0.0

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - ${self.amount_paid} ({self.timestamp.date()})"

    @abstractmethod
    def apply_to(self, loan: "Loan") -> None:
        # Payment-specific application logic
        pass
