# Recursive function to calculate sum of digits

def recursive_sum(number):

    # Base case
    if number == 0:
        return 0

    return (number % 10) + recursive_sum(number // 10)


# Iterative approach
def iterative_sum(number):

    total = 0

    while number > 0:

        total += number % 10

        number //= 10

    return total


# User input
num = int(input("Enter a number: "))

# Display results
print("\nRecursive Sum of Digits:", recursive_sum(num))

print("Iterative Sum of Digits:", iterative_sum(num))