"""
Perform the following operations using NumPy:

Mathematical Operations
Addition
Subtraction
Multiplication
Division
Statistical Functions
Mean
Median
Minimum
Maximum
Standard Deviation
Sum

Use a numerical dataset of your choice and display the results.
"""

import numpy as np

# Creating two arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([2, 4, 6, 8, 10])

# Performing mathematical operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# basic statistical values
print("\nSum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))