"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_unsubsidized_loan
"""

# Import modules
from dateutil.relativedelta import relativedelta
from loans.loan import Loan

# DirectUnsubsidizedLoan class
class DirectUnsubsidizedLoan(Loan):

    GRACE_PERIOD_MONTHS = 6

    def grace_period_range(self):
        """ Determine the start and end date of the grace period """
        grace_start = self.start_date
        grace_end = self.start_date + relativedelta(months=self.GRACE_PERIOD_MONTHS)
        return grace_start, grace_end

    def monthly_payment(self):
        pass

    def current_total(self):
        return self.principal  # TODO: Correct logic, only here for loan __str__ method

    def total_paid(self):
        pass

    def apply_relief(self, relief_policy):
        pass