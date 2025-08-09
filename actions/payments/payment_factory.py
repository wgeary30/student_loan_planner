"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment_factory
"""

# Import modules
from dateutil.parser import parse

from actions.payments.types.extra_payment import ExtraPayment
from actions.payments.types.payment_type import PaymentType
from actions.payments.types.rehabilitation_payment import RehabilitationPayment
from actions.payments.types.scheduled_payment import ScheduledPayment
from actions.payments.types.settlement_payment import SettlementPayment
from utils import to_date


# PaymentFactory class
class PaymentFactory:

    # Class variables
    _payment_type_to_class = {
        PaymentType.SCHEDULED: ScheduledPayment,
        PaymentType.EXTRA: ExtraPayment,
        PaymentType.SETTLEMENT: SettlementPayment,
        PaymentType.REHABILITATION: RehabilitationPayment
    }

    # Class methods
    @classmethod
    def get_payment(cls, payment_type, amount, payment_date):
        """ Get a payment object given certain parameters """
        return cls._create_payment(
            payment_type=payment_type,
            amount=amount,
            payment_date=to_date(payment_date)
        )

    @classmethod
    def get_payment_from_json(cls, json_object):
        """ Get a payment object from a payment JSON object """
        return cls._create_payment(
            payment_type=json_object["type"],
            amount=json_object["amount"],
            payment_date=parse(json_object["payment_date"])
        )

    # Helper methods
    @classmethod
    def _create_payment(cls, payment_type, amount, payment_date):
        """ Create a payment object """
        payment_type = payment_type if isinstance(payment_type, PaymentType) else PaymentType.from_string(payment_type)
        payment_class = cls._payment_type_to_class[payment_type]
        return payment_class(amount, payment_date)