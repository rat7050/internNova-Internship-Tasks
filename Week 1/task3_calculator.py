"""Create a calculator program that performs:

Addition
Subtraction
Multiplication
Division
Modulus

using two numbers entered by the user."""

# Taking user input for two numbers
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))

# Performing calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

# Displaying the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

"""Any number can not be divided by zero so we will check 
if the second number is not zero 
before performing division and modulus operations"""

if num2 != 0:
    print("Division:", division)
    print("Modulus:", modulus)
else:
    print("Division is not possible by zero.")
    print("Modulus is not possible by zero.")