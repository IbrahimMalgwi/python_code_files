# Printing letters with *

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print('x' * x_count)

print("===============================")

# Methode 2
numbers = [2, 2, 2, 2, 7]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x';
    print(output)
