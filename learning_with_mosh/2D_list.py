# 2D list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print 1 and 5 and 9

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

for row in matrix:
    for item in row:
        print(item)