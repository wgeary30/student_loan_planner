"""
William Geary
Student Loan Planner
27 July 2025
--------------------------------------------------------------------------------
plan_type
"""

# Import modules
from enum import Enum

# PlanType class
class PlanType(Enum):

    # Fixed Term
    STANDARD = "Standard"
    GRADUATED = "Graduated"
    EXTENDED = "Extended"

    # Income-driven
    SAVE = "SAVE"
    PAYE = "PAYE"
    IBR = "IBR"
    ICR = "ICR"

    # Class methods
    @classmethod
    def from_string(cls, plan_type_str):
        """ Return a plan class from a plan type string """
        normalized = plan_type_str.strip().lower()
        for plan_type in cls:
            if plan_type.value.lower() == normalized:
                return plan_type
        raise ValueError(f"Unrecognized plan type: '{plan_type_str}'")