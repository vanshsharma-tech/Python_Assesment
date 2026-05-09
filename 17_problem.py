# Program to check Armstrong numbers
# using loops and conditional statements

# Take input from user
number = int(input("Enter a number: "))

# Store original number
original_number = number

# Count number of digits
digits = len(str(number))

# Variable to store sum
sum_of_powers = 0

# Calculate sum of digits raised to power of digits
temp = number

while temp > 0:

    digit = temp % 10

    sum_of_powers += digit ** digits

    temp = temp // 10

# Check Armstrong condition
if sum_of_powers == original_number:
    print(f"\n{original_number} is an Armstrong Number.")
else:
    print(f"\n{original_number} is NOT an Armstrong Number.")