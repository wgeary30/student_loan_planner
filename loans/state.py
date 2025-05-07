"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
state
"""

# Import modules
from dataclasses import dataclass, field
from datetime import date
from loans.compounding_frequency import CompoundingFrequency


# LoanConfig class
@dataclass
class LoanConfig:
    loan_type: str
    original_principal: float
    interest_rate: float
    disbursement_date: date
    term_months: int
    graduation_date: date
    compounding_frequency: CompoundingFrequency

    def __post_init__(self):
        self.interest_rate = self.interest_rate / 100


# LoanState class
@dataclass
class LoanState:
    current_date: date
    principal_balance: float
    last_payment_date: date | None = None
    accrued_interest: float = 0.0
    fees: float = 0.0
    total_paid: float = 0.0
    loan_history: list = field(default_factory=list)