add = '+'
sub = '-'
mul = '*'
div = '/'

input_one = float(input("What is your first number?: "))
input_two = float(input("What is your second number?: "))

print("Choose an operator:")
print("1. + (Addition)")
print("2. - (Subtraction)")
print("3. * (Multiplication)")
print("4. / (Division)")

operator_choice = int(input("Enter your choice (1/2/3/4): "))

if operator_choice == 1:
    sign = add
elif operator_choice == 2:
    sign = sub
elif operator_choice == 3:
    sign = mul
elif operator_choice == 4:
    sign = div
else:
    print("Invalid operator choice")
    exit()

if sign == add:
    print(input_one + input_two)
elif sign == sub:
    print(input_one - input_two)
elif sign == mul:
    print(input_one * input_two)
elif sign == div:
    if input_two != 0:
        print(input_one / input_two)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("No valid operator seen")
