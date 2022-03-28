#!/usr/bin/python3

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def randList(original_list, nr):
    new_l = []
    for i in range(1, len(original_list) - 1):
        x = random.choice(original_list)
        new_l.append(x)
        if i == nr:
            break
    return(new_l)


def password(final_list):
    passwd = ""
    x = random.sample(final_list, len(final_list))
    for i in x:
        passwd += i
    return(passwd)


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    new_letters = randList(letters, nr_letters)
    new_numbers = randList(numbers, nr_numbers)
    new_symbols = randList(symbols, nr_symbols)

    final_list = new_letters + new_numbers + new_symbols

    # print(f"\n{new_letters}\n{new_numbers}\n{new_symbols}\n")
    print(password(final_list))
