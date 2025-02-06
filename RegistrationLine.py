"""
Zion King
4/30/24
Comp 163-004
In this program I am attempting to dentify and quantify the smallest areas of frustration
within the registration line by determining the number of Aggies in the line ('n') and assigns each Aggie an
integer representing their position Then calculates each Aggie's frustration
"""
def smallest_area_of_frustration(n, Aggies_position):
    # Sort the positions
    Aggies_position.sort()

    area = float('inf')

    # Iterates through the positions, excluding the first and last
    for i in range(1, n - 1):
        left_neighbor = Aggies_position[i - 1]
        right_neighbor = Aggies_position[i + 1]
        current_position = Aggies_position[i]

        # Calculates the left and right areas of frustration
        left_area = (current_position - left_neighbor) / 2
        right_area = (right_neighbor - current_position) / 2

        # Updates the minimum area if needed
        area = min(area, left_area + right_area)

    return area


n = int(input("Number of Aggies in the Dowdy registration line: "))
Aggies_position = list(map(int, input("Positions of Aggies in the line: ").split()))

print("Smallest area of frustration: {:.1f}".format(smallest_area_of_frustration(n, Aggies_position)))

