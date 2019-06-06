#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
weak_password_list = []
weak_password_status = True


for line in f:
    weak_password_list.append(str(line[0:-1]))

def enter_password():
    print("Can your password survive a dictionary attack?")

    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password: ")

    #Write logic to see if the password is in the dictionary file below here:
    stripped_password = test_password.replace(" ", "")
    return stripped_password

def weak_password():
    print("\nThat is a weak password. Please try again.\n")

def level_two_check(password):
    if not password.isalpha():
        level_three_check(password)
    else:
        weak_password()



while weak_password_status == True:
    password = enter_password()
    if password.lower() not in weak_password_list:
        if not password.isalpha():
                filtered_password = "".join(filter(lambda w: w.isalpha(), password))
                if len(password) - 3 >= len(filtered_password):
                    weak_password_status = False
                else:
                    print("\nTry adding some numbers or special characters\n")
        else:
            weak_password()
    else:
        weak_password()
else:
    print("\nThat is a strong password!\n")
