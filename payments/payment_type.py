"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment_type
"""

# Import modules
from enum import Enum
from payments.types.standard_payment import StandardPayment
from payments.types.extra_payment import ExtraPayment

# PaymentType class
class PaymentType(Enum):

    STANDARD = ("Standard", StandardPayment)
    EXTRA = ("Extra", ExtraPayment)

    # Properties
    @property
    def payment_name(self):
        return self.value[0]

    @property
    def payment_class(self):
        return self.value[1]

    # Class methods
    @classmethod
    def from_string(cls, payment_type_str):
        """ Return a payment class from a payment type string """
        normalized = payment_type_str.strip().lower()
        for payment_type in cls:
            if payment_type.payment_name.lower() == normalized:
                return payment_type
        raise ValueError(f"Unrecognized payment type: '{payment_type_str}'")