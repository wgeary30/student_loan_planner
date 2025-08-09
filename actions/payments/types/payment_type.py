"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
payment_type
"""

# Import modules
from enum import Enum

# PaymentType class
class PaymentType(Enum):

    SCHEDULED = "Scheduled"
    EXTRA = "Extra"
    SETTLEMENT = "Settlement"
    REHABILITATION = "Rehabilitation"

    # Class methods
    @classmethod
    def from_string(cls, payment_type_str):
        """ Return a payment class from a payment type string """
        normalized = payment_type_str.strip().lower()
        for payment_type in cls:
            if payment_type.value.lower() == normalized:
                return payment_type
        raise ValueError(f"Unrecognized payment type: '{payment_type_str}'")