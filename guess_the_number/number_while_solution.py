from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
correct = False

while not correct:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    	print("That's not a positive whole number, try again!")
    else:
        int_guess = int(guess) # converts a string to an integer
        correct = int_guess == aRandomNumber
else:
    print("\nCongrats! You guessed {num} which was the correct answer!\n".format(num=aRandomNumber))
