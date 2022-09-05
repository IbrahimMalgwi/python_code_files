# this how to square a range
square = []
for i in range (1, 11):
    square.append(i ** 2)
print(square)

# this is how to get a range
cont = []
for i in range(1, 11):
    cont.append(i)
print(cont)

# comprehension
container1 = [i for i in range(1, 11)]
print(container1)

# comprehension
container = [i ** 2 for i in range(1, 11)]
print(container)

# Even number
even_numbers = [even for even in range(1, 11) if even % 2 == 0]
print(even_numbers)

# suqrae even and cube odd

even_square_odd_cube_numbers = [num ** 2 if num % 2 == 0 else num ** 3  for num in range(1, 11)]
print(even_square_odd_cube_numbers)