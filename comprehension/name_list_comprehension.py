names = ['bimpe', 'Banke', 'abimbola', 'James', 'Kelechi', 'Olaleka', 'Racheal']
my_name = []
for name in names:
    if name.istitle():
        my_name.append(name)

print(my_name)

# another method
surnames = ['bimpe', 'Banke', 'abimbola', 'James', 'Kelechi', 'Olaleka', 'Racheal']
my_surnames = [name for name in surnames if name.istitle()]
print(my_surnames)

# Another method
input_name = [input(f"{i + 1}, Name? ") for i in range(5)]
print(input_name)

# Another method
number_of_times = int(input("How many times will you like to enter name: "))
input_name2 = [input(f"{i + 1}, Name? ") for i in range(number_of_times)]
print(input_name2)

# using two  for loops
x_and_y = [(x, y) for x in range (1, 6) for y in range(1, 6)]
print(x_and_y)

x_and_y = [(x, y) if x > y else (y, x) for x in range (1, 6) for y in range(1, 6)]
print(x_and_y)

x_and_y = [(x ** 2 if x % 2 == 0 else x, y) for x in range (1, 6) for y in range(1, 6)]
print(x_and_y)