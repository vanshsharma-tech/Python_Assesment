# Program to encrypt and decrypt message
# using Caesar Cipher technique

# Function for encryption
def encrypt(message, shift):

    encrypted = ""

    for ch in message:

        if ch.isalpha():

            # Preserve uppercase and lowercase
            base = 65 if ch.isupper() else 97

            encrypted += chr((ord(ch) - base + shift) % 26 + base)

        else:
            encrypted += ch

    return encrypted


# Function for decryption
def decrypt(message, shift):

    return encrypt(message, -shift)


# User input
text = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Encrypt message
encrypted_text = encrypt(text, shift)

# Decrypt message
decrypted_text = decrypt(encrypted_text, shift)

# Display results
print("\nEncrypted Message:", encrypted_text)

print("Decrypted Message:", decrypted_text)