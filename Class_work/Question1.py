myList = [1, 2, 3, 4, 5]


def largest_number(myList: int):
    largest = myList[0]
    for i in myList:
        if i > largest:
            largest = i

    return largest


print(largest_number(myList))


def reverse(myList):
    reverse = myList[::-1]
    return reverse


print(reverse(myList))


def element_contains(myList, number):
    for i in myList:
        if i == number:
            return True

    return False


print(element_contains(myList, 5))


def odd_position_values(myList):
    values = []
    for i in range(0,len(myList)):
        if i % 2 != 0:
            values.append(myList[i])
    return values


print(odd_position_values(myList))


def even_position_values(myList):
    values = []
    for i in range(0,len(myList)):
        if i % 2 == 0:
            values.append(myList[i])
    return values


print(even_position_values(myList))


def isPalindrome(s):
    # Calling reverse function
    if len(s) <= 1:
        return True
    if s[0] == s[len(s) - 1]:
        return isPalindrome(s[1:len(s) - 1])
    else:
        return False

print()

