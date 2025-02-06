"""
Zion King
COMP 163 -004
3/29/24
in this Program, I will be Developers use UML to communicate how
Classes are to be constructed. In this Example I will use a car as an example
getting all the attributes like miles, miles forward, miles in reversed and ext.

"""
# Class with desired car functions: drive, reverse, honkHorn and report
class SimpleCar:
    def __init__(self):
        self.miles_driven = 0

    def drive(self, miles):
        print(f"Driving forward {miles} miles")
        self.miles_driven += miles

    def reverse(self, miles):
        print(f"Driving in reverse {miles} miles")
        self.miles_driven -= miles

    def honkHorn(self):
        print("Beep beep")

    def report(self):
        print(f"Car has driven: {self.miles_driven} miles")


# Taking input from the user
miles_forward = int(input("Enter miles driven forward: "))
miles_reverse = int(input("Enter miles driven in reverse: "))

# Creating a SimpleCar object
car = SimpleCar()

# Perform operations on the car
car.drive(miles_forward)
car.reverse(miles_reverse)
car.honkHorn()
car.report()
