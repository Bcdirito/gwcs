import json

# Creates the dictionary to store responses.
leave = {"status": False}
answers = {}

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
        display_my_answers()
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
    answers["name"] = name
    answers["birthday"] = birthday
    answers["song"] = song
    answers["artist"] = artist
    answers["tv"] = tv
    answers["dream_job"] = dream_job


def display_my_answers():
    print("\nYour name is {name}".format(name=answers["name"]))
    print("\nYour birthday is {dte}".format(dte=answers["birthday"]))
    print("\nYou're jamming to {title} by {artist}".format(title=answers["song"], artist=answers["artist"]))
    print("\nYou can always binge {show}".format(show=answers["tv"]))
    print("\nIf you could be anything, you'd be a {job}".format(job=answers["dream_job"]))

survey_loop()
