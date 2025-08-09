"""
William Geary
Student Loan Planner
8 May 2025
--------------------------------------------------------------------------------
loan_action
"""

# Import modules
from abc import ABC, abstractmethod
from actions.loan_action_type import LoanActionType
from dataclasses import field
from datetime import datetime
from events.loan_event import LoanEvent
from typing import TYPE_CHECKING

# Avoid circular imports
if TYPE_CHECKING:
    from loans.loan import Loan


# LoanAction class
class LoanAction(ABC):
    action_type: LoanActionType
    timestamp: datetime = field(default_factory=datetime.now)

    @abstractmethod
    def apply_to(self, loan: "Loan") -> "LoanEvent":
        # Action-specific application logic
        pass

    def _create_event(self, loan: "Loan") -> "LoanEvent":
        # Action-specific event logic
        pass