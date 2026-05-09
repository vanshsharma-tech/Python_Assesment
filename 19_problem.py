# Function to return factorial of only even numbers

# Function to calculate factorial
def factorial(num):

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact


# Function to process list
def even_factorials(numbers):

    # List to store factorials of even numbers
    result = []

    for num in numbers:

        # Check if number is even
        if num % 2 == 0:

            # Append factorial of even number
            result.append(factorial(num))

    return result


# Example list
numbers = [1, 2, 3, 4, 5, 6]

# Function call
output = even_factorials(numbers)

# Display result
print("Factorials of Even Numbers:\n")
print(output)