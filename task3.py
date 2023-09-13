

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Initialize variables to store maximum and minimum values
maximum = num1
minimum = num1

# Compare num2 with maximum and minimum
if num2 > maximum:
    maximum = num2
elif num2 < minimum:
    minimum = num2

# Compare num3 with maximum and minimum
if num3 > maximum:
    maximum = num3
elif num3 < minimum:
    minimum = num3

# Print the maximum and minimum values
print("Maximum value:", maximum)
print("Minimum value:", minimum)
