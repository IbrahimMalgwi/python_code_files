total = 0
counter = 0

grade = input("Enter grade ")
grade = int(grade)

while grade != -1:
    total = total + grade
    counter = counter + 1
    grade = input("Enter -1 to end ")
    grade = int(grade)

if counter != 0:
    average = float (total) / counter
    print("Class average is ", average)
else:
    print("No grade was entered ")