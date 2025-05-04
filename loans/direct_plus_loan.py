"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_plus_loan
"""

# Import modules
from loans.loan import Loan

# DirectSubsidizedLoan class
class DirectPlusLoan(Loan):

    def monthly_payment(self):
        pass

    def current_total(self):
        return self.principal  # TODO: Correct logic, only here for loan __str__ method

    def total_paid(self):
        pass

    def apply_relief(self, relief_policy):
        pass