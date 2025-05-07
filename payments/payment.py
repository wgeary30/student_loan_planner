"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment
"""

# Import modules
from abc import ABC, abstractmethod

# Payment class
class Payment(ABC):

    def __init__(self, amount_paid, date):
        self.amount_paid = amount_paid
        self.date = date
        self.principal_paid = 0.0
        self.interest_paid = 0.0
        self.fees_paid = 0.0

    def __str__(self):
        return f"{self.__class__.__name__} - ${self.amount_paid} ({self.date})"

    @abstractmethod
    def test(self):
        # TODO: Determine if there are any methods to be added
        pass
