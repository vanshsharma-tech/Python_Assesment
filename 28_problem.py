# Mathematical Utility Program

def factorial(num):

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact


def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


def is_armstrong(num):

    digits = len(str(num))

    total = 0
    temp = num

    while temp > 0:

        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


while True:

    print("\n1. Factorial")
    print("2. Prime Check")
    print("3. Armstrong Check")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    elif choice == 2:

        n = int(input("Enter number: "))

        if is_prime(n):
            print("Prime Number")
        else:
            print("Not Prime")

    elif choice == 3:

        n = int(input("Enter number: "))

        if is_armstrong(n):
            print("Armstrong Number")
        else:
            print("Not Armstrong")

    elif choice == 4:

        print("Program Exited")
        break

    else:
        print("Invalid Choice!")