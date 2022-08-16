import math

# def add(first_number: int, second_number: int) -> int:
#     """
#     Adds two numbers
#     :param first_number: int
#     :param second_number: int
#     :return: int
#     """
#     return first_number + second_number
#
#
# print(add(2, 3))
# print(add.__doc__)
# print(add.__annotations__)
# print(add.__get__)

# =============================================
# def get_digit(number, position):
#     """
#     return digit at position in number, counting from right
#     :param number:
#     :param position:
#     :return:
#     """
#     return number // (10 ** position) % 10
#
#
# print(get_digit(3794, 2))

# =======================================
# def get_length(number: int) -> int:
#     """
#     return the length of the strength
#     :param number:
#     :return:
#     """
#     return len(str(number))
#
# print(get_length(4563))

# ========================================================
def get_length(number: int) -> int:
    import math
    return math.ceil(math.log10(number))

print(get_length(456))