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

import string
from random import choice


def select_word():
    with open("words.txt", "r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


# Take the user input and validate it
def get_player_input(guessed_letter):
    while True:
        player_input = input("Enter your letter you guessed : ").lower()
        if _validate_input(player_input, guessed_letter):
            return player_input


def _validate_input(player_input, guessed_letter):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letter
    )


# To show the player he had letters guessed and how many are left
def join_guessed_letter(guessed_letter):
    return "".join(sorted(guessed_letter))


# build the guessed_word to show the user
def build_guessed_word(target_words, guessed_letter):
    current_letters = []
    for letter in target_words:
        if letter in guessed_letter:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return "".join(current_letters)


# draw hangman in ascii
def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])


# planning the end of game
MAX_INCORRECT_GUESSES = 6


def game_over(wrong_guesses, target_words, guessed_letter):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_words) <= guessed_letter:
        return True

    return False


# Running and closing the loop
if __name__ == "__main__":
    # Initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Hangman!")
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(f"Current guessed letters: {join_guessed_letter(guessed_letters)}\n")

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)
