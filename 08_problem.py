# Python program to perform set operations

# Take input for first set
set1 = set(map(int, input("Enter elements of Set 1 separated by space: ").split()))

# Take input for second set
set2 = set(map(int, input("Enter elements of Set 2 separated by space: ").split()))

# Perform Union Operation
union_set = set1.union(set2)

# Perform Intersection Operation
intersection_set = set1.intersection(set2)

# Perform Symmetric Difference Operation
symmetric_diff = set1.symmetric_difference(set2)

# Check Subset Operation
is_subset = set1.issubset(set2)

# Display results
print("\n----- Set Operations Result -----")

print("Union:", union_set)

print("Intersection:", intersection_set)

print("Symmetric Difference:", symmetric_diff)

# Display subset result
if is_subset:
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is NOT a subset of Set 2")