"""
William Geary
Student Loan Planner
3 May 2025
--------------------------------------------------------------------------------
loan_factory
"""

# Import modules
from datetime import date
from dateutil.parser import parse
from loans.compounding_frequency import CompoundingFrequency
from loans.loan import Loan
from loans.types.loan_type import LoanType
from loans.state import LoanConfig
from typing import Dict, Any


# LoanFactory class
class LoanFactory:

    # Class methods
    @classmethod
    def get_loan(cls, loan_type: LoanType, principal: float, interest_rate: float, disbursement_date: date,
                 graduation_date: date, term_months: int, compounding_frequency: CompoundingFrequency) -> Loan:
        """ Get a loan object given certain parameters """
        config = LoanConfig(
            loan_type=loan_type,
            original_principal=principal,
            interest_rate=interest_rate,
            disbursement_date=parse(disbursement_date) if isinstance(disbursement_date, str) else disbursement_date,
            term_months=term_months,
            graduation_date=parse(graduation_date) if isinstance(graduation_date, str) else graduation_date,
            compounding_frequency=compounding_frequency
        )
        return cls._create_loan(config)

    @classmethod
    def get_loan_from_json(cls, json_object: Dict[str, Any]) -> Loan:
        """ Get a loan object from a loan JSON object """
        config = LoanConfig(
            loan_type=LoanType.from_string(json_object["type"]),
            original_principal=json_object["principal"],
            interest_rate=json_object["interest_rate"],
            disbursement_date=parse(json_object["disbursement_date"]),
            term_months=json_object.get("term_months", json_object.get("term_years", None) * 12),
            graduation_date=parse(json_object["graduation_date"]),
            compounding_frequency=CompoundingFrequency.from_string(json_object["compounding_frequency"])
        )
        return cls._create_loan(config)

    # Helper methods
    @staticmethod
    def _create_loan(config):
        """ Create a loan object """
        loan_class = config.loan_type.loan_class
        return loan_class(config)