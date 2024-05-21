def calculate_interest_loan():
    interest_rates = {
        1: 0.10,  # Housing
        2: 0.11,  # Personal
        3: 0.06,  # Educational
        4: 0.15   # Vehicle Leasing
    }

    # Input loan details
    loan_amount = float(input("Enter loan amount: "))
    loan_period_months = int(input("Enter loan period in months: "))
    loan_type = int(input("Enter type of loan (1: Housing, 2: Personal, 3: Educational, 4: Vehicle Leasing): "))

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rates.get(loan_type)
    if monthly_interest_rate is None:
        print("Invalid loan type!")
        return

    # Calculate monthly interest amount
    monthly_interest_amount = loan_amount * monthly_interest_rate

    # Calculate monthly installment (including interest and principal)
    monthly_installment = (loan_amount + monthly_interest_amount) / loan_period_months

    # Display results
    print("\nLoan Details:")
    print("Loan amount: $", loan_amount)
    print("Loan period (months):", loan_period_months)
    print("Type of loan:", end=" ")
    if loan_type == 1:
        print("Housing")
    elif loan_type == 2:
        print("Personal")
    elif loan_type == 3:
        print("Educational")
    elif loan_type == 4:
        print("Vehicle Leasing")
    print("\nMonthly Interest Amount: RS", monthly_interest_amount)
    print("Monthly Installment: RS", monthly_installment)

calculate_interest_loan()
