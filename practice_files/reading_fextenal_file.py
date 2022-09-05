employee_file = open("name.txt", "r")  # Read from the file
# employee_file = open("name.txt", "w") # Write to change and write new and exisit information
# employee_file = open("name.txt", "a") # cannot change the file but add to the end of the file
# employee_file = open("name.txt", "r+") # you can read and write on the file

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines())
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)
    
employee_file.close()
