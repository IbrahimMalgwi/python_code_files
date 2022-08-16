# Program to fine largest number

numbers = [3, 6, 2, 8, 4, 10]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)
