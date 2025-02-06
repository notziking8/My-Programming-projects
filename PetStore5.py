"""
Zion King
COMP 163 - 004
5/1/24
"""


pets = ['Canine', 'Feline', 'Snake', 'Lizard']
def setupStore():
    # set up inventory for pet store
    inventory = dict()
    # Enter cost of each pet in each category
    for pet in pets:
        cat = list()
        num = int(input(f"How many {pet} would you like to enter: "))
        if num <= 0: continue
        for i in range(0,num):
            animal = ''
            if pet == 'Canine':
                animal = createCanine()
            elif pet == 'Feline':
                animal = createFeline()
            elif pet == 'Snake':
                animal = createSnake()
            elif pet == 'Lizard':
                animal = createLizard()
            animal.inventory.setLocation(input('Location: '))
            animal.inventory.setQuantity(int(input('Quantity: ')))
            animal.inventory.setPrice(float(input('Price: ')))
            cat.append(animal)
        inventory[pet] = cat
    return inventory

def createCanine():
    animal = C.Canine()
    animal.setName(input('Name: '))
    animal.setSize(input('Size: '))
    animal.setWeight(float(input('Weight: ')))
    animal.setColor(input('Color: '))
    return animal
def createFeline():
    animal = F.Feline()
    animal.setName(input('Name: '))
    animal.setSize(input('Size (S/M/L/XL): '))
    animal.setWeight(float(input('Weight: ')))
    animal.setColor(input('Color:'))
    return animal
def createSnake():
    animal = S.Snake()
    animal.setName(input('Name: '))
    animal.setConstrictor(bool(input('Is Constrictor (True/False): ')))
    animal.setColor(input('Color: '))

    return animal
def createLizard():
    animal = L.Lizard()
    animal.setName(input('Name: '))
    animal.setHabitat(input('Habitat: '))
    animal.setFrill(input('Has Frill (True/False): '))
    animal.setSpikes(input('Spikes (True/False): '))
    return animal

def displayInventory(inventory):
    # Display the pet store menu optons
    print("We offer the following pets")


    for cat, pets in inventory.items():
        print(f"{cat} : ")
        for pet in pets:
            print(f"\t{pet.getName()} count {pet.inventory.getQuantity()} cost ${pet.inventory.getPrice():,.2f}.")
def petStoreMenu():
    # Display the menu
    print("\n")
    print("A) Setup Store")
    print("B) Display Pets")
    print("C) Sale Pet")
    print("D) Total Sale")
    print("E) Exit")

def calculateTax(total):
    # caculate the total tax
    totalSale = 0.0
    stateTax = 0.07
    fedTax = 0.10
    totalSale += total * stateTax
    totalSale += total * fedTax
    totalSale += total
    print(f"\t\t\tState Tax \t\t\t${stateTax:.2f}")
    print(f"\t\t\tFederal Tax \t\t${fedTax:.2f}")
    print(f"\t\t\tTotal Due \t\t\t${totalSale:.2f}")

def POS(sale, inventory):

    catMenu = 1
    print("What category would you like to sale : ")
    for cat in inventory.keys():
        print(f"{catMenu}) {cat}")
        catMenu += 1
    catMenuSelection = int(input(f"What is being sold:  "))
    cat = list(inventory.keys())[catMenuSelection-1]
    petList = inventory.get(list(inventory.keys())[catMenuSelection-1])

    petMenu = 1
    for pet in petList:
        print(f"{petMenu}) {pet.getName()}")
        petMenu += 1
    petMenuSelection = int(input(f"What {cat} is being sold:  "))
    petItem = petList[petMenuSelection-1]
    if petItem.inventory.getQuantity() <= 0 :
        print("Sorry out of stock!")
    else:
        PetPrice = petItem.inventory.getPrice()
        qty = int(input(f"How many {petItem.getName()} are being sold: "))
        itemNum = len(sale)+1
        sale[itemNum] = [pets[catMenuSelection-1], petItem.getName(), PetPrice,qty,(qty*PetPrice)]
        petItem.inventory.setPrice(petItem.inventory.getPrice()-qty)
    return sale

def displayReceipt(sale):
    # test data used when testing just the D menu selection
    # sale = {1: ['Canine', 'Terrier', 56.45, 2, 112.9], 2: ['Reptile', 'Corn', 5.9, 1, 5.9]}
    print("\n")
    print("Aggie Pet Store Bill of Sale")
    print("_"*50)
    total = 0.0
    for k,v in sale.items():
        print(f"{k:d}. {v[0]}\t{v[1]}\t${v[2]:,.2f}\t{v[3]:,d}\t${v[4]:,.2f}")
        total += v[4]
    calculateTax(total)
    print("_" * 50)

def closePetStore():
    print("Thank you for using the Aggie PetStore POS")
    print("Aggie Pride!")


if __name__ == "__main__":
    inventory = dict()
    # test data used when testing the C menu option
    # inventory = {'Canine': {'Begal': 56.45, 'Bull': 125.0}, 'Feline': {'Main Coon': 2000.0},
    #            'Reptile': {'Rat': 25.0, 'Corn': 5.9, 'Boa': 112.0}}
    sale = dict()
    totalSale = 0.0
    stateTax = 0.07
    fedTax = 0.10
    print("Welcome to the Aggie Pet Store")
    while True:
        petStoreMenu()
        print("\n")
        option = input("Menu selection: ").upper()
        if option == "E":
            break
        elif option == "A":
            inventory = setupStore()

        elif option == "B":
            displayInventory(inventory)
        elif option == "C":
            sale = POS(sale, inventory)

        elif option == "D":
            displayReceipt(sale)
            sale= dict()
        else:
            print("Invalid Selection.... Please select again.")
            print("\n")
    # Display the pets and price
    print("\n\n")
    closePetStore()

