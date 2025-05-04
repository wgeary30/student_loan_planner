"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_subsidized_loan
"""

# Import modules
from loans.loan import Loan

# DirectSubsidizedLoan class
class DirectSubsidizedLoan(Loan):

    def monthly_payment(self):
        r = self.interest_rate / 12
        n = self.term_years * 12
        if r == 0:
            return self.principal / n
        return (self.principal * r) / (1 - (1 + r) ** -n)

    def current_total(self):
        return self.principal  # TODO: Correct logic, only here for loan __str__ method

    def total_paid(self):
        pass

    def apply_relief(self, relief_policy):
        pass