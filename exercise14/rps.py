# Rock Paper scissors game
import random
import os

print("BARRIE'S ROCK, PAPER SCISSORS GAME")
name = input("Please enter your name:\n")
print("Hello", name, "Let's get started.")
print("Good Luck!")
                                    
# List of available options to choose
choices = ["rock", "paper", "scissors"]
def determine_winner(player, opponent):
    # Check if it's a tie
    if player == opponent:
        return "It's a tie"
    # Check if the player won
    elif ((player == "rock" and opponent == "scissors") or
          (player == "paper" and opponent == "rock") or
          (player == "scissors" and opponent == "paper")):
        return "YOU WIN!"
    # If the player lost
    else:
        return "YOU LOSE!"

# Whether the game is in play or not using boolean operator.
playing, invalid = True, False
# In play loop
while playing:
    if not invalid:
        print("Please choose rock, paper or scissors: ")
    else:
        print("Invalid input. Please type rock, paper or scissors")
        invalid = False
    player_choice = input().lower().strip()
    computer = random.choice(choices)

    if player_choice in choices:
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer}")
        print(determine_winner(player_choice, computer))

    else:
        invalid = True

    # Does the player want to play again
    if playing and not invalid:
        replay = input("Do you want to play again? "
                       "\"y\" to replay\nHit Enter to quit\n").lower().strip()
        playing = replay == "y"

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

print("Thanks for playing!")





