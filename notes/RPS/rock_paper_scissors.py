# Rock, paper, scissors program
import random

options = ("rock", "paper", "scissors")
options = {0: "rock", 1: "paper", 2: "scissors"}

pc = random.choice(options)

my = input("Choose your option rock paper scissors: ")

if my == "paper":
    if pc == "scissors":
        print("you loose")
    elif pc == "rock":
        print("you win")
    else:
        print("you tie")
if my == "rock":
    if pc == "scissors":
        print("you win")
    elif pc == "rock":
        print("you tie")
    else:
        print("you loose")

if my == "scissors":
    if pc == "scissors":
        print("you tie")
    elif pc == "rock":
        print("you loose")
    else:
        print("you win")