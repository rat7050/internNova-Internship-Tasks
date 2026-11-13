"""
Using two or more datasets, perform the following operations:

Merge & Concatenate
Merge two DataFrames using a common column.
Concatenate two DataFrames.
GroupBy
Group data based on a selected column.
Calculate aggregate values such as sum, mean, count, minimum, or maximum.
Pivot Table
Create a Pivot Table using Pandas.
Summarize the data based on appropriate rows, columns, and values.

Display the output of each operation.
"""
import pandas as pd

# Reading two CSV files
employees = pd.read_csv("D:\Downloads\internNova Internship Tasks\Week 2\dataset\employee_data.csv")
departments = pd.read_csv("D:\Downloads\internNova Internship Tasks\Week 2\dataset\department_data.csv")

# Merging both datasets
merged_data = pd.merge(employees, departments, on="Department")

print("Merged Dataset:")
print(merged_data)

# Grouping employees by department
print("\nAverage Salary by Department:")
print(merged_data.groupby("Department")["Salary"].mean())

# Creating a pivot table
print("\nPivot Table:")
pivot = pd.pivot_table(
    merged_data,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print(pivot)
