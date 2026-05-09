# Q2. Develop a grading system where marks of five subjects are entered by the user. The program should
# calculate percentage, assign grades using nested if-else conditions, and identify whether the student qualifies for
# a scholarship.
# Grading System Program

# Input marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

# Assign grade using nested if-else
if percentage >= 90:
    grade = "A+"
    scholarship = "Qualified for Full Scholarship"
else:
    if percentage >= 75:
        grade = "A"
        scholarship = "Qualified for Partial Scholarship"
    else:
        if percentage >= 60:
            grade = "B"
            scholarship = "Not Qualified for Scholarship"
        else:
            if percentage >= 40:
                grade = "C"
                scholarship = "Not Qualified for Scholarship"
            else:
                grade = "Fail"
                scholarship = "Not Qualified for Scholarship"

# Display results
print("\n----- Result -----")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Scholarship Status: {scholarship}")
