"""
Create a Pandas program that:

Creates a Pandas Series.
Creates a DataFrame containing student or employee information.
Displays the DataFrame.
Displays the column names.
Displays the index.
Adds a new column to the DataFrame.
Displays the updated DataFrame
"""

import pandas as pd

# Creating a Pandas Series
marks = pd.Series([75, 82, 90, 68, 85])

print("Pandas Series:")
print(marks)

# Creating an employee DataFrame
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Aman", "Priya", "Rohit", "Neha"],
    "Department": ["IT", "HR", "Sales", "IT", "Finance"],
    "Salary": [25000, 28000, 30000, 27000, 32000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("\nEmployee DataFrame:")
print(df)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display index
print("\nDataFrame Index:")
print(df.index)

# Add a new column
df["Experience"] = [1, 2, 3, 2, 4]

# Display updated DataFrame
print("\nUpdated DataFrame:")
print(df)