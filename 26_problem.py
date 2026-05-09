# Program to separate vowels and consonants

sentence = input("Enter a sentence: ")

vowels = []
consonants = []

for ch in sentence.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels.append(ch)
        else:
            consonants.append(ch)

print("\nVowels:")
print(vowels)

print("\nConsonants:")
print(consonants)