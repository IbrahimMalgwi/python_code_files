def add(a: int, b: int) -> int:
    """
    this functions add numbers
    :param a:
    :param b:
    :return:
    """

    return a + b


# print(add.__name__)
# print(add.__doc__)

# function taking a function as parameter
def operate(x, y, func):
    return func(x, y)


def sub(x, y):
    return y - x


# print(operate(2, 3, add))
# print(operate(5, 8, sub))

# Function returning a function
def multiply(a):
    def by(b):
        return a * b

    return by


# multiply_by_five = multiply(5)
# print(multiply_by_five)
# print(multiply_by_five(5))


# Nested function
def multiply(a):
    def by(b):
        def another(c):
            return a * b * c

        return another
    return by


multiply_by_func = multiply(2)(5)
print(multiply_by_func(10))
