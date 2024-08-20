# Python calculator

import re

# get user input
usr_input = input(">> ").strip()


#print(usr_input)


# validate user input
    # create 2 lists and populate the 1st one with values the 2nd with algebra operators
    # 1st input: 1+1
    # 2nd input: 1 + 1 
    # dziel na znakach typu +, *, -, / 
    # create set of  avaliable algebra operators
avaliable_operators = {'+', '-', '*', '/'}
operators = []
values = []

def valid_input(usr_input):
    # use regex to determinate if the user provided possible equation



for char in usr_input:
    if char.isdigit():
        values.append(char)
    elif char in avaliable_operators:
        operators.append(char)


print(values)
print(operators)

def tokenize(usr_input):
    token = re.findall('\d+ | [+\-/\*]')






    # use regex to determine if the input is correct
    # if the user provides the expression with some errors 
    # provide the guidance on how to correct it so:
    # .. 1 + --> should ouput: 1 + _ the 2nd argument is missing


