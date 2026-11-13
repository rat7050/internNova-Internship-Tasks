"""
Using a NumPy array:

Access specific elements using indexing.
Extract a portion of the array using slicing.
Create a two-dimensional array.
Access specific rows and columns.
Reshape an array into different dimensions.
Display the original and reshaped arrays.
"""

import numpy as np

# Creating an array
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Accessing individual elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("\nSelected Elements:", numbers[1:5])

# Reshaping the array into 2 rows and 4 columns
matrix = numbers.reshape(2, 4)

print("\nReshaped Array:")
print(matrix)

# Accessing an element from the 2D array
print("\nElement at Row 1, Column 2:", matrix[0, 1])