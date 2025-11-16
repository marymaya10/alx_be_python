#!/usr/bin/env python3

def get_number(prompt: str):
    while True:
        s = input(prompt).strip()
        try:
            if '.' in s:
                return float(s)
            return int(s)
        except ValueError:
            print("Please enter a valid number.")

def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    op = input("Choose the operation (+, -, *, /): ").strip()

    match op:
        case "+":
            print(f"The result is {num1 + num2}.")
        case "-":
            print(f"The result is {num1 - num2}.")
        case "*":
            print(f"The result is {num1 * num2}.")
        case "/":
            try:
                print(f"The result is {num1 / num2}.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operation.")

if __name__ == "__main__":
    main()

