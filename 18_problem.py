# Program to count frequency of words in a paragraph
# and display the most repeated word

# Take paragraph input from user
paragraph = input("Enter a paragraph:\n")

# Convert paragraph to lowercase
paragraph = paragraph.lower()

# Remove punctuation marks manually
cleaned_text = ""

for ch in paragraph:

    if ch.isalnum() or ch.isspace():
        cleaned_text += ch

# Split paragraph into words
words = cleaned_text.split()

# Dictionary to store word frequency
word_frequency = {}

# Count occurrence of each word
for word in words:

    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Display word frequencies
print("\nWord Frequencies:\n")

for word, count in word_frequency.items():
    print(f"{word} -> {count}")

# Find most repeated word
most_repeated_word = ""
highest_count = 0

for word, count in word_frequency.items():

    if count > highest_count:
        highest_count = count
        most_repeated_word = word

# Display most repeated word
print("\nMost Repeated Word:\n")
print(f"{most_repeated_word} -> {highest_count} times")
