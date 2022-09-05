from collections import defaultdict


def doit(a_list) -> dict:
    result = defaultdict(list)
    for item in list(a_list).items():
        result[item[1]].append(item[0])
        return dict(result)


# print(doit())


def func(lst=None):
    if lst is None:
        lst = []
    lst.append(2)
    return lst

print(func())
print(func([1,2,3]))
print(func())
print(func())
