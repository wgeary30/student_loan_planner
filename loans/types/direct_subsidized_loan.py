"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
direct_subsidized_loan
"""

# Import modules
from datetime import date, datetime
from typing import Tuple
from dateutil.relativedelta import relativedelta
from loans.loan import Loan
from utils import to_date


# DirectSubsidizedLoan class
class DirectSubsidizedLoan(Loan):

    # Constants
    GRACE_PERIOD_MONTHS = 6

    # Abstract methods
    def grace_period_range(self) -> Tuple[date, date]:
        """ Determine the start and end date of the grace period """
        grace_start = self.graduation_date
        grace_end = self.graduation_date + relativedelta(months=self.GRACE_PERIOD_MONTHS)
        return to_date(grace_start), to_date(grace_end)

    def expected_monthly_payment(self) -> float:
        """ Calculate the expected monthly payment over the term of the loan,
        assuming the user does not make payments during the grace period """
        p = self.loan_config.original_principal
        r = self.interest_rate / 12
        n = self.term_months - self.GRACE_PERIOD_MONTHS

        if r == 0:
            return p / n
        return round((p * r) / (1 - (1 + r) ** -n), 2)

    def current_monthly_payment(self, current_date: date=None):
        """ Calculate the monthly payment over the term of the loan given
        the current state of the user's payments """

        current_date = to_date(current_date) or datetime.now().date()

        p = self.remaining_balance(current_date=current_date)
        r = self.interest_rate / 12
        n = self.term_months - self.GRACE_PERIOD_MONTHS

        if r == 0:
            return p / n
        return round((p * r) / (1 - (1 + r) ** -n), 2)

    def apply_relief(self, relief_policy):
        pass