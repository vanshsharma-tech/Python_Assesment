# Program to display students with attendance below 75%

import pandas as pd

# Create sample attendance data
data = {
    "Name": ["Rahul", "Aman", "Priya", "Sneha", "Karan"],
    "Attendance": [82, 68, 91, 70, 74]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Save data into CSV file
df.to_csv("attendance.csv", index=False)

# Read CSV file
attendance_data = pd.read_csv("attendance.csv")

# Filter students below 75% attendance
low_attendance = attendance_data[
    attendance_data["Attendance"] < 75
]

# Display result
print("Students with Attendance Below 75%:\n")
print(low_attendance)