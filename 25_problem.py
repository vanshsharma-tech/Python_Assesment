# Program to store word frequencies from file

try:

    file = open("sample.txt", "r")

    text = file.read().lower()

    file.close()

    words = text.split()

    frequency = {}

    # Count word frequencies
    for word in words:

        word = word.strip(".,!?")

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Sort dictionary by frequency
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Display top 5 words
    print("Top Five Frequent Words:\n")

    for word, count in sorted_words[:5]:
        print(word, "->", count)

except FileNotFoundError:
    print("Error: File not found!")
