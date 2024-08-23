# Python number guessing game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guessses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a numbe between {lowest_num} and {highest_num}")

while is_running:   
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guessses += 1

        if guess not in range(lowest_num, highest_num + 1):
            print("This number is out of range")
            print(f"Select a numbe between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guessses}")
            is_running = False

    else:
       print("Invalid guess")
       print(f"Select a numbe between {lowest_num} and {highest_num}")