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
    INTEREST_ACCRUAL = "interest_accrual"
    FEE = "fee"
    CAPITALIZATION = "capitalization"
    DEFERMENT = "deferment"
    FORBEARANCE = "forbearance"
    ADJUSTMENT = "adjustment"
    GRADUATION = "graduation"
    TERM_CHANGE = "term_change"