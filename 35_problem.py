# Contact Management System

contacts = []

while True:

    print("\n===== Contact Management =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Contact
    if choice == 1:

        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact added successfully.")

    # Update Contact
    elif choice == 2:

        name = input("Enter contact name to update: ")

        found = False

        for contact in contacts:

            if contact["name"] == name:

                new_phone = input("Enter new phone number: ")

                contact["phone"] = new_phone

                print("Contact updated successfully.")

                found = True

        if not found:
            print("Contact not found!")

    # Search Contact
    elif choice == 3:

        name = input("Enter contact name to search: ")

        found = False

        for contact in contacts:

            if contact["name"] == name:

                print(contact)

                found = True

        if not found:
            print("Contact not found!")

    # Delete Contact
    elif choice == 4:

        name = input("Enter contact name to delete: ")

        found = False

        for contact in contacts:

            if contact["name"] == name:

                contacts.remove(contact)

                print("Contact deleted successfully.")

                found = True

                break

        if not found:
            print("Contact not found!")

    # Display Contacts
    elif choice == 5:

        print("\nAll Contacts:\n")

        for contact in contacts:
            print(contact)

    # Exit
    elif choice == 6:

        print("Program Exited")
        break

    else:
        print("Invalid Choice!")