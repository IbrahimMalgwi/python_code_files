
for i in range(1, 100):
    if i % 3 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz, Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

    # if not i / 3 == 0 and not i / 5 == 0:
    #     print(i)
    # elif i % 3 == 0:
    #     print("Fizz")
    # elif i % 5 == 0:
    #     print("Buzz")
    # elif i % 3 and i % 5:
    #     print("Fizz_Buzz")