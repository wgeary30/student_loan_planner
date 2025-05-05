"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
loan
"""

# Import modules
from abc import ABC, abstractmethod
from datetime import datetime

# Loan class
class Loan(ABC):

    def __init__(self, principal, interest_rate, start_date, graduation_date, term_years):
        self.principal = principal
        self.interest_rate = interest_rate / 100
        self.start_date = start_date
        self.graduation_date = graduation_date
        self.term_years = term_years
        self.payments = []

    def __str__(self):
        remaining_balance = self.remaining_balance()

        if remaining_balance == 0:
            return (f"{self.__class__.__name__} - Paid Off "
                    f"(${self.principal:,.2f} originally, {self.interest_rate * 100:.2f}% for {self.term_years} years)")
        else:
            return (f"{self.__class__.__name__} - ${self.principal:,.2f} "
                    f"({self.interest_rate * 100:.2f}% for {self.term_years} years, "
                    f"currently: ${remaining_balance:,.2f})")

    # Inherited methods
    def is_in_grace_period(self, current_date):
        """ Check if the loan is in the grace period """
        grace_start, grace_end = self.grace_period_range()
        return grace_start <= current_date <= grace_end

    def grace_period_remaining(self, current_date=datetime.now()):
        """ Determine the number of days remaining in the grace period """
        _, grace_end = self.grace_period_range()
        grace_days = (grace_end - current_date).days
        return max(grace_days, 0)

    def make_payment(self, amount, date=datetime.now().date(), payment_type="standard_payment"):
        """ Add a user payment to payments """
        # TODO: Use the PaymentFactory
        payment = Payment(amount, date)
        self.payments.append(payment)

    # Abstract methods
    @abstractmethod
    def grace_period_range(self):
        # Loan-specific grace period logic
        pass

    @abstractmethod
    def expected_monthly_payment(self):
        # Loan-specific expected monthly payment logic
        pass

    @abstractmethod
    def actual_monthly_payment(self):
        # Loan-specific actual monthly payment logic
        pass

    @abstractmethod
    def remaining_balance(self):
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

    # Helper methods
    def _paid_as_of(self, date=datetime.now().date()):
        # TODO: DETERMINE STRUCTURE OF PAYMENTS WHEN APPENDED, WHAT INFORMATION DO I NEED?
        """ Determine the total amount paid at a current date """
        return sum([a for d, a in self.payments if d <= date])