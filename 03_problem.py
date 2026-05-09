# Create a program that generates the first N prime numbers using a for loop and also calculates the sum and
# average of those prime numbers.


# Create a genPrimeNumber for return the number is prime or not
def genPrimeNumber(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    return is_prime


sum_of_prime_number = 0
avg_of_prime_number = 0
count = 0
# User input for genrate the nth term series for identify the prime number
n = int(input("Enter the range:"))
for i in range(n + 1):
    if genPrimeNumber(i):
        # Here calculating the sum of prime numbers
        sum_of_prime_number += i
        count += 1
# Here we calculating the average of prime number
avg_of_prime_number = sum_of_prime_number / count
# Print the result
print("Sum of prime number is :", sum_of_prime_number)
print("Average of prime number is :", avg_of_prime_number)