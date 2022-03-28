#!/usr/bin/python3

# Password Generator Project
import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def psswd_generator():
    run = True
    count = 0

    while (run):
        print("Welcome to the PyPassword Generator!")
        if count > 0:
            ex = input("Would you like exit? Y or N\n")
            if ex == 'Y' or ex == 'y':
                sys.exit("Thanks, see you soon!")
            elif ex == 'N' or ex == 'n':
                pass

        nr_letters = int(
            input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        if nr_letters > len(letters) or nr_numbers > len(numbers) or nr_symbols > len(symbols):
            sys.exit(
                f"Long of chars out of range: letters: {len(letters)}, numbers: {len(numbers)}, symbols: {len(symbols)}")

        else:
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list += random.choice(letters)

            for number in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            for symbol in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            random.shuffle(password_list)

            password = ""

            for item in password_list:
                password += item

            print('\n' + '*' * 15)
            print("Your new password is: {}".format(password))
            print('*' * 15 + '\n')

            count += 1


if __name__ == '__main__':
    psswd_generator()
