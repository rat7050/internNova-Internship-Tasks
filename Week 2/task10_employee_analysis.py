"""
Perform a basic data analysis project using NumPy and Pandas.

Choose a dataset such as:
Student Performance Dataset
Sales Dataset
Employee Dataset
E-commerce Dataset
Customer Dataset

Your project should include:
Loading the dataset.
Data inspection.
Identifying and handling missing values.
Selecting and filtering data.
Sorting data.
Performing GroupBy analysis.
Creating at least one Pivot Table.
Finding useful insights from the dataset.
Exporting the cleaned/processed dataset.

"""
import pandas as pd
import numpy as np

# Reading employee dataset
df = pd.read_csv("D:\\Downloads\\internNova Internship Tasks\\Week 2\\dataset\\employee_data.csv")

print("Employee Dataset:")
print(df)

# Total number of employees
print("\nTotal Employees:", len(df))

# Average salary
average_salary = np.mean(df["Salary"])
print("Average Salary:", average_salary)

# Highest and lowest salary
print("Highest Salary:", np.max(df["Salary"]))
print("Lowest Salary:", np.min(df["Salary"]))

# Total salary expenditure
print("Total Salary:", np.sum(df["Salary"]))

# Department-wise employee count
print("\nEmployees in Each Department:")
print(df["Department"].value_counts())

# Department-wise average salary
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

# Sorting employees by salary
print("\nEmployees by Salary:")
print(df.sort_values(by="Salary", ascending=False))
