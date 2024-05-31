def calculate_equation(equation):
    # Tokenize the equation
    tokens = []
    current_number = ""
    for char in equation:
        if char.isspace():
            continue
        elif char.isdigit() or char == ".":
            current_number += char
        else:
            if current_number:
                tokens.append(float(current_number))
                current_number = ""
            tokens.append(char)
    if current_number:
        tokens.append(float(current_number))

    # Evaluate the equation
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    values_stack = []
    operators_stack = []
    for token in tokens:
        if token in operators:
            operators_stack.append(token)
        else:
            values_stack.append(token)
            while len(values_stack) >= 2 and operators_stack:
                operator = operators_stack.pop()
                y = values_stack.pop()
                x = values_stack.pop()
                result = operators[operator](x, y)
                values_stack.append(result)

    return values_stack[0]

input_string = input("Enter your equation (e.g., (10 + 1 / 100) * 3): ")
result = calculate_equation(input_string)
print(result)
