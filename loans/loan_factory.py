"""
William Geary
Student Loan Planner
3 May 2025
--------------------------------------------------------------------------------
loan_factory
"""

# Import modules
from dateutil.parser import parse
from loans.loan_type import LoanType

# LoanFactory class
class LoanFactory:

    # Class methods
    @classmethod
    def get_loan(cls, loan_type, principal, interest_rate, start_date, term_years):
        """ Get a loan object given certain parameters """
        return cls._create_loan(
            loan_type=loan_type,
            principal=principal,
            interest_rate=interest_rate,
            start_date=parse(start_date) if isinstance(start_date, str) else start_date,
            term_years=term_years
        )

    @classmethod
    def get_loan_from_json(cls, json_object):
        """ Get a loan object from a loan JSON object """
        return cls._create_loan(
            loan_type=json_object["type"],
            principal=json_object["principal"],
            interest_rate=json_object["interest_rate"],
            start_date=parse(json_object["start_date"]),
            term_years=json_object["term_years"]
        )

    # Helper methods
    @staticmethod
    def _create_loan(loan_type, principal, interest_rate, start_date, term_years):
        """ Create a loan object """
        loan_class = LoanType.from_string(loan_type).loan_class
        return loan_class(principal, interest_rate, start_date, term_years)