word: str = str(input("Enter sentence in camel casa: "))
count = 1

for element in range(0, len(word)):
    if word[element].isupper():
        count += 1
print("We have", count, "words in the sentence ")
