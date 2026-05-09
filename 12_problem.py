# Calculator Program using Multiple Exception Blocks

try:

    # Take first number input
    num1 = float(input("Enter first number: "))

    # Take operator input
    operator = input("Enter operation (+, -, *, /): ")

    # Take second number input
    num2 = float(input("Enter second number: "))

    # Perform calculation based on operator
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    else:
        # Raise error for invalid operation
        raise ValueError("Invalid Operator!")

    # Display result
    print(f"\nResult = {result}")

# Handle invalid numeric input
except ValueError as ve:
    print(f"\nError: {ve}")

# Handle division by zero
except ZeroDivisionError:
    print("\nError: Division by zero is not allowed!")

# Handle any other unexpected errors
except Exception as e:
    print(f"\nUnexpected Error: {e}")
