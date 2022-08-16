numbers = [2, 6, 7, 12, 60, 5, 50, 30, 33, 5, 7, 8, 3, 45, 5, 8, 45, 7, 6, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)