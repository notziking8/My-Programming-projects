"""
Zion King
2/6/24
Comp 163-004
In this program, I will be calculating the total cost it would be to paint a
wall based on the area of the wall and the amount of paint needed.
"""

import math
# Asks user for the height and width of the wall, and the cost of the paint.
wall_Height = int(input())
wall_Width = int(input())
cost_to_paint = float(input())

# Calculates the wall's area and the paint needed
# I used the ceil() function to round the paint needed to the nearest whole number
wall_Area = wall_Width * wall_Height
paint_Needed = wall_Area / 350
cans_Needed = math.ceil(paint_Needed)

# Calculates the cost of the paint, sales tax and the cost of everything.
paint_Cost = cans_Needed * cost_to_paint
sales_Tax = paint_Cost * 0.07
total_cost = paint_Cost + sales_Tax

print("What is the height of the wall :", wall_Height)
print("What is the width of the wall :", wall_Width)
print("What is the cost of a bucket of paint :", cost_to_paint)

# Outputs all needed variables and rounding them to there correct decimal place
print(f'Wall area: {wall_Area:.1f} sq ft')
print(f'Paint needed: {paint_Needed:.3f} gallons')
print('Cans needed:', cans_Needed, 'can(s)')
print(f'Paint cost: ${paint_Cost:.2f}')
print(f'Sales tax: ${sales_Tax:.2f}')
print(f'Total cost: ${total_cost:.2f}')


