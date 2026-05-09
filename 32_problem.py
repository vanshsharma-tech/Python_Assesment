# Program to validate voting eligibility
# and handle invalid inputs gracefully

try:

    # Take age input
    age = int(input("Enter your age: "))

    # Validate negative age
    if age < 0:
        print("Invalid age entered!")

    # Check voting eligibility
    elif age >= 18:
        print("You are eligible to vote.")

    else:
        print("You are NOT eligible to vote.")

# Handle non-numeric input
except ValueError:
    print("Error: Please enter numeric values only!")

# Handle unexpected errors
except Exception as e:
    print("Unexpected Error:", e)