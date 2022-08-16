# user_input = int(input("Enter number you want for multiplication table: "))
#
# # user_input = 2
# table = range(1, 13)
# for x in table:
#     result = user_input * x
#     print(user_input, " * ", x, " = ", result)


# Method two
for row in range(2, 13, 1):
    for col in range(1, 13, 1):
        print(row, "*", col, "=", row * col, end='     ')
    print()


    # for space in range(1, 15):
    #     print("=", end='')

#     using while loop
#
# user_number = int(input("Enter number for table: "))
#
# number = 1
#
# while number <= 12:
#     result = user_number * number
#     print(user_number, " * ", number, " = ", result)
#     number = number + 1
