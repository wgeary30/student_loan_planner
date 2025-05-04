"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
loan_calculator
"""

# Import modules
import json

from loans.loan_factory import LoanFactory

# Initialize constants
LOAN_FILE = "student_loans.json"


def parse_loans(loan_json):
    """ Parse the user's loans from a JSON file """
    with open(loan_json, "r") as file:
        data = json.load(file)
        loan_objects = data.get("loans", [])

    if len(loan_objects) == 0:
        raise Exception(f"No loans found in {loan_json}")
    else:
        loans = []
        for loan_object in loan_objects:
            loans.append(LoanFactory.get_loan_from_json(loan_object))

    return loans


def main():

    # Initialize student loans
    loans = parse_loans(LOAN_FILE)
    for loan in loans:
        print(loan)


if __name__ == "__main__":
    main()