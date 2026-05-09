# Simple Menu-Driven Banking Application

# Initial balance
balance = 0

# Infinite loop to keep the program running
while True:

    # Display menu options
    print("\n===== Banking Menu =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    # Take user choice
    choice = int(input("Enter your choice (1-4): "))

    # Deposit Option
    if choice == 1:
        deposit = float(input("Enter amount to deposit: "))

        # Check if deposit amount is valid
        if deposit > 0:
            balance += deposit
            print(f"₹{deposit} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    # Withdraw Option
    elif choice == 2:
        withdraw = float(input("Enter amount to withdraw: "))

        # Check if sufficient balance is available
        if withdraw <= balance:
            balance -= withdraw
            print(f"₹{withdraw} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Balance Check Option
    elif choice == 3:
        print(f"Current Balance: ₹{balance}")

    # Exit Option
    elif choice == 4:
        print("Thank you for using the banking application.")
        break

    # Invalid Choice Handling
    else:
        print("Invalid choice! Please select between 1 and 4.")
