# Initialize an empty inventory dictionary
inventory = {}

def display_menu():
    print("\nInventory Management System")
    print("1. Add new item")
    print("2. Update item quantity")
    print("3. View all items")
    print("4. Remove item")
    print("5. Exit")

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory[name] = {"quantity": quantity, "price": price}
    print(f"{name} added to inventory.")

def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        change = int(input("Enter quantity change (positive to add, negative to subtract): "))
        inventory[name]["quantity"] += change
        print(f"{name} updated. New quantity: {inventory[name]['quantity']}")
    else:
        print("Item not found in inventory.")

def view_items():
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\nCurrent Inventory:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total Value"))
    print("-" * 50)
    
    for item, details in inventory.items():
        total_value = details["quantity"] * details["price"]
        print("{:<20} {:<10} {:<10.2f} ${:<10.2f}".format(
            item, details["quantity"], details["price"], total_value))

def remove_item():
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print("Item not found in inventory.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        view_items()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting inventory system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")