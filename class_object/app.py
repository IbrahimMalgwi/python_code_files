from Student import Student

student1 = Student("Mike", "Computer Science", 3.1, False)
student2 = Student("Kelichi", "Software Engineering", 4.3, False)

print(student1.gpa)
print(student2.gpa)

print(student1.on_honour_roll())
print(student2.on_honour_roll())