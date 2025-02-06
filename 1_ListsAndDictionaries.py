"""
Zion King
COMP 163-004
3/24/24
In this program I am going to be managing player information for a soccer team. I will be able to
 add, remove, update player ratings and output the roster.
"""

# Prints the Menu options
def print_menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

# Adds players to the roster
def add_player(roster):
    jersey_number = int(input("Enter a player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    roster[jersey_number] = rating

# Removes players from the roster
def remove_player(roster):
    jersey_number = int(input("Enter player's jersey number to remove: "))
    if jersey_number in roster:
        del roster[jersey_number]
        print("Player removed successfully.")
    else:
        print("Player not found.")

# Updates Players rating
def update_player_rating(roster):
    jersey_number = int(input("Enter player's jersey number to update rating: "))
    if jersey_number in roster:
        rating = int(input("Enter new rating: "))
        roster[jersey_number] = rating
        print("Player rating updated successfully.")
    else:
        print("Player not found.")


def output_players_above_rating(roster):
    rating_threshold = int(input("Enter rating threshold: "))
    print("Players above rating", rating_threshold)
    for jersey_number, rating in roster.items():
        if rating > rating_threshold:
            print("Jersey number:", jersey_number, "- Rating:", rating)

# Function to output the entire roster
def output_roster(roster):
    print("\nROSTER")
    for jersey_number, rating in sorted(roster.items()):
        print("Jersey number:", jersey_number, ", Rating:", rating)

# Function to print the initial roster
def print_initial_roster(roster):
    print("\nInitial Roster:")
    if roster:
        for jersey_number in sorted(roster.keys()):
            print("Jersey number:", jersey_number, ", Rating:", roster[jersey_number])
    else:
        print("Roster is empty.")
# Main Function
def main():
    roster = {}
    choice = ''

    while choice != 'q':
        print_menu()
        choice = input("Choose an option: ")

        if choice == 'a':
            add_player(roster)
        elif choice == 'd':
            remove_player(roster)
        elif choice == 'u':
            update_player_rating(roster)
        elif choice == 'r':
            output_players_above_rating(roster)
        elif choice == 'o':
            output_roster(roster)

main()