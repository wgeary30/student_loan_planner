"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
loan
"""

# Import modules
import math

from abc import ABC, abstractmethod
from datetime import datetime, date
from events.loan_event import LoanEvent
from events.types.payment_event import PaymentEvent
from loans.state import LoanState, LoanConfig
from payments.payment import Payment
from payments.payment_factory import PaymentFactory
from payments.types.payment_type import PaymentType
from typing import List


# Loan class
class Loan(ABC):

    def __init__(self, config: LoanConfig, state: LoanState=None) -> None:
        self.loan_config = config
        self.loan_state = state if state else LoanState(
            current_date=datetime.now().date(),
            principal_balance=self.loan_config.original_principal
        )

    def __str__(self) -> str:
        remaining_balance = self.remaining_balance()

        if remaining_balance == 0:
            return (f"{self.__class__.__name__} - Paid Off "
                    f"(${self.principal:,.2f} originally, {self.interest_rate * 100:.2f}% for "
                    f"{math.ceil(self.term_months / 12)} years)")
        else:
            return (f"{self.__class__.__name__} - ${self.principal:,.2f} "
                    f"({self.interest_rate * 100:.2f}% for {math.ceil(self.term_months / 12)} years, "
                    f"currently: ${remaining_balance:,.2f})")

    # Properties
    @property
    def principal(self) -> float:
        return self.loan_state.principal_balance

    @property
    def interest_rate(self) -> float:
        return self.loan_config.interest_rate

    @property
    def term_months(self) -> int:
        return self.loan_config.term_months

    @property
    def disbursement_date(self) -> date:
        return self.loan_config.disbursement_date

    @property
    def graduation_date(self) -> date:
        return self.loan_config.graduation_date

    @property
    def loan_history(self) -> List[LoanEvent]:
        return self.loan_state.loan_history

    # Inherited public methods
    def is_in_grace_period(self, current_date: date=None) -> bool:
        """ Check if the loan is in the grace period """
        current_date = current_date or datetime.now().date()
        grace_start, grace_end = self.grace_period_range()
        return grace_start <= current_date <= grace_end

    def grace_period_remaining(self, current_date: date=None) -> int:
        """ Determine the number of days remaining in the grace period """
        current_date = current_date or datetime.now().date()
        _, grace_end = self.grace_period_range()
        grace_days = (grace_end - current_date).days
        return max(grace_days, 0)

    def make_payment(self, amount: float, current_date: date=None,
                     payment_type: PaymentType=PaymentType.SCHEDULED) -> None:
        """ Add a user payment to payments """
        current_date = current_date or datetime.now().date()
        payment = PaymentFactory.get_payment(payment_type, amount, current_date)
        self.apply_payment(payment)

    def apply_payment(self, payment: Payment) -> None:
        """ Apply a payment to the loan """
        payment.apply_to(self)
        # TODO: Handle event (figure out how to handle events)
        # self.payments.append(payment)

    def total_paid(self, current_date: date=None) -> float:
        """ Return the total amount paid by a certain date """
        current_date = current_date or datetime.now().date()
        return self._paid_as_of(current_date)

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
    def current_monthly_payment(self):
        # Loan-specific actual monthly payment logic
        pass

    @abstractmethod
    def remaining_balance(self):
        # Loan-specific current total logic
        pass

    @abstractmethod
    def apply_relief(self, relief_policy):
        # Loan-specific relief logic
        pass

    # Inherited helper methods
    def _paid_as_of(self, current_date: date=None) -> float:
        """ Determine the total amount paid by a current date """
        current_date = current_date or datetime.now().date()
        return sum([event.amount_paid for event in self.loan_history if isinstance(event, PaymentEvent) and
                    event.timestamp.date() <= current_date])

    def _add_to_history(self):
        """ Add an event to the loan history """
        # TODO: Determine how to add to loan history
        self.loan_history.append()
        pass