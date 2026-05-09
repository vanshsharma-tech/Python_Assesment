# Tuples containing student names and courses

course1 = ("Rahul", "Aman", "Priya", "Sneha")
course2 = ("Priya", "Karan", "Rahul", "Vikas")

# Convert tuples into sets
set1 = set(course1)
set2 = set(course2)

# Find students enrolled in multiple courses
common_students = set1.intersection(set2)

print("Students enrolled in multiple courses:\n")
print(common_students)