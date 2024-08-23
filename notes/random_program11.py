import random

low = 1
high = 100

# provides random intiger 
number = random.randint(low, high)
print(number)

# random floating point number between 0-1
float_number = random.random()
print(float_number)

# radom choice from option
options = ("rock", "paper", "scissors")
choice = random.choice(options)
print(choice)

# shuffle module
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
random.shuffle(cards)
print(cards)