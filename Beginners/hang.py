# Writing a hangman game in python with basic class functionalities

"""
Game setup: The game of hangman is for two or more players, comprising a selecting player and one or more guessing players.
Word selection: The selecting player selects a word that the guessing players will try to guess.
The selected word is traditionally represented as a series of underscores for each letter in the word.
The selecting player also draws a scaffold to hold the hangman illustration.
Guessing: The guessing players attempt to guess the word by selecting letters one at a time.
Feedback: The selecting player indicates whether each guessed letter appears in the word.
If the letter appears, then the selecting player replaces each underscore with the letter as it appears in the word.
If the letter doesn’t appear, then the selecting player writes the letter in a list of guessed letters. Then, they draw the next piece of the hanged man. To draw the hanged man, they begin with the head, then the torso, the arms, and the legs for a total of six parts.
Winning conditions: The selecting player wins if the hanged man drawing is complete after six incorrect guesses, in which case the game is over. The guessing players win if they guess the word.
If the guess is right, the game is over, and the guessing players win.
If the guess is wrong, the game continues.
A game in progress is shown below. In this game, the word to be guessed is hangman:
"""

# Random choice of words from random.txt

from random import choice


def select_word():
    with open("words,txt", "r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

#Take the user input and validate it
def get_player_input(guessed_word):
   pass 
