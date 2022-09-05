def count_element(list, x):
    count = 0
    for element in list:
        if (element == x):
            count = count + 1
    return count


# Driver Code

list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, count_element(list, x)))


# dict((i, a.count(i)) for i in a)