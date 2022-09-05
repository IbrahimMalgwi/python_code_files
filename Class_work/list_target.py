numbers = [3, -1, 5, 4]
target = 9


def two_sum(numbers: list, target: int) -> int:
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j
    return [-1, -1]


print(two_sum(numbers, target))

arr = [3, -1, 5, 4]
target = 8


def sum_two(arr: list, target: int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


print(sum_two(arr, target))
