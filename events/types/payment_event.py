"""
William Geary
Student Loan Planner
7 May 2025
--------------------------------------------------------------------------------
payment_event
"""

# Import modules
from dataclasses import dataclass, field
from datetime import datetime

from events.loan_event import LoanEvent
from events.loan_event_type import LoanEventType
from actions.payments.types.payment_type import PaymentType


# PaymentEvent class
@dataclass
class PaymentEvent(LoanEvent):
    payment_type: PaymentType
    amount_paid: float
    principal_paid: float
    interest_paid: float
    fees_paid: float

    def __post_init__(self):
        self.event_type = LoanEventType.PAYMENT

        total_paid = self.principal_paid + self.interest_paid + self.fees_paid
        if not self.amount_paid - total_paid == 0:
            raise ValueError(
                f"amount_paid ({self.amount_paid}) does not equal sum of principal, interest, and fees "
                f"({total_paid})"
            )