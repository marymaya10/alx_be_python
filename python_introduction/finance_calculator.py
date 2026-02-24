# Finance Calculator
# This script calculates monthly savings and projects annual savings with interest

# Get user input for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% interest
# Formula: (Monthly Savings * 12) + (Monthly Savings * 12 * 0.05)
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display Results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.0f}.")
