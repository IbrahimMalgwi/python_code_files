from functools import reduce
from math import prod

list = [1, 2, 3, 4, 5]
fruits = "apple pear cucumber mango grape melon"


def reduce_func(acc, item):
    print(f"acc-> {acc} <> item -> {item}")
    return acc + item


print("\n############### reduce ###############\n")
# Print(reduce(lambda acc, item: acc + item, list))
print(list)
print(reduce(reduce_func, list, 100))
print(prod(list, start=100))
print(reduce(lambda acc, item: acc if acc > item else item, list))
print(max(list))

