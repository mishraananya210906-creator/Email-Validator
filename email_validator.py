import re

def validate_email(email):
    condition = r"^[a-z]+[.]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if re.match(condition, email):
        return True
    return False


email = input("Enter your email: ")

if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")