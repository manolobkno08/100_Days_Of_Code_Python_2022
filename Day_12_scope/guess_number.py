#!/usr/bin/env python3

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def check_answer(guess, answer, turns):
    """Validate if number match"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficult():
    """Set difficult"""
    level = input("Set difficult. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """Run game"""
    print(logo)
    print("Welcome to the GAME!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"{answer}")
    turns = set_difficult()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
