# File Processing Program
# Counts total words, lines, and characters in a text file
# Handles file not found errors

try:

    # Take file name input from user
    file_name = input("Enter file name: ")

    # Open file in read mode
    file = open(file_name, "r")

    # Read file content
    content = file.read()

    # Count total characters
    characters = len(content)

    # Count total words
    words = len(content.split())

    # Count total lines
    lines = len(content.splitlines())

    # Close file
    file.close()

    # Display results
    print("\nFile Analysis Result:\n")

    print(f"Total Lines      : {lines}")
    print(f"Total Words      : {words}")
    print(f"Total Characters : {characters}")

# Handle file not found error
except FileNotFoundError:
    print("\nError: File not found!")

# Handle other unexpected errors
except Exception as e:
    print(f"\nUnexpected Error: {e}")
