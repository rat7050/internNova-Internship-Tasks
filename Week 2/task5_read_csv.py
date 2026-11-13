"""
Use a CSV dataset and perform the following operations:

Read the CSV file using Pandas.
Display the first 5 rows using head().
Display the last 5 rows using tail().
Check the number of rows and columns.
Display column names.
Check data types using dtypes.
Use info() and describe() to understand the dataset.
"""
import pandas as pd

# Read CSV file
df = pd.read_csv("D:\Downloads\internNova Internship Tasks\Week 2\dataset\employee_data.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Display last five rows
print("\nLast Five Rows:")
print(df.tail())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check shape
print("\nDataset Shape:", df.shape)
