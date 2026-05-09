# Program to store employee records using tuples
# and display employees whose salary is above average

# Employee records
# Each tuple contains: (Employee ID, Name, Salary)

employees = [
    (101, "Rahul", 45000),
    (102, "Aman", 52000),
    (103, "Priya", 60000),
    (104, "Sneha", 48000),
    (105, "Karan", 70000),
]

# Calculate total salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

# Calculate average salary
average_salary = total_salary / len(employees)

# Display average salary
print(f"Average Salary: ₹{average_salary:.2f}\n")

# Display employees with salary above average
print("Employees with salary above average:\n")

for emp in employees:

    # emp[2] represents salary
    if emp[2] > average_salary:
        print(f"Employee ID: {emp[0]}")
        print(f"Name: {emp[1]}")
        print(f"Salary: ₹{emp[2]}")
        print("----------------------")
