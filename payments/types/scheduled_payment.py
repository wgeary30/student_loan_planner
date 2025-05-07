"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
scheduled_payment
"""

# Import modules
from payments.payment import Payment
from typing import TYPE_CHECKING

# Avoid circular imports
if TYPE_CHECKING:
    from loans.loan import Loan

# ScheduledPayment class
class ScheduledPayment(Payment):

    def apply_to(self, loan: "Loan"):
        """ Apply a payment to a loan object """
        # TODO: Apply the payment to a loan
        print("test")