"""
Zion King
COMP 163 - 004
4/7/24
In this program, I will be modifying Pet store 3 to use classes and objects
"""

# Import animal classes from the classes module
from Classes import Canine, Feline, Snake, Lizard

# Initialize inventory dictionary
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

    pets = ['Canine', 'Feline', 'Snake', 'Lizard']  # List of all pet types
    for pet_type in pets:
        num_pets = int(input(f"How many {pet_type}s would you like to enter: "))
        inventory[pet_type] = {}

        for _ in range(num_pets):
            pet_name = input(f"What is the name of the {pet_type}: ")
            pet_cost = float(input(f"What is the price of {pet_name}: "))

            # Create instances based on pet_type
            if pet_type == 'Canine':
                size = input(f"Enter size of {pet_name}: ")
                weight = float(input(f"Enter weight of {pet_name}: "))
                color = input(f"Enter color of {pet_name}: ")
                pet_instance = Canine(pet_name, size, weight, color)
            elif pet_type == 'Feline':
                size = input(f"Enter size of {pet_name}: ")
                weight = float(input(f"Enter weight of {pet_name}: "))
                color = input(f"Enter color of {pet_name}: ")
                pet_instance = Feline(pet_name, size, weight, color)
            elif pet_type == 'Snake':
                size = input(f"Enter size of {pet_name}: ")
                weight = float(input(f"Enter weight of {pet_name}: "))
                pet_instance = Snake(pet_name, size, weight)
            elif pet_type == 'Lizard':
                size = input(f"Enter size of {pet_name}: ")
                weight = float(input(f"Enter weight of {pet_name}: "))
                pet_instance = Lizard(pet_name, size, weight)

            # Store the instance and cost in inventory
            inventory[pet_type][pet_name] = {
                "instance": pet_instance,
                "cost": pet_cost
            }

    print("Pet Store setup completed.")

# Function to display inventory
def display_inventory():
    print("\nWe offer the following pets:\n")
    for pet_type, pets_info in inventory.items():
        print(f"\n{pet_type}:")
        for pet_name, pet_data in pets_info.items():
            pet_cost = pet_data["cost"]
            print(f"\t{pet_name} at a cost of ${pet_cost:,.2f}")

# Function to calculate taxes for a sale
def calculate_tax(line_items):
    total = sum(item["Total"] for item in line_items.values())
    state_tax_total = total * state_tax
    federal_tax_total = total * federal_tax
    total_due = total + state_tax_total + federal_tax_total
    return state_tax_total, federal_tax_total, total_due

# Function to display a receipt for the sale
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

# Function for Point of Sale
def pos(line_items, inventory):
    global transaction_number
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
    pet_name = list(inventory[pet_category].keys())[pet_choice - 1]
    pet_instance = inventory[pet_category][pet_name]['instance']
    pet_cost = inventory[pet_category][pet_name]['cost']

    quantity = int(input("Enter the quantity being sold: "))
    total_cost = quantity * pet_cost

    line_items[f"Transaction {transaction_number}"] = {
        "Pet Category": pet_category,
        "Pet Type": pet_name,
        "Quantity": quantity,
        "Price": pet_cost,
        "Total": total_cost
    }

    print("Sale recorded successfully!")
    transaction_number += 1  # Increment transaction number after each sale

# Main function
def main():
    line_items = {}

    print("Welcome to the Aggie Pet Store")
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

# Run the program
if __name__ == "__main__":
    main()
