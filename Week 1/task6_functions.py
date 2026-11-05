"""Create two user-defined functions:

Function to calculate the square of a number.
Function to calculate the average of three numbers.

Call both functions with user input."""

# Taking user input

n = int(input("Enter a number to calculate square: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Function to calculate square

def square(num):
    return num * num

# Function to calculate average

def average(a, b, c):
    return (a + b + c) / 3

print("Square:", square(n))
print("Average:", average(a, b, c))