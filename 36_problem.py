# ATM Simulation Program with PIN validation

correct_pin = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    pin = input("Enter ATM PIN: ")

    # Validate PIN
    if pin == correct_pin:

        print("Access Granted!")

        break

    else:

        attempts += 1

        print("Invalid PIN!")

        print(f"Remaining Attempts: {max_attempts - attempts}")

# Lock account after 3 failed attempts
if attempts == max_attempts:
    print("\nAccount Locked due to multiple invalid attempts.")