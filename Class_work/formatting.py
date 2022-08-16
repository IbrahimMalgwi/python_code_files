import math

minute = 5
arg = 'Argument'

s = f"Sorry is this the {5} minute {'ARGUMENT'}?"
print(s)

d = "Sorry is this the {} minute {}?".format(5, "ARGUMENT")
print(d)

print("{:>10} is {:.3f} years old".format("Bill", math.pi))

for i in range(1, 11):
    sym = '*' * i
    print(f'{sym:10}')
