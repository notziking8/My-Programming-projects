"""
Zion King
2/3/24
Comp 164-004

In this program I have been tasked to create a pet store
that will display the price of 3 different types of animals and there price
(Canine, Feline and Reptile)
"""

print("Welcome to the Aggie Pet Store")

# List of pets we offer in the pet store.
pets = ['Canine', 'Feline', 'Reptile']

# Gathering the price for each pet per category.
canine_Price = float(input("What is the price per Canine: "))
feline_Price = float(input("What is the price per Feline: "))
reptile_Price = float(input("What is the price per Reptile: "))

print("We offer the following pets: ")

# Displaying the available pets and their prices.
print(f'{pets[0]} at a cost of ${canine_Price:.2f}')
print(f'{pets[1]} at a cost of ${feline_Price:.2f}')
print(f'{pets[2]} at a cost of ${reptile_Price:.2f}')
