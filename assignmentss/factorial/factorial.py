import math


# number = int(input("Please Enter number: "))
#
# fact = 1
#
# for i in range(1, number + 1):
#     fact = fact * i
# print(fact)
# print("The factorial of %d = %d" %(number, fact))

# Example 2

# number = int(input("Enter a number: "))
#
# factorial = 1
# if number < 0:
#     print("Factorial does not exist for negative numbers")
# elif number == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, number + 1):
#         factorial = factorial * i
#         print("The factorial of ", number, "is", factorial)


# example 2
# def fact(n):
#     return 1 if (n == 1 or n == 0) else n * fact(n - 1)
# num = 5
# print("Factorial of", num, "is", fact(num))


# example 3
def fact(n):
    return math.factorial(n)

number = int(input("Enter the number: "))
factorial = fact(number)
print("Factorial of ", number, "is", factorial)
