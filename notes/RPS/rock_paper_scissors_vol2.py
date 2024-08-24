import random
options = ({0: "rock", 1: "paper", 2: "scissors"})
pc = random.choice(options)
usr = input("Pick one: rock, paper, scissors: ")


for value, option in options.items():
    print(value)
    print(option)

'''
if compare % 3 == 0:
    print("It's a tie!")
elif (compare % 3 + 1) % 2 == 0:
    print("You win!")
elif (compare % 3) % 2 == 0:
    print("You lose")'''