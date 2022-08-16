# Password checking method
def password_checker(password):
    """
    Method to check for password
    :param password:
    :return:
    """
    special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "|"]

    validation = True

    if len(password) < 6:
        print("Length of password should be at least 6 characters")
        validation = False

    if len(password) > 20:
        print("Length of password should not be more than 20 characters ")
        validation = False

    if not any(char.isdigit() for char in password):
        print("Password must have at least one digit")
        validation = False

    if not any(char.isupper() for char in password):
        print("Password must have at least one upper case character ")
        validation = False

    if not any(char.islower() for char in password):
        print("Password must contained at least one lower case character ")
        validation = False

    if not any((char in special_symbols for char in password)):
        print("Password must contain at least one special character ")
        validation = False

    if validation:
        return validation


password: str = str(input("Enter Password to check: "))
if password_checker(password):
    print("Password is valid")
else:
    print("Password is not Valid")
