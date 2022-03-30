#!/usr/bin/env python3

import sys
import os
import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
# lives
lives = 6
# Logo to welcome
print(logo)

# print(f'The word is {chosen_word}')

# display spaces
display = []
for _ in range(len(chosen_word)):
    display += "_"

# infinite loop
end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # less live
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    # end loop game
    if "_" not in display:
        end_game = True
        print("You win!")

    # stage image
    print(stages[lives])
