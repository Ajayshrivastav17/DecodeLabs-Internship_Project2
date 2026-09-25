from expceptions import InvalidExpenseError

def convert_expense(value):
    """convert user input into a valid expense amount."""

    try:

        expense=float(value)

    except ValueError:
        raise InvalidExpenseError(
            "Expense must be valid number."
        )

    if expense < 0:
        raise InvalidExpenseError(
            "Expense cannot be negative"
        )

    return expense

