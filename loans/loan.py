"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
loan
"""

# Import modules
from abc import ABC, abstractmethod
from actions.payments.payment_factory import PaymentFactory
from actions.loan_action import LoanAction
from datetime import datetime, date
from events.loan_event import LoanEvent
from loans.loan_state import LoanState, LoanConfig
from typing import List, TYPE_CHECKING
from utils import to_date

if TYPE_CHECKING:
    from actions.loan_action import LoanAction

# Loan class
class Loan(ABC):

    def __init__(self, config: LoanConfig, state: LoanState=None):
        self.loan_config = config
        self.loan_state = state or LoanState(
            current_date=datetime.now().date(),
            principal_balance=self.loan_config.original_principal,
            remaining_balance=self.loan_config.original_principal
        )

    def __str__(self) -> str:
        remaining_balance = self.remaining_balance()

        if remaining_balance == 0:
            return (f"{self.__class__.__name__} - Paid Off "
                    f"(${self.principal:,.2f} originally, {self.interest_rate * 100:.2f}% for "
                    f"{round(self.term_months / 12)} years)")
        else:
            return (f"{self.__class__.__name__} - ${self.principal:,.2f} "
                    f"({self.interest_rate * 100:.2f}% for {round(self.term_months / 12)} years, "
                    f"currently: ${remaining_balance:,.2f})")

    # Properties
    @property
    def principal(self) -> float:
        return self.loan_state.principal_balance

    @property
    def interest(self) -> float:
        return self.loan_state.accrued_interest

    @property
    def fees(self) -> float:
        return self.loan_state.fees

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

    # Setters
    @principal.setter
    def principal(self, value: float):
        self.loan_state.principal_balance = value

    @interest.setter
    def interest(self, value: float):
        self.loan_state.accrued_interest = value

    @fees.setter
    def fees(self, value: float):
        self.loan_state.fees = value

    # Public methods
    def is_in_grace_period(self, current_date: date=None) -> bool:
        """ Check if the loan is in the grace period """
        current_date = to_date(current_date) or datetime.now().date()
        grace_start, grace_end = self.grace_period_range()
        return grace_start <= current_date <= grace_end

    def grace_period_remaining(self, current_date: date=None) -> int:
        """ Determine the number of days remaining in the grace period """
        current_date = to_date(current_date) or datetime.now().date()
        _, grace_end = self.grace_period_range()
        grace_days = (grace_end - current_date).days
        return max(grace_days, 0)

    def total_paid(self, current_date: date=None) -> float:
        """ Return the total amount paid by a certain date """
        current_date = to_date(current_date) or datetime.now().date()
        return self.loan_state.paid_as_of(current_date)

    def remaining_balance(self, current_date: date=None) -> float:
        """ Return the remaining balance due at a certain date """
        current_date = to_date(current_date) or datetime.now().date()
        return self.loan_state.balance_as_of(current_date)

    # User-facing actions  # TODO: Eventually ma
    def make_payment(self, amount: float, payment_type, payment_date: date=None):
        """ Add a user payment to payments """
        payment_date = to_date(payment_date) or datetime.now().date()
        payment = PaymentFactory.get_payment(payment_type, amount, payment_date)
        self._apply_action(payment)

    # def apply_payment(self, payment: Payment) -> "PaymentEvent":
    #     """ Apply a payment to the loan """
    #     # TODO: Check if payment is correct or an overpayment
    #     # TODO: Handle event (figure out how to handle events)
    #     # TODO: Should I have a general method call to apply an event to the loan or individual methods?

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
    def current_monthly_payment(self, current_date: date=None):
        # Loan-specific actual monthly payment logic
        pass

    @abstractmethod
    def apply_relief(self, relief_policy):
        # Loan-specific relief logic
        pass

    # Internal methods
    def _apply_action(self, action: LoanAction):
        try:
            event = action.apply_to(self)
            self._add_event_to_history(event)
        except NotImplementedError:
            raise NotImplementedError(f"Action type '{type(action).__name__}' is not yet supported.")

    def _add_event_to_history(self, event: LoanEvent):
        """ Add an event to the loan history """
        self.loan_state.add_event(event)