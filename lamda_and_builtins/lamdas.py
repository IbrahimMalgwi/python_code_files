def operate(x, y, func):
    return func(x, y)


add = lambda a, b: a + b
print(add(10, 9))
print(operate(2, 3, add))
print(operate(2, 3, lambda a, b: a + b))
print(operate(2, 3, lambda a, b: b - a))
print(operate(2, 3, lambda a, b: a * b))
