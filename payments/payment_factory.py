"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment_factory
"""

# Import modules
from dateutil.parser import parse
from payments.types.payment_type import PaymentType

# PaymentFactory class
class PaymentFactory:

    # Class methods
    @classmethod
    def get_payment(cls, payment_type, amount, payment_date):
        """ Get a payment object given certain parameters """
        return cls._create_payment(
            payment_type=payment_type,
            amount=amount,
            payment_date=parse(payment_date) if isinstance(payment_date, str) else payment_date
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
    @staticmethod
    def _create_payment(payment_type, amount, payment_date):
        """ Create a payment object """
        payment_class = PaymentType.from_string(payment_type).loan_class
        return payment_class(amount, payment_date)