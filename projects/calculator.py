# Python calculator



# use regex to determine if the input is correct
    # if the user provides the expression with some errors 
    # provide the guidance on how to correct it so:
    # .. 1 + --> should ouput: 1 + _ the 2nd argument is missing

import re


def valid_input(usr_input):
    # use regex to determinate if the user provided possible equation
    pattern = re.compile(r'^\d+(\s*[\+\-\*\/]\s*\d+)*$')
    return bool(pattern.match(usr_input))
    ...


def tokenize(usr_input):
    token = re.findall('\d+ | [+\-/\*]')
    ...


def main():

    usr_input = input(">> ").strip()

    if valid_input(usr_input):
        print("yes")


    # validate user input
    # create 2 lists and populate the 1st one with values the 2nd with algebra operators
    # 1st input: 1+1
    # 2nd input: 1 + 1 
    # dziel na znakach typu +, *, -, / 
    # create set of avaliable algebra operators
    avaliable_operators = {'+', '-', '*', '/'}
    operators = []
    values = []


    for char in usr_input:
        if char.isdigit():
            values.append(char)
        elif char in avaliable_operators:
            operators.append(char)


    print(values)
    print(operators)

if __name__ == "__main__":
    main()