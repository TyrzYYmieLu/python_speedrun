import re

def main():
    user_input = input(">> ").strip()

    if is_valid(user_input):
        number, art_operator = tokenize(user_input)
        result = calculate(number, art_operator)
        print(result)
    else:
        print("Invalid character")
        print("Usage: [value] [operator] [value] ... (+, -, *, /, ^, % and numbers 0-9)")

def is_valid(user_input):
    # Use regex to match valid characters and structure
    pattern = re.compile(r"^[\d\+\-\*\/\^\%\(\) ]+$")
    return bool(pattern.match(user_input))

def calculate(numbers, operators):
    # This implementation assumes a simple binary operator handling
    if not numbers or not operators:
        return "Invalid input"

    # Convert number list from string to integers
    numbers = list(map(int, numbers))
    
    while len(operators) > 0:
        # Simplified calculation assuming only one operator at a time
        num1 = numbers.pop(0)
        num2 = numbers.pop(0)
        op = operators.pop(0)
        
        if op == "+":
            value = num1 + num2
        elif op == "-":
            value = num1 - num2
        elif op == "*":
            value = num1 * num2
        elif op == "/":
            value = num1 // num2  # Integer division
        elif op == "^":
            value = num1 ** num2
        elif op == "%":
            value = num1 % num2
        else:
            return "Unsupported operator"
        
        # Insert the result back into the numbers list
        numbers.insert(0, value)

    return numbers[0] if numbers else "Invalid calculation"

def tokenize(user_input):
    # Tokenize numbers and operators
    tokens = re.findall(r'\d+|[\+\-\*\/\^\%]', user_input)
    number = []
    operator = []
    
    for token in tokens:
        if token.isdigit():
            number.append(token)
        else:
            operator.append(token)
    
    return number, operator

if __name__ == "__main__":
    main()
