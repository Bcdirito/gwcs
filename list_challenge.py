#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.

aList = "\nHere is a list of words. We will pick a random index from this list.\n".split()

#Generates a random integer.
# The first number is the lowest integer you can get.
# The second is the highest. The reason we do this is because lists always start at index 0.

aRandomIndex = randint(0, len(aList)-1)

print("Our random word is: {word}\n".format(word=aList[aRandomIndex]))
