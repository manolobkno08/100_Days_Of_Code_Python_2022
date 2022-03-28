#!/usr/bin/env python3
import random


def validate(user, machine):
    try:
        if user == "Rock" and machine == "Rock":
            return("Draw")
        if user == "Rock" and machine == "Paper":
            return("You Lose")
        if user == "Rock" and machine == "Scissors":
            return("You Win")

        if user == "Paper" and machine == "Paper":
            return("Draw")
        if user == "Paper" and machine == "Scissors":
            return("You Lose")
        if user == "Paper" and machine == "Rock":
            return("You Win")

        if user == "Scissors" and machine == "Scissors":
            return("Draw")
        if user == "Scissors" and machine == "Rock":
            return("You Lose")
        if user == "Scissors" and machine == "Paper":
            return("You Win")

    except:
        return("Something is wrong")


if __name__ == '__main__':
    user = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors: "))
    list = ['Rock', 'Paper', 'Scissors']
    machine = random.choice(list)

    if user == 0 or user == 1 or user == 2:
        if user == 0:
            user = "Rock"
        elif user == 1:
            user = "Paper"
        elif user == 2:
            user = "Scissors"
        answer = validate(user, machine)
        print(answer)
    else:
        print("Number out of range")

    print(f"Machine choise: {machine}")
    print(f"My choise: {user}")
