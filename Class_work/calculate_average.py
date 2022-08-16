
limit_str = input("Range is from 1 to your input: ")

limit_int = int(limit_str)
count_int = 1
sum_int = 0
while count_int <= limit_int:
    sum_int = sum_int + count_int
    count_int = count_int + 1
average_float = sum_int / (count_int - 1)
print("Average sum of integer from 1 to ", limit_str, "is", average_float)