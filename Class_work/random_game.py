import random

number = random.randint(0, 10)
i = 0
while i <= 3:
    user_number = int(input("Enter number: "))
    if user_number < number:
        print("too low")
    elif user_number > number:
        print("Too high")
    elif user_number != number:
        print("Last chance")
    elif user_number == number:
        print("You are right")
    else:
        print("Try again")
    i += 1
