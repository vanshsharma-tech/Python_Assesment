# Program to read student marks from a text file
# and display topper, average marks,
# and students scoring below average

# Create and write data into file
file = open("students.txt", "w")

file.write("Rahul 78\n")
file.write("Aman 92\n")
file.write("Priya 85\n")
file.write("Sneha 67\n")
file.write("Karan 55\n")

file.close()

# Read data from file
file = open("students.txt", "r")

students = []

# Store student records
for line in file:

    data = line.split()

    name = data[0]
    marks = int(data[1])

    students.append((name, marks))

file.close()

# Find topper
topper = students[0]

# Calculate total marks
total_marks = 0

for student in students:

    total_marks += student[1]

    # Check topper
    if student[1] > topper[1]:
        topper = student

# Calculate average marks
average_marks = total_marks / len(students)

# Display topper
print("Topper Details:")
print(f"Name: {topper[0]}")
print(f"Marks: {topper[1]}")

# Display average marks
print(f"\nAverage Marks: {average_marks:.2f}")

# Display students scoring below average
print("\nStudents Scoring Below Average:\n")

for student in students:

    if student[1] < average_marks:
        print(f"{student[0]} -> {student[1]}")
