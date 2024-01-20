"""
Authors: Bessie Li
Consulted: n/a
Date: 10/11/2023
Purpose: wordGuesser task: Allows user to guess words and reveals
  which letters are correct (or misplaced but present).
"""

import random # will be used to play a game with a random word

#---------------#
# Provided Text #
#---------------#

# This variable has the text you'll need to print out at the start of
# each game, so you don't have to type it all in yourself. It's put in
# all-caps to indicate that it's a global variable: any function can use
# it, but it cannot be modified inside a function.
INTRO = """\
Welcome to guess-that-word!
You will guess what the word could be and we will reveal which letters
of your guess are correct. If a letter is in the word but in a different
location, we'll let you know.

'@' means this letter is correct.
'*' means this letter is present in a different spot.
'-' means this letter is not present.

Use the hints to guess the word!
"""


#----------------------#
# Write your code here #
#----------------------#

def letterHints(word, guess):
    """This function returns a string of hints depending on how close the guess was to the actual word"""
    hint = ""
    x = 0
    for i in range(len(guess)):
        if guess[i] == word[x]:
            hint = hint+"@"
        elif guess[i] in word:
            hint = hint+"*"
        else:
            hint = hint+"-"
        x = x+1
    return hint

def getGuess(integer):
    """This function returns the word guessed as long as the word guessed is the same length as the inputed word"""
    y = ("Guess a word ("+str(integer)+" letters): ")
    x = input(y)
    while len(x) != integer:
        print("You must guess a word with", integer, "letters.")
        x = input(y)
    return x

def playGame(word1):
    """This function prints results based on if the user guesses the word correctly or not and in how many attempts"""
    print(INTRO)
    print("The word has", len(word1), "letters.")
    count = 0
    y = True
    while y:
        x = getGuess(len(word1))
        count = count +1
        if x != word1:
            print(letterHints(word1, x))
        if x == word1:
            print("Congratulations! You guessed it, the word was:", word1)
            if count ==1:
                print("Wow, you guessed it in", count, "try!")
            elif count < 7:
                print("Great job! You guessed the word in just", count, "tries.")
            elif count >= 7:
                print("You guessed the word in", count, "tries.")
            y = False

        

#--------------#
# Random Games #
#--------------#

# This variable holds a list of words that we will use to pick a random
# word to play the game with. The list is not very long, so we don't
# use it to validate guesses. The words are all between 4 and 7 letters
# long, and most of them are drawn from the index of our textbook, or
# otherwise relate to computer science concepts. There are three words
# that start with each letter of the alphabet, except for 'x', 'y', and
# 'z'.
WORDS = [
    "assign", "alias", "append", "branch", "binary", "boolean",
    "catch", "comment", "copy", "data", "debug", "declare",
    "element", "error", "empty", "file", "float", "format",
    "global", "game", "grid", "hash", "header", "heap",
    "input", "integer", "iterate", "join", "joule", "jump",
    "keyword", "kernel", "keys", "loop", "list", "local",
    "mutable", "method", "module", "none", "newline", "nested",
    "object", "open", "order", "python", "print", "pattern",
    "quote", "queue", "quine", "range", "return", "recurse",
    "syntax", "string", "shell", "test", "tuple", "turtle",
    "update", "unique", "user", "value", "void", "virtual",
    "while", "wave", "word", "xerox", "yield", "zero", "zombie"
]


# Note: This won't work until you've finished playGame.

def playRandomGame():
    """
    Works like playGame, except the word is chosen randomly from the
    WORDS list. Use this to play a game where you don't know the answer
    ahead of time.
    """
    playGame(random.choice(WORDS))