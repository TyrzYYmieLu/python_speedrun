# weight conversion program
# user can input sentance
# input: convert 1kg to lbs
# output: 1kg is 2.2 lbs | in ascii art using cowsay

# fucntion that validates user input
# function taht converts units
# in main use cowsay to anwser the question
# use cowsay as hello screen something like this:
# cowsay: what would you like to convert??? or use 
# some quotes generator or some list of quotes at the start of the program

import subprocess


def main():

    # Run the 'fortune' command and capture its output
    fortune = subprocess.run(["fortune"], capture_output=True, text=True)

    # Pass the output of 'fortune' to 'cowsay'
    cowsay = subprocess.run(["cowsay"], input=fortune.stdout, text=True)

    # Print the result (which is what cowsay would print to the terminal)
    #print(cowsay.stdout)



    usr_input = input("\n\nUnit conversion: ").strip()
    is_valid(usr_input)
    #print(usr_input.split())

    # validate user input 
   # if is_valid():
    

def is_valid(usr_input):
    list = usr_input.split()
    # [value] [unit] to [unit]
    # valid input:
        # 1kg to lbs
        # 1 kg in lbs 
        # 1                kg to lbs
        # how much 1kg is in lbs
        ## (maybe later) how much 1k is in lbs and in grams?
    # invalid input:
        # kg to lbs show message 1kg is 2.2 lbs or sth else 
        # 1kg to kg or just put some error message
        # 1 mass of the sun in lbs

    # supported units
    # kg, lbs, 


    # make python native and regex implementation
    # native python
    # 
    list_of_units = ['kg', 'lbs']
    print(list)

    if list[1] == 'kg' and list[-1] == 'lbs':
        sum = int(list[0]) * 2.20462
    elif list[1] == 'lbs' and list[-1] == 'kg':
        sum = int(list[0]) * 0.453592
    
    print(sum)


    #...



if __name__ == "__main__":
    main()