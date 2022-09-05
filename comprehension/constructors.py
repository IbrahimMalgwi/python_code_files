listcomp = [num % 3for num in range(1, 10)]
setcomp = {num % 3for num in range(1, 10)}
dictcomp = {k: v for k, v in enumerate(range(11, 16), 1)}
genexp = (num for num in range(1, 6))

# print(type(listcomp), listcomp)
# print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
# print(type(genexp), genexp)
