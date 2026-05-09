# Pandas program to read employee data from CSV file
# and display department-wise average salary
# and highest salary employee

import pandas as pd

# Create sample employee data
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Karan"],
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [45000, 70000, 65000, 55000, 50000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save data into CSV file
df.to_csv("employees.csv", index=False)

# Read data from CSV file
employees = pd.read_csv("employees.csv")

# Display employee data
print("Employee Data:\n")
print(employees)

# Calculate department-wise average salary
avg_salary = employees.groupby("Department")["Salary"].mean()

# Display average salary
print("\nDepartment-wise Average Salary:\n")
print(avg_salary)

# Find highest salary employee
highest_salary_employee = employees.loc[employees["Salary"].idxmax()]

# Display highest salary employee
print("\nHighest Salary Employee:\n")
print(highest_salary_employee)