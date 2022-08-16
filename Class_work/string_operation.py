# a = 'hello world'
b = 'ibrahim gana malgwi'
print(str.upper(b))
print(str.lower(b))
print(str.capitalize(b))
print(str.title(b))

name = "ibrahim gana malgwi"
q = "malgwi"
print(name.startswith(name))
print(q.endswith(q))

print(name.ljust(20))
print(name.rjust(20))

print(name.center(20))
print(name.center(20, '#'))

for i in range(1, 11):
    print('#' * i)

for i in range(1, 11):
    print(('#' * i).rjust(10))

for i in range(1, 11):
    print(('#' * i).center(10))

for i in range(1, 21, 2):
    print(('#' * i).center(20))

print(name.count('b'))
print(name.count('i'))
print(name.find('b'))
print(name.find('i'))
print(name.find('mal'))
print(name.find('mal', 2))
print(name.find('h', 2))
print(name.find('h', 3, 10))

print(name.index("g"))
print(name.index("g", ))

name1 = "   ibrahim gana malgwi"

print(name.rindex("a",))
print(name.index("a",))

print(name.replace('a', '@'))
print(name.replace('a', '@', 1))

print(name1.strip())
g,h, i = name1.split()
print(g)
print(h)
print(i)

binary = "1230120310010050123"

print(binary.replace('1', '*',).replace('0', '1').replace('*', '0'))

print(binary.translate(str.maketrans('012', '109' '3')))

my_str = "madam i'm adam"
print(reverseStr = my_str [: : -1])
