def perfect_square(number):
    """
    Program return the square  iof a number and determine if the last number in the square the same as the number
    :param number:
    :return:
    """

    number_string = str(number)
    number_length = len(number_string)
    number_square = number * number
    number_square_string = str(number_square)
    count_check = number_square_string[-number_length]

    if number_string == count_check:
        print(number, "Is a Perfect Square")
    else:
        print(number, "Is not a Perfect Square")
        return " "


print(perfect_square(7))