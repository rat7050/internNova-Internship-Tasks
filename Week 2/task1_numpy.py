"""
Create a Python program using NumPy that:

Imports NumPy.
Creates a NumPy array containing at least 10 numbers.
Displays the array.
Displays the array's shape, size, and data type.
Creates a one-dimensional and two-dimensional array.
"""
import numpy as np

# Creating a one-dimensional array
numbers = np.array([12, 18, 25, 30, 36, 42, 48, 55, 63, 70])

print("One-Dimensional Array:")
print(numbers)

print("\nArray Shape:", numbers.shape)
print("Array Size:", numbers.size)
print("Data Type:", numbers.dtype)

# Creating a two-dimensional array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nTwo-Dimensional Array:")
print(matrix)

print("2D Array Shape:", matrix.shape)