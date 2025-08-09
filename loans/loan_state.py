"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
state
"""

# Import modules
from dataclasses import dataclass, field
from datetime import date, datetime
from events.loan_event import LoanEvent
from events.types.payment_event import PaymentEvent
from loans.compounding_frequency import CompoundingFrequency
from typing import TYPE_CHECKING
from utils import to_date, to_datetime

# Avoid circular imports
if TYPE_CHECKING:
    from loans.types.loan_type import LoanType

# LoanConfig class
@dataclass
class LoanConfig:
    loan_type: "LoanType"
    original_principal: float
    interest_rate: float
    disbursement_date: date
    term_months: int
    graduation_date: date
    compounding_frequency: CompoundingFrequency

    def __post_init__(self):
        self.interest_rate = self.interest_rate / 100


# LoanState class
@dataclass
class LoanState:
    current_date: date
    principal_balance: float
    remaining_balance: float
    last_payment_date: date | None = None
    accrued_interest: float = 0.0
    fees: float = 0.0
    total_paid: float = 0.0
    loan_history: list = field(default_factory=list)

    # Instance methods
    def paid_as_of(self, current_date: date=None) -> float:
        """ Determine the total amount paid by a current date """
        current_date = to_date(current_date) or datetime.now().date()
        return sum([event.amount_paid for event in self.loan_history if isinstance(event, PaymentEvent) and
                    event.timestamp.date() <= current_date])

    def balance_as_of(self, current_date: date=None) -> float:
        """ Determine the total amount due at a current date """
        current_date = to_date(current_date) or datetime.now().date()
        past_events = [e for e in self.loan_history if to_date(e.timestamp) <= current_date]
        remaining_balance = past_events[-1].remaining_balance if len(past_events) > 0 else self.remaining_balance
        return remaining_balance

    def add_event(self, event: LoanEvent):
        """ Add a loan event to loan history """
        self.loan_history.append(event)
        self._order_events()
        # TODO: Update old events (change distribution of payment, etc) if adding an event inbetween

    # Helper methods
    def _order_events(self):
        """ Order the events by timestamp """
        self.loan_history.sort(key=lambda event: event.timestamp)
        self._update_state()

    def _update_state(self):
        """ Update the loan state given current loan history """
        most_recent_event = [e for e in self.loan_history if to_date(e.timestamp) <= datetime.now().date()][-1]

        self.current_date = datetime.now().date()
        self.total_paid = self.paid_as_of(datetime.now())

        self.principal_balance = most_recent_event.remaining_principal
        self.remaining_balance = most_recent_event.remaining_balance
        self.last_payment_date = most_recent_event.timestamp.date()
        self.accrued_interest = most_recent_event.remaining_interest
        self.fees = most_recent_event.remaining_fees