"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
scheduled_payment
"""

# Import modules
from actions.payments.payment import Payment
from actions.payments.types.payment_type import PaymentType
from events.types.payment_event import PaymentEvent
from typing import TYPE_CHECKING

# Avoid circular imports
if TYPE_CHECKING:
    from loans.loan import Loan

# ScheduledPayment class
class ScheduledPayment(Payment):

    def apply_to(self, loan: "Loan") -> "PaymentEvent":
        """ Apply a payment to a loan object """

        remaining = self.amount_paid

        # Pay fees
        self.fees_paid = min(loan.fees, remaining)
        loan.fees -= self.fees_paid
        remaining -= self.fees_paid

        # Pay interest
        self.interest_paid = min(loan.interest, remaining)
        loan.interest -= self.interest_paid
        remaining -= self.interest_paid

        # Pay principal
        self.principal_paid = min(loan.principal, remaining)
        loan.principal -= self.principal_paid
        remaining -= self.principal_paid

        # Excess amount becomes an overpayment
        self.overpayment = max(remaining, 0.0)

        return self._create_event(loan)

    # Helper methods
    def _create_event(self, loan: "Loan") -> "PaymentEvent":
        """ Create a payment event to track when a payment is applied """

        payment_event = PaymentEvent(

            # From payment
            payment_type=PaymentType.SCHEDULED,
            amount_paid=self.amount_paid,
            principal_paid=self.principal_paid,
            interest_paid=self.interest_paid,
            fees_paid=self.fees_paid,

            # From loan
            remaining_balance=loan.fees + loan.interest + loan.principal,
            remaining_principal=loan.principal,
            remaining_interest=loan.interest,
            remaining_fees=loan.fees
        )

        return payment_event