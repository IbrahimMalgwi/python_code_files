import string

word = input("What would you like to encode: ")
key = int(input("Your key? "))

lower_letters = string.ascii_lowercase
upper_letter = string.ascii_uppercase

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_letter_code = upper_letter[key:] + upper_letter[:key]

letters = lower_letters + upper_letter
letters_code = lower_letters_code + upper_letter_code

encoded_word = word.translate(str.maketrans(letters, letters_code))

print(word)
print(encoded_word)

print("======================================================")

decode_word = encoded_word.translate(str.maketrans(letters_code, letters))

print(decode_word)

for i in range(1, 27):
    lower_letters_code = lower_letters[i:] + lower_letters[:i]
    upper_letter_code = upper_letter[i:] + upper_letter[:i]

    letters = lower_letters + upper_letter
    letters_code = lower_letters_code + upper_letter_code
    print(encoded_word.translate(str.maketrans(letters_code, letters)))