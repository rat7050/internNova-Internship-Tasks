"""
After processing the dataset:

Export the final DataFrame to a new CSV file.
Verify that the exported file contains the processed data.
Save the file properly for submission.
"""
import pandas as pd

# Reading employee dataset
df = pd.read_csv(r"D:\Downloads\internNova Internship Tasks\Week 2\dataset\employee_data.csv")

print("Original Employee Data:")
print(df)

# Adding a new column
df["Bonus"] = df["Salary"] * 0.10

# Exporting data to CSV
df.to_csv(r"D:\Downloads\internNova Internship Tasks\Week 2\dataset\updated_employee_data.csv", index=False)

# Exporting data to Excel
df.to_excel(r"D:\Downloads\internNova Internship Tasks\Week 2\dataset\updated_employee_data.xlsx", index=False)

print("\nUpdated Employee Data:")
print(df)

print("\nData exported successfully!")
