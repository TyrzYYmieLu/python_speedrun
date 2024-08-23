def main():
    # make the cursor blink
    user_input = input(">> ")
    #print(is_valid(user_input))

    if is_valid(user_input):
        number, operator = tokenize(user_input)
        #calculate(number, operator)
        print(calculate(number, operator))
    else:
        print("Invalid character")
        print("Usage: [value] [operator] [value] ... (+, -, *, /, ^, % and number 0-9)")


def is_valid(user_input):
    # allowed characters: - + / * () ^ % 0-9
    # allowed input:
    # 1+2+          4*(2/2)^3
    allowed_char = {"-", "+", "/", "*", "(", ")", "^", "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "}
    for char in user_input:
        if char not in allowed_char:
            return False
    return True


def calculate(numbers, operators):
    if len(operators) != len(numbers) - 1:
        raise ValueError("The number of operators should be one less than the number of numbers.")

    result = numbers[0]
    
    for i in range(1, len(numbers)):
        if operators[i-1] == "+":
            result += numbers[i]
        elif operators[i-1] == "-":
            result -= numbers[i]
        elif operators[i-1] == "*":
            result *= numbers[i]
        elif operators[i-1] == "/":
            result /= numbers[i]
        elif operators[i-1] == "^":
            result **= numbers[i]
        elif operators[i-1] == "%":
            result %= numbers[i]
        else:
            raise ValueError(f"Unsupported operator: {operators[i-1]}")

    return result



def tokenize(user_input):
    
    
    operator = []
    number = []
    for char in user_input:
        if char in {" ", "(", ")"}:
            continue
        elif char in {"+", "-", "*", "/", "^", "%"}:
            operator.append(char)
        else:
            number.append(char)

    return number, operator



if __name__ == "__main__":
    main()  