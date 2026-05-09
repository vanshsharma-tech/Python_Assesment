# Function for division with exception handling

def divide_numbers(a, b):

    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

    except TypeError:
        print("Error: Invalid input type!")

    except Exception as e:
        print("Unexpected Error:", e)


# User input
try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    divide_numbers(num1, num2)

except ValueError:
    print("Error: Please enter numeric values only!")