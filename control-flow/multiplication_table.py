# multiplication_table.py
# This program asks the user for a number and prints its multiplication table from 1 to 10.

# Prompt the user for input
number_input = input("Enter a number to see its multiplication table: ")

# Validate the input and convert to integer
try:
    number = int(number_input)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    exit()

# Print the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

