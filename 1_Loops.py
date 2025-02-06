"""
Zion King
COMP163-004
2/25/24
in this program 2 of the users will be playing rock paper scissors using
the random number generator and loop through the amount of games played.
"""

import random
# Gets the seed from the user
input_seed = int(input("Seed: "))
random.seed(input_seed)

# Rock, Paper or scissors
choices = ["Rock", "Paper", "Scissors"]

player1 = input("Player 1 Name: ")
player2 = input("Player 2 Name: ")

# if the number of rounds are less than 1 than an Error is displayed
rounds_played = int(input("Enter Number of rounds: "))
while rounds_played < 1:
    print('Error')
print(f"{player1} vs {player2} for {rounds_played} rounds")

# Loop through the number of rounds to be played
for _ in range(rounds_played):
    player1_choice = random.choice(choices)
    player2_choice = random.choice(choices)

    print(f"{player1} chose {player1_choice}")
    print(f"{player2} chose {player2_choice}")
    # Check if both players chose the same option
    if player1_choice == player2_choice:
        print("Tie")
    else:
        # Check for all possible winning scenarios for player1
        if (player1_choice == "rock" and player2_choice == "scissors") or \
            (player1_choice == "paper" and player2_choice == "scissors") or \
            (player1_choice == "scissors" and player2_choice == "paper"):
            print(f"{player1} wins!")
        else:
            # If player1 didn't win, player2 wins
            print(f"{player2} wins!")








