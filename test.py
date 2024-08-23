import re

def main():
    while True:
        user_input = input(">> ")
        if user_input.lower() in {"exit", "quit"}:
            break

        try:
            tokens = tokenize(user_input)
            if validate_tokens(tokens):
                result = evaluate_expression(tokens)
                print(f"Result: {result}")
            else:
                print("Invalid input. Usage: [value] [operator] [value] ... (+, -, *, /, ^, %, ())")
        except Exception as e:
            print(f"Error: {e}")

def tokenize(user_input):
    # Use regex to tokenize the input properly, including handling of parentheses
    pattern = r'(\d+|\+|\-|\*|\/|\^|\%|\(|\))'
    tokens = re.findall(pattern, user_input.replace(" ", ""))
    return tokens

def validate_tokens(tokens):
    if not tokens:
        return False

    # Ensure that the sequence of tokens is valid
    allowed_operators = {"+", "-", "*", "/", "^", "%"}
    previous_was_operator = True
    open_parentheses = 0

    for token in tokens:
        if token.isdigit():
            previous_was_operator = False
        elif token in allowed_operators:
            if previous_was_operator:
                return False
            previous_was_operator = True
        elif token == '(':
            open_parentheses += 1
            previous_was_operator = True
        elif token == ')':
            if open_parentheses == 0 or previous_was_operator:
                return False
            open_parentheses -= 1
            previous_was_operator = False
        else:
            return False

    return open_parentheses == 0 and not previous_was_operator

def evaluate_expression(tokens):
    # Convert to postfix (Reverse Polish Notation) and evaluate
    postfix = infix_to_postfix(tokens)
    return evaluate_postfix(postfix)

def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 2}
    output = []
    operators = []

    for token in tokens:
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Pop the '('
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output

def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
            elif token == '%':
                stack.append(a % b)

    return stack[0]

# Testing functions to verify our logic

def test():
    assert tokenize("3 + 5") == ['3', '+', '5']
    assert tokenize("10 * (2 + 3)") == ['10', '*', '(', '2', '+', '3', ')']
    assert validate_tokens(['3', '+', '5']) == True
    assert validate_tokens(['+', '3', '5']) == False
    assert validate_tokens(['(', '3', '+', '5', ')', '*', '2']) == True
    assert validate_tokens(['(', '3', '+', ')']) == False
    assert evaluate_expression(['3', '+', '5']) == 8
    assert evaluate_expression(['10', '*', '2', '+', '3']) == 23
    assert evaluate_expression(['10', '*', '(', '2', '+', '3', ')']) == 50
    assert evaluate_expression(['(', '3', '+', '4', ')', '*', '5']) == 35
    print("All tests passed!")

if __name__ == "__main__":
    test()  # Run tests before the main program
    main()
