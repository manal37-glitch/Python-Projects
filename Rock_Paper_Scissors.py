import random

# Defining constants for the moves
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

# Put all the moves in a list for easy access
choices = [ROCK, PAPER, SCISSORS]

# Define winning and losing combinations as lists of pairs
win = [[ROCK, SCISSORS], [PAPER, ROCK], [SCISSORS, PAPER]]
lose = [[SCISSORS, ROCK], [ROCK, PAPER], [PAPER, SCISSORS]]

# Function to generate a random move for the computer
def get_computer_move():
    move = random.choice(choices)  # Randomly select one of the available moves
    return move

# Function to determine the winner
def find_winner(user_move, computer_move):
    if [user_move, computer_move] in win:
        return 1  # User wins
    elif [user_move, computer_move] in lose:
        return -1  # Computer wins
    return 0  # It's a tie

# Main game loop
print("Welcome to Rock, Paper, Scissors! =)")

while True:  # Loop until the user decides to quit
    choice = input("Are you ready to play? (Yes/No): ").strip().lower()
    
    if 'yes' in choice:
        # Get the computer's move
        computer_move = get_computer_move()

        while True:  # Loop to ensure valid user input
            move = input("Select a move ('r' for rock / 'p' for paper / 's' for scissors): ").strip().lower()

            # Validate the input and map it to the corresponding move
            if move == 'r':
                user_move = ROCK
            elif move == 'p':
                user_move = PAPER
            elif move == 's':
                user_move = SCISSORS
            else:
                print("Invalid input. Please try again.")  # Handle invalid inputs
                continue  # Prompt the user again

            print(f"Your move: {user_move}")
            print(f"Computer's move: {computer_move}")

            # Determine the result
            result = find_winner(user_move, computer_move)
            if result == 1:
                print("Congratulations, you won!")
            elif result == -1:
                print("Computer won! Better luck next time.")
            else:
                print("It's a tie!")
            break  # Exit the inner loop after a valid round

    elif 'no' in choice:
        print("Exiting the game. See you next time!")
        break  # Exit the game loop

    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")  # Handle invalid inputs for starting the game
    print()
