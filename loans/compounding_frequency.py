"""
William Geary
Student Loan Planner
5 May 2025
--------------------------------------------------------------------------------
compounding_frequency
"""

# Import modules
from enum import Enum

# CompoundingFrequency class
class CompoundingFrequency(Enum):

    DAILY = 365
    WEEKLY = 52
    MONTHLY = 12
    YEARLY = 1

    # Class methods
    @classmethod
    def from_string(cls, comp_freq_str):
        """ Return a compounding frequency from a compounding frequency string """
        normalized = comp_freq_str.strip().lower()
        for comp_freq in cls:
            if comp_freq.name.lower() == normalized:
                return comp_freq
        raise ValueError(f"Unrecognized compounding frequency: '{comp_freq_str}'")