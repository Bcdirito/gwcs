import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_", "_"]
for char in word:
	current_word.append("_")

	if len(current_word) == len(word):
		break


 # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ").lower()
    counter = 0
    # check if the guess is valid: Is it one letter? Have they already guessed it?
    if word.find(guess) != -1:
        for char in word:
            counter += 1
            if char == guess:
                current_word[counter - 1] = guess

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

    if "_" not in current_word:
        print ("You won the game by guessing the word: " + "".join(current_word))
        break
    else:
        print("".join(current_word))

        fails = fails + 1

        if fails < maxfails:
            print("You have " + str(maxfails - fails) + " tries left!")
        else:
            break
