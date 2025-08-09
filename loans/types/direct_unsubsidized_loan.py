"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_unsubsidized_loan
"""

# Import modules
from datetime import date
from dateutil.relativedelta import relativedelta
from loans.loan import Loan
from typing import Tuple

from utils import to_date


# DirectUnsubsidizedLoan class
class DirectUnsubsidizedLoan(Loan):

    # Constants
    GRACE_PERIOD_MONTHS = 6

    def grace_period_range(self) -> Tuple[date, date]:
        """ Determine the start and end date of the grace period """
        grace_start = self.graduation_date
        grace_end = self.graduation_date + relativedelta(months=self.GRACE_PERIOD_MONTHS)
        return to_date(grace_start), to_date(grace_end)

    def expected_monthly_payment(self) -> float:
        """ Calculate the expected monthly payment over the term of the loan,
        assuming the user does not make payments during the grace period """
        r = self.interest_rate / 12
        n = self.term_months - self.GRACE_PERIOD_MONTHS
        grace_interest = self.principal * self.interest_rate * (self.GRACE_PERIOD_MONTHS / 12)
        capitalized_principal = self.principal + grace_interest

        if r == 0:
            return round(capitalized_principal / n, 2)
        return round((capitalized_principal * r) / (1 - (1 + r) ** -n), 2)

    def current_monthly_payment(self):
        pass

    def apply_relief(self, relief_policy):
        pass