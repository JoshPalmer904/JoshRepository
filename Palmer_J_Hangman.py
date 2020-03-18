'''Module to run a hangman game.'''

import random
import string
WORD_FILE = open('word_list.txt', 'r')
WORD_BANK = [line.rstrip('\n') for line in WORD_FILE.readlines()]


class Word:
    '''Assign an answer & return the number of unique characters.'''
    def __init__(self):
        self.answer = WORD_BANK[random.randint(1, len(WORD_BANK))]

    def reveal_word(self, guess, current_word):
        '''Reveal the letters which have been guessed correctly.'''
        wrong_guess = True

        for count, char in enumerate(self.answer):
            if char.lower() == guess:
                current_word[count] = char
                wrong_guess = False

        return (wrong_guess, current_word)

def verify_guess(guess, all_guesses):
    '''Check whether player's guess is in the correct format.'''
    good_guess = False

    while not good_guess:
        if len(guess) == 1 and guess.lower() in string.ascii_lowercase\
        and not guess in all_guesses:
            good_guess = True
        elif guess in all_guesses:
            guess = input('\nYou have already guessed this letter.\
                \nPlease enter your next guess: ').lower()
        else:
            guess = input('\nYou did not enter a single letter.\
                \nPlease enter your next guess: ').lower()

    return guess

def victory(current_word):
    '''Determine if the player has won or not.'''
    if not '*' in current_word:
        print(f"\nYour word is {WORD.answer}\nCongratulations you win!")
    else:
        print("\nYou lose!")


WORD = Word()
shown_word = ['*' for char in WORD.answer]
total_guesses = 7
previous_guesses = []

print('Welcome to Hangman!\nRemaining lives: 7')

while total_guesses != 0:
    print('\nYour word is: ', ''.join(shown_word))
    user_guess = input('Please enter your next guess: ').lower()
    user_guess = verify_guess(user_guess, previous_guesses)
    previous_guesses.append(user_guess.lower())
    (wrong, shown_word) = WORD.reveal_word(user_guess, shown_word)
    if wrong:
        total_guesses -= 1
        print(f'\nRemaining lives: {total_guesses}')

    if not '*' in shown_word:
        break

victory(shown_word)
