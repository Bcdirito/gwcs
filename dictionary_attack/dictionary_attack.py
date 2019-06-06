#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
weak_password_list = []
weak_password = True

for line in f:
    weak_password_list.append(str(line[0:-1]))

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
stripped_password = test_password.replace(" ", "")

def check_password(pwd):
    tested_password = pwd
    if pwd not in weak_password_list:
        level_two_check(pwd)
    else:
        print("That is a weak password")

def level_two_check(password):
    if not password.isalpha():
        print("stronger password")
    else

while weak_password == True:
    check_password(stripped_password)
else:
    print("That is a strong password!")
