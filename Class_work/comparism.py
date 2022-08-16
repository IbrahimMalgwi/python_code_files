num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))


def square(num1, num2: int):
    number_one = num1 * num1
    number_two = num2 * num2

    square_addition = number_one + number_two
    return square_addition

print(square(num1, num2))
