# match_case_calculator.py
# Simple calculator using match-case (Python 3.10+)

def get_number(prompt):
    """Prompt until the user enters a valid number (float)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = input("Choose the operation (+, -, *, /): ").strip()

    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation selected. Please choose one of +, -, *, /.")

if __name__ == "__main__":
    main()
