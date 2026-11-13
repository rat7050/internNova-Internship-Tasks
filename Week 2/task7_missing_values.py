"""
Take a dataset containing missing values and perform the following:

Identify missing values using isnull() / isna().
Count missing values in each column.
Remove rows containing missing values.
Fill missing values using appropriate methods.
Display the dataset before and after handling missing values.

Briefly explain why handling missing data is important in Data Analytics.
"""

import pandas as pd

df = pd.read_csv("D:\Downloads\internNova Internship Tasks\Week 2\dataset\employee_missing.csv")

print("Original Dataset:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].mean())


df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nUpdated Dataset:")
print(df)

# Checking missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
