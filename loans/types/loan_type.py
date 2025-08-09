"""
William Geary
Student Loan Planner
3 May 2025
--------------------------------------------------------------------------------
loan_type
"""

# Import modules
from enum import Enum

# LoanType class
class LoanType(Enum):

    DIRECT_SUBSIDIZED = "Direct Subsidized"
    DIRECT_UNSUBSIDIZED = "Direct Unsubsidized"
    DIRECT_PLUS = "Direct Plus"

    # Class methods
    @classmethod
    def from_string(cls, loan_type_str):
        """ Return a loan class from a loan type string """
        normalized = loan_type_str.strip().lower()
        for loan_type in cls:
            if loan_type.value.lower() == normalized:
                return loan_type
        raise ValueError(f"Unrecognized loan type: '{loan_type_str}'")