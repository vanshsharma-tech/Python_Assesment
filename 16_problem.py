# Python program to generate Fibonacci numbers up to N
# and store only even Fibonacci numbers in a list

# Function to generate Fibonacci series
def generate_fibonacci(n):

    # First two Fibonacci numbers
    a = 0
    b = 1

    # List to store even Fibonacci numbers
    even_fibonacci = []

    print("Fibonacci Series:\n")

    # Generate Fibonacci numbers up to N
    while a <= n:

        print(a, end=" ")

        # Store only even Fibonacci numbers
        if a % 2 == 0:
            even_fibonacci.append(a)

        # Generate next Fibonacci number
        temp = a + b
        a = b
        b = temp

    # Return even Fibonacci list
    return even_fibonacci


# Take input from user
N = int(input("\n\nEnter the value of N: "))

# Function call
even_numbers = generate_fibonacci(N)

# Display even Fibonacci numbers
print("\n\nEven Fibonacci Numbers:\n")
print(even_numbers)