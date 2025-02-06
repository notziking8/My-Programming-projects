"""
Zion King
Comp 163-004
3/17/24
in this program I will be modifying petstore 2 to add a menu and point of sale.
"""

inventory = {}
state_tax = 0.07
federal_tax = 0.10
transaction_number = 1

# Function to display the main menu
def display_menu():
    print("\n=== Pet Store Menu ===")
    print("A) Set Up Pet Store")
    print("B) Display Pets")
    print("C) Sale Pet")
    print("D) Total Sale")
    print("E) Exit")

# Function to set up the pet store
def setup_store():
    global inventory
    print("Welcome to the Pet Store Setup")
    pets = ['Canine', 'Feline', 'Reptile']
    for pet_type in pets:
        num_pets = int(input(f"How many {pet_type}s would you like to enter: "))
        inventory[pet_type] = {}
        for i in range(num_pets):
            pet_name = input(f"What is the type of {pet_type}: ")
            pet_cost = float(input(f"What is the price per {pet_name}: "))
            inventory[pet_type][pet_name] = pet_cost

# Function to display inventory
def display_inventory():
    print("\nWe offer the following pets:\n")
    for pet_type, pets_info in inventory.items():
        print(f"\n{pet_type}:")
        for pet_name, pet_cost in pets_info.items():
            print(f"\t{pet_name} at a cost of ${pet_cost:,.2f}")

# Function for Point of Sale
def pos(line_items, inventory):
    print("\n=== Point of Sale ===")
    print("Select the category of pet:")
    for index, pet_type in enumerate(inventory.keys(), start=1):
        print(f"{index}. {pet_type}")

    category_choice = int(input("Enter the number corresponding to the category: "))
    pet_category = list(inventory.keys())[category_choice - 1]

    print(f"Select the type of {pet_category}:")
    for index, pet_name in enumerate(inventory[pet_category].keys(), start=1):
        print(f"{index}. {pet_name}")

    pet_choice = int(input("Enter the number corresponding to the pet type: "))
    pet_type = list(inventory[pet_category].keys())[pet_choice - 1]

    quantity = int(input("Enter the quantity being sold: "))
    line_items[f"Transaction {transaction_number}"] = {
        "Pet Category": pet_category,
        "Pet Type": pet_type,
        "Quantity": quantity,
        "Price": inventory[pet_category][pet_type],
        "Total": quantity * inventory[pet_category][pet_type]
    }
    print("Sale recorded successfully!")

# Function to calculate tax
def calculate_tax(line_items):
    total = sum(item["Total"] for item in line_items.values())
    state_tax_total = total * state_tax
    federal_tax_total = total * federal_tax
    total_due = total + state_tax_total + federal_tax_total
    return state_tax_total, federal_tax_total, total_due

# Function to display receipt
def display_receipt(line_items):
    print("\n==================================================")
    print("============== Aggie Pet Store Receipt ============")
    print("==================================================")
    for transaction, details in line_items.items():
        print(f"Transaction: {transaction}")
        print(f"Pet Category: {details['Pet Category']}")
        print(f"Pet Type: {details['Pet Type']}")
        print(f"Price per Pet: ${details['Price']:,.2f}")
        print(f"Quantity: {details['Quantity']}")
        print(f"Line Item Total: ${details['Total']:,.2f}")
    state_tax_total, federal_tax_total, total_due = calculate_tax(line_items)
    print("==================================================")
    print(f"State Tax (7%): ${state_tax_total:,.2f}")
    print(f"Federal Tax (10%): ${federal_tax_total:,.2f}")
    print(f"Total Due: ${total_due:,.2f}")
    print("==================================================")

# Function to close the pet store
def close_pet_store():
    print("Thank you for visiting Aggie Pet Store. Goodbye!")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (A/B/C/D/E): ").upper()
        if choice == 'A':
            setup_store()
        elif choice == 'B':
            display_inventory()
        elif choice == 'C':
            pos(line_items, inventory)
        elif choice == 'D':
            display_receipt(line_items)
        elif choice == 'E':
            close_pet_store()
            break
        else:
            print("Invalid choice. Please select from A to E.")

# Initialize line items dictionary
line_items = {}

# Run the program
print("Welcome to the Aggie Pet Store")
main()
