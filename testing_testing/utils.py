import doctest

from testing_testing.exception import MyCustomException


# Assertion Test
def add_two(x, y):
    assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Only int or float can be added"
    assert x > 0 and y > 0, "Numbers cannot be negative"
    return x + y


# assert [1, 2, 3] == [1, 2, 3]
# print(add("2", "3"))


def add_list(lst):
    assert isinstance(lst, list), "Can only take list"
    return sum(lst)


# lst1 = (1, 2, 3)
# print(add_list(lst1))

# lst2 = [1, 2, 3]
# print(add_list(lst2))


# Doctest
def add(x, y):
    """
    add two numbers
    >>> add(5, 5)
    10
    >>> add(2, 6)
    8
    >>> add(2, "hi") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    if x > y:
        raise MyCustomException("Just fooling around")
    return x + y


print(add(5, 6))
if __name__ == "__main__":
    doctest.testmod(verbose=True)
