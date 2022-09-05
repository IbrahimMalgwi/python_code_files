import itertools


# num = int(input("Enter a number: "))
# num1 = int(input("Enter a number: "))
#
# match num:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case _:
#         print("Don't know you")
#
# match num1:
#     case _ as x if 1 <= x <= 10:
#         print(x)
#     case 30 | 40 | 50:
#         print(2)
#     case _:
#         print("Don't know you")
#
# list = [20, 13, 16]
#
# match list:
#     case [i1, i2, i3]:
#         print(i3, i2, i1)
#     case _:
#         print("Nothing matched")
#
# list1 = [20, [13, 5], "good"]
#
# match list1:
#     case [i1, i2, i3]:
#         print(i3, i2, i1)
#     case [a, [b, c], d]:
#         print(a, b, c, d)
#     case _:
#         print("Nothing matched")
#
# d = {
#     "name": "Hadiza",
#     "age": 18,
#     "is_swit": True
# }
#
# match d:
#     case {"name": str(name), "age": int(age)}:
#         print(name, age)
#     case _:
#         print("nothing to match")
#
#
# def fizzbuzz(num):
#     three = num % 3
#     five = num % 5
#     match (three, five):
#         case (0, 0):
#             return "FIZZBUZZ"
#         case (0, _):
#             return "FIZZ"
#         case (_, 0):
#             return "BUZZ"
#         case _:
#             return num
#
#
# for i in range(1, 101):
#     print(fizzbuzz(i))


def summing_list(list_: list[int]) -> int:
    match list_:
        case []:
            return 0
        case [int(first_value), *another_list]:
            return first_value + summing_list(another_list)
        case _:
            print("Can only accept an int")
            return None


print(summing_list([1, 2, 3, 4, 5]))
print(list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0)))
