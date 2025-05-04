"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
loan
"""

# Import modules
from abc import ABC, abstractmethod

# Loan class
class Loan(ABC):

    def __init__(self, principal, interest_rate, start_date, term_years):
        self.principal = principal
        self.interest_rate = interest_rate / 100
        self.start_date = start_date
        self.term_years = term_years

    def __str__(self):
        current_total = self.current_total()

        if current_total == 0:
            return (f"{self.__class__.__name__} - Paid Off "
                    f"(${self.principal:,.2f} originally, {self.interest_rate * 100:.2f}% for {self.term_years} years)")
        else:
            return (f"{self.__class__.__name__} - ${self.principal:,.2f} "
                    f"({self.interest_rate * 100:.2f}% for {self.term_years} years, "
                    f"currently: ${current_total:,.2f})")

    @abstractmethod
    def monthly_payment(self):
        # Loan-specific monthly payment logic
        pass

    @abstractmethod
    def current_total(self):
        # Loan-specific current total logic
        pass

    @abstractmethod
    def total_paid(self):
        # Loan-specific total paid logic
        pass

    @abstractmethod
    def apply_relief(self, relief_policy):
        # Loan-specific relief logic
        pass