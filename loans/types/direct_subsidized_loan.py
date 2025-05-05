"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_subsidized_loan
"""

# Import modules
from dateutil.relativedelta import relativedelta
from loans.loan import Loan

# DirectSubsidizedLoan class
class DirectSubsidizedLoan(Loan):

    # Constants
    GRACE_PERIOD_MONTHS = 6

    def grace_period_range(self):
        """ Determine the start and end date of the grace period """
        grace_start = self.start_date
        grace_end = self.start_date + relativedelta(months=self.GRACE_PERIOD_MONTHS)
        return grace_start, grace_end

    def expected_monthly_payment(self):
        """ Calculate the expected monthly payment over the term of the loan,
        assuming the user does not make payments during the grace period """
        r = self.interest_rate / 12
        n = self.term_years * 12 - self.GRACE_PERIOD_MONTHS
        if r == 0:
            return self.principal / n
        return round((self.principal * r) / (1 - (1 + r) ** -n), 2)

    def actual_monthly_payment(self):
        pass

    def remaining_balance(self):
        return self.principal  # TODO: Correct logic, only here for loan __str__ method

    def total_paid(self):
        pass

    def apply_relief(self, relief_policy):
        pass

