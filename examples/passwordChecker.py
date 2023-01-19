def pwdchecker(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


user_password = input("Enter new password: ")
print(pwdchecker(user_password))
