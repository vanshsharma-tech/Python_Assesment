# Program to copy contents from one file to another
# and display total number of words copied

try:

    # Open source file
    source = open("source.txt", "r")

    # Read file content
    content = source.read()

    source.close()

    # Open destination file
    destination = open("destination.txt", "w")

    # Copy content
    destination.write(content)

    destination.close()

    # Count total words
    word_count = len(content.split())

    print("File copied successfully.")
    print("Total Words Copied:", word_count)

except FileNotFoundError:
    print("Error: Source file not found!")

except Exception as e:
    print("Unexpected Error:", e)
