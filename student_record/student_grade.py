number_of_students = int(input("How many students are in your class? "))
number_of_subjects = int(input("How many subject do they do: "))
# score_of_subjects = int(input("Enter the Score of Each Subject: "))

students_names = [input("Enter Names of Student: ") for student_name in range(number_of_students)]
print(" ")
subjects = [input("Enter Names for Subjects: ") for subject_name in range(number_of_subjects)]
print(" ")
# scores = [input("Enter SCore for Subjects ") for score in range(score_of_subjects)]

print(f"f{subjects}")

print("The name of students are:", students_names)
print("The subject they offered: ", subjects)

students = [
    {
        'Student_name': 'Mike ',
        'Subjects': [{'English': 90, 'English': 80}],
        'Total': 170,
        'Average': 85
    }
]