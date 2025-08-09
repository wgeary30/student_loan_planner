"""
William Geary
Student Loan Planner
8 May 2025
--------------------------------------------------------------------------------
loan_action_type
"""

# Import modules
from enum import Enum

# LoanAction class
class LoanActionType(Enum):

    DISBURSEMENT = "disbursement"
    PAYMENT = "payment"
    INTEREST_ACCRUAL = "interest_accrual"
    FEE = "fee"
    CAPITALIZATION = "capitalization"
    DEFERMENT = "deferment"
    FORBEARANCE = "forbearance"
    ADJUSTMENT = "adjustment"
    GRADUATION = "graduation"
    TERM_CHANGE = "term_change"

    # Class methods
    @classmethod
    def from_string(cls, loan_action_str: str) -> "LoanActionType":
        """ Return a loan action type from a loan action type string """
        normalized = loan_action_str.strip().lower()
        for loan_action_type in cls:
            if loan_action_type.value.lower() == normalized:
                return loan_action_type
        raise ValueError(f"Unrecognized loan action type: '{loan_action_str}'")