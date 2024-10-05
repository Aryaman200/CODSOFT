import random
import time

# Instructions for the game
print('Welcome to the ROCK, PAPER, SCISSORS game!\n')
print('Rules of the game:')
print('1. Rock vs Paper -> Paper wins')
print('2. Rock vs Scissors -> Rock wins')
print('3. Paper vs Scissors -> Scissors wins\n')

# Mapping choices to names
choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

# Initialize score tracking
user_score = 0
computer_score = 0
draw_count = 0

def get_winner(player, computer):
    """Determine the winner between player and computer."""
    if player == computer:
        return "DRAW"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return "USER"
    else:
        return "COMPUTER"

while True:
    # Prompting user for choice input
    print("Choose your option: \n 1 - Rock \n 2 - Paper \n 3 - Scissors")
    
    # Validating input
    try:
        user_choice = int(input("Enter your choice (1/2/3): "))
        if user_choice not in [1, 2, 3]:
            raise ValueError("Invalid choice")
    except ValueError:
        print("Please enter a valid option (1/2/3).\n")
        continue

    # User's choice
    user_choice_name = choices[user_choice]
    print(f"\nYou chose: {user_choice_name}")

    # Computer's turn
    print("Computer is choosing...")
    time.sleep(1)
    computer_choice = random.randint(1, 3)
    computer_choice_name = choices[computer_choice]
    print(f"Computer chose: {computer_choice_name}")

    # Determine and announce the winner
    print(f"\n{user_choice_name} vs {computer_choice_name}")
    winner = get_winner(user_choice, computer_choice)

    time.sleep(1)
    if winner == "DRAW":
        print("<== It's a tie! ==>")
        draw_count += 1
    elif winner == "USER":
        print("<== You win! ==>")
        user_score += 1
    else:
        print("<== Computer wins! ==>")
        computer_score += 1

    # Ask if the user wants to play again
    play_again = input("\nWould you like to play again? (Y/N): ").lower()
    if play_again == 'n':
        print("\nGame over!")
        time.sleep(1)
        print(f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}\nTies: {draw_count}")
        time.sleep(1)
        print("Thanks for playing!")
        time.sleep(1)
        break

    print("\nStarting a new round...\n")
    time.sleep(1)
