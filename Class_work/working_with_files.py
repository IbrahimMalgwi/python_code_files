with open('temp_file.txt', mode='w', encoding='utf-8') as file_object:
    print(file_object.tell())
    file_object.write("Life is good with Banke\n")
    # file_object.seek(10)
    # print(file_object.tell())
    file_object.write("Life is good with Banke\n")
    file_object.writelines(['Life\n', 'is\n', 'bad\n', 'with\n', 'leken\n'])

with open('temp_file.txt', mode='r', encoding='utf-8') as file:
    for idx, line in enumerate(file.readlines(), start=1):
        print(f"{idx}. {line.upper()}")


