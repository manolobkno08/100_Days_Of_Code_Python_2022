#!/usr/bin/env python3

from art import logo
import os

def addItem(data, name, bid):
    new_data = {
        "name": name,
        "bid": bid
    }
    data.append(new_data)

def checkBid(data):
    # maxBid = max(data, key=lambda x: x["bid"])
    # print(f"\nThe winner is {maxBid['name']} with a bid of ${maxBid['bid']}.")
    max_bid = 0
    winner = ""
    for obj in data:
        if obj["bid"] > max_bid:
            max_bid = obj["bid"]
            winner += obj["name"]
    print(f"\nThe winner is {winner} with a bid of ${max_bid}.")

if __name__ == '__main__':
    print(logo)

    data = []
    run = True
    while run:
        print("Welcome to the secret auction program.")
        name = input("What is your name?: ")
        bid = int(input("What is your bid? : $"))

        addItem(data, name, bid)

        other_bidders = input(
            "Are there any other biders? Type 'yes' or 'no'.\n")
        if other_bidders == 'yes':
            os.system('clear')
        elif other_bidders == 'no':
            run = False
            os.system('clear')
            print(logo)
            # print(data)
            checkBid(data)
