"""
William Geary
Student Loan Planner
2 May 2025
--------------------------------------------------------------------------------
loan_calculator
"""

# Import modules
import json

from actions.payments.types.payment_type import PaymentType
from loans.loan_factory import LoanFactory


# Initialize constants
LOAN_FILE = "student_loans.json"
PAYMENT_FILE = "loan_payments.json"


def parse_loans(loan_json):
    """ Parse the user's loans from a JSON file """
    with open(loan_json, "r") as file:
        data = json.load(file)
        loan_objects = data.get("loans", [])

    if len(loan_objects) == 0:
        raise Exception(f"No loans found in {loan_json}")
    else:
        return [LoanFactory.get_loan_from_json(loan_object) for loan_object in loan_objects]


def parse_payments(payment_json):
    """ Parse the user's payments from a JSON file """
    with open(payment_json, "r") as file:
        data = json.load(file)
        payment_objects = data.get("payments", [])

    if len(payment_objects) == 0:
        raise Exception(f"No payments found in {payment_json}")
    else:
        return payment_objects


def main():

    # Initialize student loans
    loans = parse_loans(LOAN_FILE)
    payments = parse_payments(PAYMENT_FILE)

    print("Expected monthly payment:", loans[0].expected_monthly_payment())
    print("Grace period days remaining:", loans[0].grace_period_remaining())

    loans[0].make_payment(amount=120.00, payment_type=PaymentType.SCHEDULED)
    loans[0].make_payment(amount=300.00, payment_type=PaymentType.SCHEDULED)

    print(loans[0].current_monthly_payment())

    # TODO: DETERMINE STRUCTURE OF PAYMENTS (OBJECTS?)
    # TODO: Fix PaymentFactory after determining base Payment class parameters
    # TODO: TYPEHINTING FOR DATES, USE DATES RATHER THAN DATETIMES

    # TODO: Create a payment schedule for a loan, make sure the schedule is updated based on the payments that
    # TODO: user makes, including extra payments, which will reduce the amount of the future payments


if __name__ == "__main__":
    main()