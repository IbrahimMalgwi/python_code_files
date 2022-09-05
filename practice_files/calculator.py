number1 = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
number2 = float(input("Enter the second number number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid Operator")
