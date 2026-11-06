# Loan EMI & Moratorium Calculator

A command-line loan calculator written in Python. It works out your monthly EMI and shows a month-by-month breakdown of interest, principal and remaining payment. It also supports **education loans** with a course period, moratorium period and subsidy option.

This is my first Python project, built as part of my BCA studies.

## Features

- Monthly and yearly EMI calculation using the standard reducing-balance formula
- Total payment and total interest over the loan tenure
- Education loan mode:
  - Course period + moratorium period
  - Interest during moratorium (added to the principal when no subsidy is received)
  - CSIS subsidy option (yes / no)
- Month-by-month schedule: EMI, interest, principal and remaining payment
- Input validation: rejects text, zero and negative values, and asks again

## How it works

EMI is calculated with:

```
EMI = P × r × (1 + r)^n / ((1 + r)^n − 1)
```

- `P` = loan amount (including moratorium interest, if applicable)
- `r` = monthly interest rate (annual rate ÷ 12 ÷ 100)
- `n` = tenure in months

For an education loan without subsidy, the interest accumulated during the course and moratorium period is calculated as simple interest and added to the principal before the EMI is computed.

## Requirements

- Python 3.6 or later
- No external libraries

## Usage

```bash
python emi_calculator.py
```

Then answer the prompts.

## Example

Education loan, no subsidy, no moratorium:

```
Enter your loan amount : 100000
Kitna percent(%) interest hai (annual, min 0.1) : 10
Kitne saal mein loan chuka doge : 2
Education loan hai toh yes or no: yes
Enter Your Course Period Without moratorium : 1
Enter moratorium period: 0
Kya CSIS subsidy mili hai?? yes or no : no

INTEREST DURING MORATORIUM PERIOD : 10000.0
YOUR TOTAL PAYMENT IS : 121823
YOUR INTEREST DURING LOAN REPAYMENT : 11822.56
YOUR MONTHLY EMI IS : 5075.94
YOUR YEARLY EMI IS : 60911.28

Your 1st Month EMI is: 5075.94
Your Remaining Payment is: 116746.62
Your Interest In This Month is: 916.67
Your Principal In This Month Is: 4159.27
...
```

## What I learned

- Taking user input safely with `try` / `except ValueError`
- Writing reusable functions (`get_number`, `get_yes_no`, `ordinal`)
- Turning a financial formula into working code
- Debugging logic errors such as double-counting interest

## Future improvements

- Export the repayment schedule to a CSV file
- Add a simple GUI

## Author

**Ayush** – BCA student, DPG Degree College (MDU Rohtak)
