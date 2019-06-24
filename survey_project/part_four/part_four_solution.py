import json

# Creates the dictionary to store responses.
leave = {"status": False}
survey_json = open("./part_four_data.json", "r+")
all_answers = json.load(survey_json)
survey_json.close()

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''

def survey_loop():
    print("\nWelcome!")

    while leave["status"] == False:
        print("\nWhat would you like to do?")
        print("\nWould you like to take the survey, view your answers, analyze data, or exit?\n")
        choice = input("Please enter survey, answers, analyze, or exit: ").lower()
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
    elif ans == "analyze":
        choose_data_path()
    else:
        print("I'm sorry, I didn't quite understand where to go. Please try again.")

def take_survey():
    name = input("\nWhat is your full name: ")
    birthday = input("\nWhen is your birthday: ")
    age = int(input("\nHow old are you: "))
    song = input("\nWhat is a song you're totally jamming to these days: ")
    artist = input("\nWho is it by: ")
    tv = input("\nWhat's a tv show you could always binge: ")
    dream_job = input("\nIf you could have any job, what would it be: ")
    answers = {
        "name": name,
        "birthday": birthday,
        "age": age,
        "song": song,
        "artist": artist,
        "show": tv,
        "dream_job": dream_job
    }

    save_response = input("\nWould you like to save this to the database? Please input 'yes' or 'no': ").lower()
    while save_response != "yes" and save_response != "no":
        print("\nI didn't quite get that!")
        save_response = input("\nWould you like to save this to the database? Please input 'yes' or 'no': ").lower()
    else:
        if save_response == "yes":
            all_answers.append(answers)
            with open("./part_four_data.json", "w") as f:
                    json.dump(all_answers, f)

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
    for dic in all_answers:
            if dic["name"].lower() == name:
                display_my_answers(dic)

def display_my_answers(user):
    print("\nYour name is {name}".format(name=user["name"]))
    print("\nYour birthday is {dte}".format(dte=user["birthday"]))
    print("\nYou're jamming to {title} by {artist}".format(title=user["song"], artist=user["artist"]))
    print("\nYou can always binge {show}".format(show=user["show"]))
    print("\nIf you could be anything, you'd be a {job}".format(job=user["dream_job"]))

def display_all_answers():
    for dic in all_answers:
        print("\n{name} said:".format(name=dic["name"]))
        display_my_answers(dic)

def choose_data_path():
    print("Would you like to see data for ages, shows, or artists?")
    choice = input("\nPlease enter ages, shows, or artists: ").lower()

    while choice != "ages" and choice != "shows" and choice != "artists":
        print("\nI didn't quite understand that. Please try again!")
        choice = input("\nPlease enter ages, shows, or artists").lower()
    else:
        if choice == "ages":
            analyze_ages()
        else:
            analyze_shows_or_artists(choice)

def analyze_shows_or_artists(key):
    print("\nHere are all of the favorite {info}: ".format(info=key))
    for dic in all_answers:
        print(dic[key[0:-1]])

def analyze_ages():
    total_ages = 0
    total_surveys = len(all_answers)
    age_dict = {}
    for dic in all_answers:
        total_ages += dic["age"]
        if dic["age"] in age_dict:
            age_dict[dic["age"]] += 1
        else:
            age_dict[dic["age"]] = 1
    avg_age = total_ages / total_surveys
    display_age_info(age_dict, avg_age)

def display_age_info(age_dictionary, average_age):
    for k in age_dictionary:
        string_k = "{num}".format(num=k)
        print("\nThere are {value} people who are {key} years old!".format(value=string_k, key=k))
    print("\nThe average age is {avg}".format(avg=average_age))

survey_loop()
