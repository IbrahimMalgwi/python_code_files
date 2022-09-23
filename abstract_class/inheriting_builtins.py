class DoubleIt(int):
    def __new__(cls, value):
        return super().__new__(cls, value * 2)


d = DoubleIt(4)
print(d)
d += 6
print(d)


class Mylist(list):
    def __setitem__(self, index, value):
        print("called")
        if index < 1:
            raise IndexError("Index can neither be negative or zero")
        super().__setitem__(index - 1, value)

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index can neither be negative nor zero")
        super().__getitem__(index - 1)


l = Mylist("hello")
print(l)
# l.append(1)
# print(l)

l[1] = 7
print(l)


class Mydict(dict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Can only take a string key")
        super().__setitem__(key, value)


mydicy = Mydict()
mydicy['1'] = 6
print(mydicy)

# print(type("")) == str