"""
Using a Pandas DataFrame:

Select specific columns.
Select specific rows.
Filter records based on a condition.
Apply multiple filtering conditions.
Sort data in ascending order.
Sort data in descending order.

Example: Filter students based on marks, employees based on salary, or products based on price.
"""

import pandas as pd

# Reading employee dataset
df = pd.read_csv("D:\Downloads\internNova Internship Tasks\Week 2\dataset\employee_data.csv")

# Selecting a single column
print("Employee Names:")
print(df["Name"])

# Selecting multiple columns
print("\nEmployee Name and Salary:")
print(df[["Name", "Salary"]])

# Filtering employees with salary greater than 27000
print("\nEmployees with Salary Above 27000:")
print(df[df["Salary"] > 27000])

# Filtering employees from IT department
print("\nEmployees in IT Department:")
print(df[df["Department"] == "IT"])

# Sorting employees by salary
print("\nEmployees Sorted by Salary:")
print(df.sort_values(by="Salary", ascending=False))
