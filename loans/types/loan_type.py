"""
William Geary
Student Loan Planner
3 May 2025
--------------------------------------------------------------------------------
loan_type
"""

# Import modules
from enum import Enum
from loans.types.direct_plus_loan import DirectPlusLoan
from loans.types.direct_subsidized_loan import DirectSubsidizedLoan
from loans.types.direct_unsubsidized_loan import DirectUnsubsidizedLoan

# LoanType class
class LoanType(Enum):

    DIRECT_SUBSIDIZED = ("Direct Subsidized", DirectSubsidizedLoan)
    DIRECT_UNSUBSIDIZED = ("Direct Unsubsidized", DirectUnsubsidizedLoan)
    DIRECT_PLUS = ("Direct Plus", DirectPlusLoan)

    # Properties
    @property
    def loan_name(self):
        return self.value[0]

    @property
    def loan_class(self):
        return self.value[1]

    # Class methods
    @classmethod
    def from_string(cls, loan_type_str):
        """ Return a loan class from a loan type string """
        normalized = loan_type_str.strip().lower()
        for loan_type in cls:
            if loan_type.loan_name.lower() == normalized:
                return loan_type
        raise ValueError(f"Unrecognized loan type: '{loan_type_str}'")