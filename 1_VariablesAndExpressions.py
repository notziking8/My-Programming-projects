"""
Zion King
1/31/24
Comp 163-004
In this program, I have been tasked to find out how many pizzas to order
if a certain amount of people attend a pizza party, so that there will be enough for everyone attending.
 and finally calculate the total cost.
"""
import math
# The number of people going to the party.
num_People = int(input())
pizza_Cost = 14.95

# Computing the total number of pizza to be ordered,
# use the ceil() function to round up the result to the nearest whole number.
slices_Needed = num_People * 2
num_Pizzas = math.ceil(slices_Needed / 12)

# Calculated cost of the pizza.
total_cost = num_Pizzas * pizza_Cost

# The print statements displays the number of people, number of pizzas being ordered.
# and the total cost of the pizzas, formatted as a floating point value.
# with two decimal places using the f-string syntax (total_pizza_cost:.2f).
print("Number of people attending the party:",  num_People)
print('People:', num_People)
print('Pizzas(s):', num_Pizzas)
print(f'Cost for {num_Pizzas} pizza(s): ${total_cost:.2f}')
