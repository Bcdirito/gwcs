from random import shuffle

# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

# This global variable is used to make sure that no matter what the user input is, it will keep from breaking unless terminated with a command line input
user_input = ""

# These are also being used for keeping the program from breaking and/or ending early
options = ["left", "right"]
decisions = ["yes", "no"]

# The syntax of this solution might look strange, but I've checked and it works. The reason you can use a basic else statment for the right path is because anything that isn't left or right will restart the journey.

while user_input not in options:
    # Always make sure to add a space at the end of an input string, it make it more legible for the user.
    # Also, I specifically added .lower() at the end of each input so that I only need one if statement and not an if or statement. This also helps to keep the program from breaking.
    user_input = input("Type 'left' to go left or 'right' to go right: ").lower()

if user_input == "left":
    # In a string in both Python and JavaScript, \n will always start a new line, making the text more legible for the reader.
    print("\nUpon moving left, you stumble upon a weird looking root. You stare at it and decide whether or not to touch it.\n")

    decision = ""

    # The following while loop uses the same logic and syntax as the one above.
    while decision not in decisions:
        decision = input("Please enter yes or no: ").lower()

    if decision == "yes":
        print("\nUnfortunately, the root wraps itself around your arm and you are unable to move for the rest of the hour. A white rabbit runs by in a hurry...\n")
    else:
        print("\nYou decide to leave the root as is. You continue onward and find an exit! Congrats! You've made it to the Mad Hatter's Tea Party! Enjoy a very merry un-birthday!\n")
else:
    print("\nUpon heading down the path to your right, you come across a potion that says...")

    print("\n'Drink Me'\n")

    print("Do you drink it?\n")

    decision = ""

    while decision not in decisions:
        decision = input("Plese enter yes or no: ")

    if decision == "yes":
        print("\nWhen you drink the potion, you shrink down to the size of a flea. You decide to continue on, but it takes to long to reach the end...\n")
    else:
        print("\nYou decide it's not a great idea to drink strange liquids, and you're probably correct. You continue on navigating throughout the maze and find an exit that leads to a very strange catepillar...\n")
        print("\nCongrats on making it through the maze!\n")
