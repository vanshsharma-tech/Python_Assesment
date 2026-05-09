# Python program to merge two lists,
# remove duplicates, sort in descending order,
# and display numbers divisible by both 3 and 5

# Input two lists
list1 = [10, 15, 30, 45, 60, 75, 90]
list2 = [15, 25, 30, 50, 60, 75, 100]

# Merge both lists
merged_list = list1 + list2

# Remove duplicate values
unique_list = []

for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)

# Sort list in descending order (without using sort())
for i in range(len(unique_list)):
    for j in range(i + 1, len(unique_list)):

        # Swap elements for descending order
        if unique_list[i] < unique_list[j]:
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]

# Display numbers divisible by both 3 and 5
print("Numbers divisible by both 3 and 5:\n")

for num in unique_list:
    if num % 3 == 0 and num % 5 == 0:
        print(num)