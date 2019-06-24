#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
correct = False
counter = 0

for i in range(3):
	counter += 1
	guess = input("\nGuess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("\nThat's not a positive whole number, try again!")
	else:
		int_guess = int(guess) # converts a string to an integer
		
		if counter == 3 and int_guess != aRandomNumber:
			print("\nGame Over! Please try again!\n")
		elif int_guess > aRandomNumber:
			print("\nToo high. Try guessing lower.")
		elif int_guess < aRandomNumber:
			print("\nToo low. Try guessing higher")
		else:
			correct = True
			print("\nYou win! Congrats!\n")
			break
