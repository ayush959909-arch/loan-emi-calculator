## MY 1ST PROJECT - Loan EMI + Moratorium Calculator


def get_number(prompt, minimum, inclusive, error_msg):
    """Number maangta rehta hai jab tak valid na mile.
    inclusive=True  -> minimum bhi allowed hai (value >= minimum)
    inclusive=False -> minimum allowed nahi hai (value > minimum)
    """
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Only numbers are allowed")
            continue
        if value > minimum or (inclusive and value == minimum):
            return value
        print(error_msg)


def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower().strip()
        if answer in ("yes", "no"):
            return answer
        print("Only type yes or no")


def ordinal(i):
    """1 -> 1st, 2 -> 2nd, 11 -> 11th, 23 -> 23rd"""
    if i % 100 in (11, 12, 13):
        return f"{i}th"
    return f"{i}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(i % 10, 'th') }"


def print_month(i, emi, total_payment):
    print(f"Your {ordinal(i)} Month EMI is: {emi}")
    remaining = max(0, round(total_payment - emi * i, 2))  # -0.00 na aaye
    print(f"Your Remaining Payment is: {remaining:.2f}")


# ---------------- INPUTS ----------------
Loan_amount = get_number("Enter your loan amount : ", 0, False,
                         "Loan cannot be zero or negative")
Interest = get_number("Kitna percent(%) interest hai (annual, min 0.1) : ", 0.1, True,
                      "Interest cannot be less than 0.1 or negative")
Tenure = get_number("Kitne saal mein loan chuka doge : ", 0, False,
                    "Tenure can't be zero or negative")

# Tenure ko mahino mein badla, ek hi baar, poore program mein yahi use hoga
Tenure_month = max(1, round(Tenure * 12))

Education_loan = get_yes_no("Education loan hai toh yes or no: ")
Subsidy = "no"
Interest_during_course = 0

if Education_loan == "yes":
    Course_period = get_number("Enter Your Course Period Without moratorium : ", 0, False,
                               "Course period cant be zero or negative")
    print("If you didn't get moratorium just type zero")
    Moratorium_period = get_number("Enter moratorium period: ", 0, True,
                                   "Moratorium Period Cannot be Negative(-)")
    Course_period += Moratorium_period

    Subsidy = get_yes_no("Kya CSIS subsidy mili hai?? yes or no : ")
    if Subsidy == "no":
        # Course + moratorium ka interest principal mein jud jaata hai
        Interest_during_course = Loan_amount * Interest * Course_period / 100
        Loan_amount = Loan_amount + Interest_during_course

# ---------------- EMI FORMULA ----------------
# EMI = P * r * (1+r)^n / ((1+r)^n - 1)
r = Interest / 12 / 100  # monthly interest, decimal mein
growth = (1 + r) ** Tenure_month
EMI = round(Loan_amount * r * growth / (growth - 1), 2)

# Loan_amount mein moratorium ka interest pehle se juda hai,
# isliye EMI * months mein wo already included hai (alag se add nahi karna)
Total_Payment = EMI * Tenure_month

# ---------------- RESULTS ----------------
print()
if Education_loan == "yes" and Subsidy == "no":
    print(f"INTEREST DURING MORATORIUM PERIOD : {round(Interest_during_course, 2)}")
print(f"YOUR TOTAL PAYMENT IS : {round(Total_Payment)}")
print(f"YOUR INTEREST DURING LOAN REPAYMENT : {round(Total_Payment - Loan_amount, 2)}")
print(f"YOUR MONTHLY EMI IS : {EMI}")
print(f"YOUR YEARLY EMI IS : {round(EMI * 12, 2)}", "", sep="\n")

# ---------------- MONTH-BY-MONTH ----------------
balance = Loan_amount
for i in range(1, Tenure_month + 1):
    print_month(i, EMI, Total_Payment)
    interest_this_month = balance * r
    principal_this_month = EMI - interest_this_month
    print(f"Your Interest In This Month is: {interest_this_month:.2f}")
    print(f"Your Principal In This Month Is: {principal_this_month:.2f}", "", sep="\n")
    balance -= principal_this_month
