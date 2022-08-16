total = 0
counter = 0

while counter <= 10:
    grade = input("Enter grade ")
    grade = int(grade)
    total = total + grade
    counter = counter + 1

average = total / 10
print("class average is: ", average)