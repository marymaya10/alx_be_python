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

    if op == "+":
        print(f"The result is {num1 + num2}.")
    elif op == "-":
        print(f"The result is {num1 - num2}.")
    elif op == "*":
        print(f"The result is {num1 * num2}.")
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    else:
        print("Invalid operation. Please choose one of: +, -, *, /")

if __name__ == "__main__":
    main()
