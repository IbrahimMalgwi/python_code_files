lst = ['r', 'i', 'n', 'g', 'i', 'n', 'g']

def find(my_list, value):
    index = 0
    for element in my_list:
        if element == value:
            index += 1
    return index