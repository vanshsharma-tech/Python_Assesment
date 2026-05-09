# Write a Python program that accepts a paragraph from the user and calculates the number of uppercase
# letters, lowercase letters, digits, spaces, and special characters. Display the result in descending order based on
# frequency.
# Program to count character types in a paragraph

paragraph = input("Enter a paragraph: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

# Count characters
for ch in paragraph:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

# Store results in dictionary
result = {
    "Uppercase Letters": uppercase,
    "Lowercase Letters": lowercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special Characters": special,
}

# Sort in descending order based on frequency
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Display result
print("\nCharacter Frequency (Descending Order):")
for category, count in sorted_result:
    print(f"{category}: {count}")
