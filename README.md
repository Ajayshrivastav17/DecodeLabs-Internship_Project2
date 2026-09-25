# 💰 Expense Tracker

A simple **command-line Expense Tracker** built with Python.

The program allows users to enter multiple expense amounts, calculates the **total amount spent**, and counts the **number of expenses entered**.

The project also demonstrates basic exception handling using a separate custom exception file.

---

## 🎯 Project Objective

The main objective of this project is to practice fundamental Python concepts such as:

* User input
* Variables
* Data types
* Type conversion
* `while` loops
* `break`
* Conditional statements
* Accumulators
* Counters
* Exception handling
* Custom exceptions
* Python modules

---

# ✨ Features

The Expense Tracker provides the following features:

* Enter multiple expenses
* Automatically calculate total expenses
* Count the number of expenses
* Display numbered input prompts
* Use `done` to stop entering expenses
* Validate expense values
* Reject invalid text input
* Reject negative expenses
* Handle errors without crashing the application
* Use a separate file for custom exceptions
* Display the final expense summary

---

# 📁 Project Structure

```text
expense_tracker/
│
├── main.py
├── expense.py
├── exceptions.py
└── README.md
```

### File Responsibilities

| File            | Responsibility                                    |
| --------------- | ------------------------------------------------- |
| `main.py`       | Runs the application and handles user interaction |
| `expense.py`    | Validates and converts expense values             |
| `exceptions.py` | Contains custom exception classes                 |
| `README.md`     | Project documentation                             |

---

# 🧠 How the Application Works

The application starts with:

```python
total = 0
count = 0
```

`total` stores the total amount of money spent.

`count` stores the number of valid expenses entered.

The application then continuously asks the user for an expense.

```text
[1] Enter the Expense amount : 89
[2] Enter the Expense amount : 56
[3] Enter the Expense amount : 100
[4] Enter the Expense amount : done
```

When the user enters:

```text
done
```

the program stops accepting expenses and displays the final result.

---

# 🔢 Accumulator Logic

The most important calculation in this project is the accumulator:

```python
total = total + expense
```

It can also be written as:

```python
total += expense
```

For example:

```text
Starting total = 0

Expense = 89
0 + 89 = 89

Expense = 56
89 + 56 = 145

Expense = 100
145 + 100 = 245
```

Final total:

```text
₹245
```

---

# 🔢 Counter Logic

The application also keeps track of how many expenses were entered.

```python
count = count + 1
```

For example:

```text
Expense 1 → ₹89
Expense 2 → ₹56
Expense 3 → ₹100
```

Therefore:

```text
Number of Expenses = 3
```

The counter and accumulator have different purposes:

```text
total → calculates money

count → calculates number of expenses
```

---

# 🔄 Why `while True` Is Used

The application does not know how many expenses the user will enter.

The user might enter:

```text
2 expenses
```

or:

```text
10 expenses
```

or:

```text
100 expenses
```

Therefore, a `while True` loop is used:

```python
while True:
```

The loop continues until the user enters:

```text
done
```

The program then uses:

```python
break
```

to exit the loop.

The basic logic is:

```text
START
  ↓
Ask for expense
  ↓
Is input "done"?
  ├── YES → Stop
  │
  └── NO
       ↓
   Validate input
       ↓
   Add to total
       ↓
   Increase count
       ↓
   Ask again
```

---

# 🛡️ Exception Handling

The application validates the expense before adding it to the total.

For example, these inputs are invalid:

```text
abc
hello
₹100
-50
```

The program should not crash when invalid input is provided.

Instead, it displays an appropriate error message.

Example:

```text
[1] Enter the Expense amount : abc

Error: Expense must be a valid number.
```

The user can then enter another value.

---

# ⚠️ Custom Exception

The project uses a separate file called:

```text
exceptions.py
```

It contains the custom exception:

```python
class InvalidExpenseError(Exception):
    """Raised when the expense amount is invalid."""
    pass
```

This allows the application to create a meaningful error specifically for invalid expenses.

---

# 🔧 Expense Validation

The `expense.py` module contains the validation logic.

Example:

```python
from exceptions import InvalidExpenseError


def convert_expense(value):

    try:
        expense = float(value)

    except ValueError:
        raise InvalidExpenseError(
            "Expense must be a valid number."
        )

    if expense < 0:
        raise InvalidExpenseError(
            "Expense cannot be negative."
        )

    return expense
```

The function performs two major checks.

### Check 1 — Is it a number?

```text
100       → Valid
50.50     → Valid
abc       → Invalid
hello     → Invalid
```

### Check 2 — Is it positive?

