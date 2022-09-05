def exponent(base_number, power):
    result = 1
    for index in range(power):
        result = result * base_number
    return result

print(exponent(3, 4))