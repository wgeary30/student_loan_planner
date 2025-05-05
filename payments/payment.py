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

    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

    @abstractmethod
    def test(self):
        pass
