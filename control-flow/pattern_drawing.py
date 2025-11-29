# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: iterate over rows
while row < size:
    # Inner loop: iterate over columns
    for col in range(size):
        print("*", end="")  # print asterisk without newline
    print()  # move to the next line after a row is complete
    row += 1  # increment row counter
