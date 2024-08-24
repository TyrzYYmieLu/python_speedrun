import random

# Step 1: Define the graph
winning_moves = {
    'rock': ['scissors'],
    'scissors': ['paper'],
    'paper': ['rock']
}

# Step 2: Get user input and randomly choose for the program
user_move = input("Enter your move (rock, paper, scissors): ").lower()
program_move = random.choice(('rock', 'paper', 'scissors'))

# Step 3: Determine the outcome
if user_move == program_move:
    result = "It's a tie!"
elif program_move in winning_moves[user_move]:
    result = "You win!"
else:
    result = "You lose!"

# Step 4: Print the result
print(f"You chose {user_move}, and the program chose {program_move}. {result}")

