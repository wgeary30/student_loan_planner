"""
William Geary
Student Loan Planner
7 May 2025
--------------------------------------------------------------------------------
loan_event_type
"""

# Import modules
from enum import Enum

# LoanEventType class
class LoanEventType(Enum):

    DISBURSEMENT = "disbursement"
    PAYMENT = "payment"
    INTEREST_ACCRUAL = "interest accrual"
    FEE = "fee"
    CAPITALIZATION = "capitalization"
    DEFERMENT = "deferment"
    FORBEARANCE = "forbearance"
    ADJUSTMENT = "adjustment"
    GRADUATION = "graduation"
    TERM_CHANGE = "term change"

    # Class methods
    @classmethod
    def from_string(cls, loan_event_str: str) -> "LoanEventType":
        """ Return a loan event type from a loan event type string """
        normalized = loan_event_str.strip().lower()
        for loan_event_type in cls:
            if loan_event_type.value.lower() == normalized:
                return loan_event_type
        raise ValueError(f"Unrecognized loan event type: '{loan_event_str}'")