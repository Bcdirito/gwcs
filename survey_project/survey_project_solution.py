import json

# Creates the dictionary to store responses.
answers = {}
leave = {"status": False}

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''

def survey_loop():
    print("\nWelcome!")

    while leave["status"] == False:
        print("\nWhat would you like to do?")
        print("\nWould you like to take the survey, view your answers, or exit?\n")
        choice = input("Please enter survey, answers, or exit: ").lower()
        choice_path(choice)

    else:
        print("Bye! See ya next time!\n")

# Print the context of the dictionary.
def choice_path(ans):
    print("\nYou chose {path}\n".format(path=ans))
    if ans == "survey":
        take_survey()
    elif ans == "answers":
        display_answers_path()
    elif ans == "exit":
        leave["status"] = True
    else:
        print("I'm sorry, I didn't quite understand where to go. Please try again.")

def take_survey():
    name = input("\nWhat is your full name: ")
    birthday = input("\nWhen is your birthday: ")
    song = input("\nWhat is a song you're totally jamming to these days: ")
    artist = input("\nWho is it by: ")
    tv = input("\nWhat's a tv show you could always binge: ")
    dream_job = input("\nIf you could have any job, what would it be: ")
    survey_answers = {
        "name": name,
        "birthday": birthday,
        "song": song,
        "artist": artist,
        "tv": tv,
        "dream_job": dream_job
    }
    save_json(survey_answers)

def display_answers_path():
    print("Would you like to display your answers or see all answers: ")
    choice = input("\nPlease enter my or all: ").lower()
    print("\nYou chose {chc}!".format(chc=choice))
    if choice == "my":
        find_my_answers()
    elif choice == "all":
        display_all_answers()
    else:
        print("\nI didn't quite understand that. Please try again!")

def find_my_answers():
    name = input("What is your full name: ")
    for dic in answers_list:
            if dic["name"].lower() == name:
                display_my_answers(dic)

def display_my_answers(user):
    print("\nYour name is {name}".format(name=user["name"]))
    print("\nYou're jamming to {title} by {artist}".format(title=user["song"], artist=user["artist"]))
    print("\nYou can always binge {show}".format(show=user["tv"]))
    print("\nIf you could be anything, you'd be a {job}".format(job=user["dream_job"]))

def display_all_answers():
    all_info = open("./survey_data.json", "r")
    for dic in all_info:
        print("\n{name} said:".format(name=dic["name"]))
        display_my_answers(dic)

def save_json(info):
    survey_json = open("./survey_data.json", "w")
    json.dumps(info, survey_json)


survey_loop()
