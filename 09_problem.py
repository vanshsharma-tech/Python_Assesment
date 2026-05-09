# Dictionary-Based Inventory Management System

# Empty dictionary to store inventory
# Format: {product_name: quantity}
inventory = {}

# Infinite loop for menu-driven program
while True:

    # Display menu
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Search Product")
    print("4. Display Low-Stock Products")
    print("5. Exit")

    # Take user choice
    choice = int(input("Enter your choice (1-5): "))

    # Add Product
    if choice == 1:

        product = input("Enter product name: ")
        quantity = int(input("Enter product quantity: "))

        # Add product to dictionary
        inventory[product] = quantity

        print(f"{product} added successfully.")

    # Update Product Quantity
    elif choice == 2:

        product = input("Enter product name to update: ")

        # Check if product exists
        if product in inventory:

            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity

            print(f"{product} quantity updated successfully.")

        else:
            print("Product not found!")

    # Search Product
    elif choice == 3:

        product = input("Enter product name to search: ")

        # Search product in dictionary
        if product in inventory:
            print(f"{product} is available with quantity: {inventory[product]}")
        else:
            print("Product not found!")

    # Display Low-Stock Products
    elif choice == 4:

        print("\nLow-Stock Products (Quantity less than 5):")

        found = False

        # Check products with low quantity
        for product, quantity in inventory.items():

            if quantity < 5:
                print(f"{product} -> Quantity: {quantity}")
                found = True

        # If no low-stock product found
        if not found:
            print("No low-stock products available.")

    # Exit Program
    elif choice == 5:

        print("Exiting Inventory Management System...")
        break

    # Invalid Choice Handling
    else:
        print("Invalid choice! Please select between 1 and 5.")