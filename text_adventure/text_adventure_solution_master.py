from random import shuffle

# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

user_input = ""
options = ["left", "right"]
decisions = ["yes", "no"]

while user_input not in options:
    user_input = input("Type 'left' to go left or 'right' to go right: ").lower()

if user_input == "left":
    print("\nUpon moving left, you stumble upon a weird looking root. You stare at it and decide whether or not to touch it.\n")

    decision = ""

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

    # Continue code to finish story.
