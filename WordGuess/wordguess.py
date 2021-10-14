import random
import string

# How many guesses we'll give them
guesses_remaining = 10

# A list to hold what letters they've guessed
guesses = ''

# Get a list of words
with open('words.txt', 'r') as f:
    words = f.read().split('\n')

# Pick one of those words but make sure it's at least a certain length.
# Capitalize the entire word to make searching easier
while True:
    word = random.choice(words).upper()
    if len(word) > 4:
        break

# Keep them guessing
while True:

    # Flag to determine if they've won
    # TODO

    # Print the word with blanks or correct guesses
    # TODO

    # Tell them how many guesses they have remaining
    # TODO

    # Tell them the letters available
    print('Available letters: ', end='')
    for l in string.ascii_uppercase:
        if l in guesses:
            print('_', end='')
        else:
            print(l, end='')

    print()

    # Check if they've guessed all of the letters
    # TODO

    # Check if they've run out of guesses
    # TODO
    
    # Have them guess another letter or a full word
    guess = input('Please guess a letter or a word: ')

    # Capitalize their guess
    # TODO

    # Make sure they guess something
    # TODO

    # If they guessed the entire word they won
    # TODO

    # If they guess the same letter more than once we should penalize them
    # TODO

    # Add their guess to our list of guesses if it's letter
    # TODO

    # Subject one remaining guess
    # TODO
