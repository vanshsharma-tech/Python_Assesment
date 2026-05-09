# Program to check whether a string is a palindrome
# after removing spaces, punctuation, and converting to lowercase

# Take input from user
text = input("Enter a string: ")

# Empty string to store cleaned text
cleaned_text = ""

# Remove spaces and punctuation marks
for ch in text:

    # Keep only alphanumeric characters
    if ch.isalnum():
        cleaned_text += ch.lower()

# Check palindrome
if cleaned_text == cleaned_text[::-1]:
    print("\nThe given string is a Palindrome.")
else:
    print("\nThe given string is NOT a Palindrome.")