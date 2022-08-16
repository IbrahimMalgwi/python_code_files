import random

lst = list(range(1, 11))
# print(lst)
# This suffle the list
# random.shuffle(lst)

# print(lst)
# this add a list as an element instead of elements of the array to the end of the ist
lst.append([20, 30, 40])

# this add as and elements of the array
lst.extend([22, 33, 44])

# This also extend to the list
lst += [50, 60, 70]

# This insert 70 at index 0
lst.insert(0, 78)

# This remove the last element in the list
last_item = lst.pop()

# remove elements at an index
item_at_index_0 = lst.pop(0)

# this remove a particular item
lst.remove(33)

# to remove multiple elemetents in a list
print("count", lst.count(8))

# to clear lst.clear()

lst.reverse()

s = "reverse a word"

# lst.sort(reverse=True)

# print(s[::-1])
# print(item_at_index_0)
# print(last_item)
# print(lst)

fruits = ["banana", "apple", "cucumber", "mango", "grape"]

fruits.sort(key=len())
print(fruits)

