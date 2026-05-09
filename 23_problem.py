# Program to print pyramid pattern and calculate sum

rows = int(input("Enter number of rows: "))

total_sum = 0
number = 1

for i in range(1, rows + 1):

    for j in range(i):

        print(number, end=" ")
        total_sum += number
        number += 1

    print()

print("\nSum of all numbers:", total_sum)