```text
100       → Valid
50        → Valid
0         → Valid
-100      → Invalid
```

---

# 🖥️ Example Usage

Run the application:

```bash
python main.py
```

Example:

```text
-----------------------------------
       WELCOME TO EXPENSE TRACKER
-----------------------------------

[1] Enter the Expense amount : 89
[2] Enter the Expense amount : 56
[3] Enter the Expense amount : 120
[4] Enter the Expense amount : done

-----------------------------------------
NUMBER OF EXPENSES : 3
TOTAL EXPENSE AMOUNT : ₹265.00
-----------------------------------------
```

---

# ❌ Example of Invalid Input

```text
-----------------------------------
       WELCOME TO EXPENSE TRACKER
-----------------------------------

[1] Enter the Expense amount : 89

[2] Enter the Expense amount : abc
Error: Expense must be a valid number.

[2] Enter the Expense amount : -50
Error: Expense cannot be negative.

[2] Enter the Expense amount : 56

[3] Enter the Expense amount : done

-----------------------------------------
NUMBER OF EXPENSES : 2
TOTAL EXPENSE AMOUNT : ₹145.00
-----------------------------------------
```

Invalid inputs do not get added to the total or expense count.

---

# 📊 Data Flow

The overall application flow is:

```text
User
  │
  ▼
main.py
  │
  │ User enters expense
  ▼
expense.py
  │
  │ Validate input
  ▼
exceptions.py
  │
  │ Raise error if invalid
  ▼
main.py
  │
  ├── Add expense to total
  │
  └── Increase expense count
  │
  ▼
Display Summary
```

---

# 🧩 Core Python Concepts Used

## Variables

```python
total = 0
count = 0
```

---

## Input

```python
expense = input(
    "Enter the Expense amount: "
)
```

---

## Type Conversion

```python
expense = float(expense)
```

`input()` returns text, so `float()` converts it into a number.

---

## Loop

```python
while True:
```

Allows the user to enter an unlimited number of expenses.

---

## Conditional Statement

```python
if expense.lower() == "done":
```

Checks whether the user wants to stop.

---

## Break

```python
break
```

Stops the loop.

---

## Accumulator

```python
total = total + expense
```

Keeps adding expenses together.

---

## Counter

```python
count = count + 1
```

Counts valid expenses.

---

## Exception Handling

```python
try:
    ...
except ValueError:
    ...
```

Prevents invalid input from crashing the application.

---

## Custom Exception

```python
class InvalidExpenseError(Exception):
    pass
```

Creates a specific error type for invalid expenses.

---

# 📦 Requirements

No external libraries are required.

The project uses Python's built-in features.

### Python

Python 3.x is recommended.

Check your Python installation:

```bash
python --version
```

---

# 🚀 How to Run

### 1. Clone or download the project

Navigate to the project directory:

```bash
cd expense_tracker
```

### 2. Run the application

```bash
python main.py
```

### 3. Enter expenses

```text
[1] Enter the Expense amount : 100
[2] Enter the Expense amount : 50
[3] Enter the Expense amount : done
```

---

# 🚫 No External Dependencies

This project intentionally does not use external packages or frameworks.

It uses only Python's standard functionality.

```text
Python
│
├── input()
├── float()
├── while
├── if / else
├── try / except
├── raise
└── custom modules
```

---

# 🎓 Learning Outcomes

After completing this project, the following concepts can be understood:

* How `input()` works
* How strings are converted into numbers
* How loops repeatedly execute code
* How `break` stops a loop
* How accumulators calculate totals
* How counters track quantities
* How exceptions prevent program crashes
* How custom exceptions are created
* How Python files can communicate using imports
* How to separate application logic into multiple files

---

# 🔮 Future Improvements

Possible improvements for future versions:

* Store expenses in a JSON file
* Add expense categories
* Add expense dates
* Display the highest expense
* Display the lowest expense
* Calculate average expense
* Generate monthly expense reports
* Add a search feature
* Add CSV export
* Add a graphical user interface
* Add database storage
* Add unit tests

---

# 📌 Project Purpose

This project was created as a beginner Python project to practice **mathematical operations, accumulators, counters, loops, input validation, exception handling, and modular programming**.

The main concept behind the project is:

```text
NEW EXPENSE
     ↓
VALIDATE
     ↓
ADD TO TOTAL
     ↓
INCREASE COUNT
     ↓
ASK FOR NEXT EXPENSE
     ↓
"done" → DISPLAY RESULT
```

---

# 👨‍💻 Author

**Ajay Deviprasad Shrivastav**

Learning Python programming and progressing toward **AI Engineering and AI Automation**.
