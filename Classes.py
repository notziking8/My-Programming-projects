class Animal:
    def __init__(self, name):
        # Basic attributes common to all animals
        self.multiCellular = True
        self.sexualReproduction = True
        self.heterotroph = True
        self.fourLimbs = True
        self.backBone = True
        self.TYPE = "Animal"  # Constant identifying the type of class
        self.name = name  # Name of the animal

    def getMultiCellular(self):
        return self.multiCellular  # Method to retrieve if the animal is multicellular

    def getSexualReproduction(self):
        return self.sexualReproduction  # Method to check if animal reproduces sexually

    def getIsHeterotroph(self):
        return self.heterotroph  # Method to check if animal is a heterotroph

    def hasFourLimbs(self):
        return self.fourLimbs  # Method to check if animal has four limbs

    def setFourLimbs(self, hasFourLimbs):
        self.fourLimbs = hasFourLimbs  # Method to set if animal has four limbs

    def hasBackBone(self):
        return self.backBone  # Method to check if animal has a backbone

    def getName(self):
        return self.name  # Method to get the name of the animal

    def setName(self, name):
        self.name = name  # Method to set the name of the animal


class Inventory:
    def __init__(self, location="N/A", quantity=0, price=0.0):
        # Inventory class for tracking location, quantity, and price of items
        self.location = location  # Location where the item is stored
        self.quantity = quantity  # Quantity of the item
        self.price = price  # Price of the item

    def getQuantity(self):
        return self.quantity  # Method to get the quantity of the item

    def getPrice(self):
        return self.price  # Method to get the price of the item

    def getLocation(self):
        return self.location  # Method to get the location of the item

    def setQuantity(self, quantity):
        self.quantity = quantity  # Method to set the quantity of the item

    def setPrice(self, price):
        self.price = price  # Method to set the price of the item

    def setLocation(self, location):
        self.location = location  # Method to set the location of the item


class Mammal(Animal):
    def __init__(self, name):
        # Initialize attributes for mammals, inheriting from Animal
        super().__init__(name)
        self.warmBlooded = True  # Mammals are warm-blooded
        self.fur = True  # Mammals typically have fur

    def getWarmBlooded(self):
        return self.warmBlooded  # Method to check if the mammal is warm-blooded

    def setWarmBlooded(self, warmBlooded):
        self.warmBlooded = warmBlooded  # Method to set if the mammal is warm-blooded

    def getFur(self):
        return self.fur  # Method to check if the mammal has fur

    def setFur(self, fur):
        self.fur = fur  # Method to set if the mammal has fur


class Reptile(Animal):
    def __init__(self, name):
        # Initialize attributes for reptiles, inheriting from Animal
        super().__init__(name)
        self.coldBlooded = True  # Reptiles are cold-blooded
        self.food = "Live"  # Reptiles typically eat live prey

    def isColdBlooded(self):
        return self.coldBlooded  # Method to check if the reptile is cold-blooded

    def getFood(self):
        return self.food  # Method to get the food type of the reptile

    def setFood(self, food):
        self.food = food  # Method to set the food type of the reptile


class Canine(Mammal):
    def __init__(self, name, size, weight, color):
        # Initialize attributes for canines, inheriting from Mammal
        super().__init__(name)
        self.size = size  # Size of the canine
        self.weight = weight  # Weight of the canine
        self.color = color  # Color of the canine

    def bark(self, count):
        # Method for the canine to bark a certain number of times
        for _ in range(count):
            print("Woof!")

    def getSize(self):
        return self.size  # Method to get the size of the canine

    def setSize(self, size):
        self.size = size  # Method to set the size of the canine

    def getWeight(self):
        return self.weight  # Method to get the weight of the canine

    def setWeight(self, weight):
        self.weight = weight  # Method to set the weight of the canine

    def getColor(self):
        return self.color  # Method to get the color of the canine

    def setColor(self, color):
        self.color = color  # Method to set the color of the canine


class Feline(Mammal):
    def __init__(self, name, size, weight, color):
        # Initialize attributes for felines, inheriting from Mammal
        super().__init__(name)
        self.size = size  # Size of the feline
        self.weight = weight  # Weight of the feline
        self.color = color  # Color of the feline

    def purr(self, count):
        # Method for the feline to purr a certain number of times
        for _ in range(count):
            print("Purr...")

    def getSize(self):
        return self.size  # Method to get the size of the feline

    def setSize(self, size):
        self.size = size  # Method to set the size of the feline

    def getWeight(self):
        return self.weight  # Method to get the weight of the feline

    def setWeight(self, weight):
        self.weight = weight  # Method to set the weight of the feline

    def getColor(self):
        return self.color  # Method to get the color of the feline

    def setColor(self, color):
        self.color = color  # Method to set the color of the feline


class Snake(Reptile):
    def __init__(self, name, size, weight):
        # Initialize attributes for snakes, inheriting from Reptile
        super().__init__(name)
        self.size = size  # Size of the snake
        self.weight = weight  # Weight of the snake
        self.color = "Brown"  # Default color for snakes
        self.constrictor = False  # Default value for constrictor (not a constrictor)
        self.food = "Rodents"  # Default food for snakes

    def getSize(self):
        return self.size  # Method to get the size of the snake

    def setSize(self, size):
        self.size = size  # Method to set the size of the snake

    def getWeight(self):
        return self.weight  # Method to get the weight of the snake

class Lizard(Reptile):
    def __init__(self, name, size, weight):
        # Call the constructor of the parent class (Reptile)
        super().__init__(name)

        # Additional attributes specific to Lizards
        self.size = size
        self.weight = weight
        self.color = "Green"  # Default color for lizards
        self.habitat = "Forest"  # Default habitat for lizards
        self.frill = False  # Default value for frill (no frill)
        self.spikes = False  # Default value for spikes (no spikes)

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def hasFrill(self):
        return self.frill

    def setFrill(self, frill):
        self.frill = frill

    def hasSpikes(self):
        return self.spikes

    def setSpikes(self, spikes):
        self.spikes = spikes