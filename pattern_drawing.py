# pattern_drawing.py

# Step 1: Ask user for pattern size
size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize row counter
row = 0

# Step 3: Outer loop for rows
while row < size:
    # Inner loop for columns
    for col in range(size):
        print("*", end="")
    # Move to next line after each row
    print()
    row += 1

