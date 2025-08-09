"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_plus_loan
"""

# Import modules
from datetime import date
from dateutil.relativedelta import relativedelta
from loans.loan import Loan
from typing import Tuple

# DirectSubsidizedLoan class
class DirectPlusLoan(Loan):

    # Constants
    GRACE_PERIOD_MONTHS = 6

    def grace_period_range(self) -> Tuple[date, date]:
        """ Determine the start and end date of the grace period """
        grace_start = self.disbursement_date
        grace_end = self.disbursement_date + relativedelta(months=self.GRACE_PERIOD_MONTHS)
        return grace_start, grace_end

    def expected_monthly_payment(self):
        pass

    def current_monthly_payment(self):
        pass

    def apply_relief(self, relief_policy):
        pass