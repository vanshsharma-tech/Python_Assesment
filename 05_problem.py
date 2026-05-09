# Function to find second largest and second smallest
# without using built-in sorting functions


def find_second_elements(numbers):

    # Remove duplicate values manually
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Check if list has at least 2 unique elements
    if len(unique_numbers) < 2:
        return "List must contain at least two unique numbers."

    # Initialize variables
    smallest = second_smallest = float("inf")
    largest = second_largest = float("-inf")

    # Find smallest, second smallest, largest, second largest
    for num in unique_numbers:

        # Find smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest:
            second_smallest = num

        # Find largest and second largest
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest:
            second_largest = num

    # Return results
    return second_smallest, second_largest


# Example list
numbers = [12, 45, 7, 89, 23, 45, 7, 90]

# Function call
result = find_second_elements(numbers)

# Display output
print("Second Smallest:", result[0])
print("Second Largest:", result[1])
