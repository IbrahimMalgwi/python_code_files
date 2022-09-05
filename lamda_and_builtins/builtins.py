import builtins

# print(builtins.sum([1, 2, 3]))

# absolute value
# print(abs(1))

# for decimal place you give it a value
# print(round(56.67854, 2))
# take to significant figure
# print(round(56.67854, -1))

# sum function
arr = [1, 6, 4, 7, 2]
# print(sum(arr, 100))

letters = [['a'], ['b', 'c'], ['d'], ['e', 'f']]
# print(sum(letters, []))

# max and min
# print(max(1, 2, 3, 4, 5, 6, 7, ))

fruits = "apple pear cucumber mango grape melon".split()
# print(max(fruits))
# print(min(fruits))
# print(max(fruits, key=len))
# print(min(fruits, key=len))
# print(max(fruits, key=lambda x: x[-3]))


# zip

iterable1 = (1, 2, 3, 4)
iterable2 = ('hello', 'how', 'are', 'you')
# print(list(zip(iterable1, iterable2)))


# Sorted
# print(sorted('hello'))

# Map

lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, lst)))
print([x ** 2 for x in lst])

print(list(map(str.upper, fruits)))
print(list(map(lambda x: x.upper(), fruits)))

fruits.append('Agbado')
print(list(filter(str.istitle, fruits)))

print(list(filter(lambda x: not x.istitle(), fruits)))

print([x for x in fruits if not x.istitle()])
print([x.upper() for x in fruits if not x.istitle()])
