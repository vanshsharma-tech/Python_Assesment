# Mini Student Management System

import pandas as pd

# File name
FILE_NAME = "students.txt"

# Function to add student
def add_student():

    try:

        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        # Save student data into file
        file = open(FILE_NAME, "a")

        file.write(f"{roll},{name},{marks}\n")

        file.close()

        print("Student added successfully.")

    except ValueError:
        print("Invalid marks entered!")

    except Exception as e:
        print("Error:", e)


# Function to display all students
def display_students():

    try:

        file = open(FILE_NAME, "r")

        data = file.readlines()

        file.close()

        print("\nStudent Records:\n")

        for line in data:
            print(line.strip())

    except FileNotFoundError:
        print("No student records found!")

    except Exception as e:
        print("Error:", e)


# Function to generate report using Pandas
def generate_report():

    try:

        # Read file using pandas
        df = pd.read_csv(
            FILE_NAME,
            names=["Roll", "Name", "Marks"]
        )

        # Assign grades
        def grade(marks):

            if marks >= 90:
                return "A+"

            elif marks >= 75:
                return "A"

            elif marks >= 60:
                return "B"

            else:
                return "C"

        # Apply grade function
        df["Grade"] = df["Marks"].apply(grade)

        # Display report
        print("\nStudent Report:\n")
        print(df)

    except FileNotFoundError:
        print("Student file not found!")

    except Exception as e:
        print("Error:", e)


# Main menu
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Generate Report")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Add student
    if choice == 1:
        add_student()

    # Display students
    elif choice == 2:
        display_students()

    # Generate report
    elif choice == 3:
        generate_report()

    # Exit program
    elif choice == 4:

        print("Program Exited")
        break

    else:
        print("Invalid choice!")