# Upper case checker function
def upChecker(name):
    for i in name:
        if i.isupper():
            up_checker = 1
            break
        else:
            up_checker = 0
            # continue
    return up_checker


# Space Checker function
def spaceChecker(name):
    if name[0] == " " or name[-1] == " ":
        spaceCheck = 0
        # print("Invalid")
    else:
        spaceCheck = 1
        # print("Valid")
    return spaceCheck


# Number Checking function
def numChecker(name):
    for letter in name:
        if letter.isdigit():
            digitChecker = 1
            break
        else:
            digitChecker = 0
            continue
    return digitChecker


# special characters checker
def specialChecker(name):
    characters = "~`!@#$%^&*()_-+={[}]|\"'<,>.?/"
    if any(char in characters for char in name):
        return 1
    else:
        return 0


# --------------------------------------------------------------------------------------

# get user input password
name = input("Enter Password : ")
# print functions return values
# print(upChecker(name), spaceChecker(name), numChecker(name), specialChecker(name))

# all conditions checking statement
if len(name) >= 8 and upChecker(name) == 1 and spaceChecker(name) == 1 and numChecker(name) == 1 and specialChecker(
        name) == 1:
    print("Valid Password")
else:
    print("---- Invalid Password ! ----")
    if upChecker(name) == 0:
        print("* please include Upper case")
    elif spaceChecker(name) == 0:
        print("* please remove white spaces, front and back")
    elif numChecker(name) == 0:
        print("* please include digit")
    elif specialChecker(name) == 0:
        print("* please include special character")
    elif len(name) >= 8:
        print("*  please include at least 8 characters")
