#!/usr/bin/env python3
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def enDec(text, shift_amount, switch, direction):
    message = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if switch:
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            message += new_letter
        else:
            message += letter

    print(f"The {direction}d text is {message}")


if __name__ == "__main__":
    print(logo)

    should_continue = True
    while should_continue:
        direction = input(
            "\nType 'encode' to encrypt, type 'decode' to decrypt: ")

        if direction == 'encode' or direction == 'decode':
            text = input("Type your message: ").lower()
            shift = int(input("Type the shift number: "))

            longer = len(alphabet) // 2
            shift = shift % longer

            if direction == "encode":
                enDec(text=text, shift_amount=shift,
                      switch=True, direction=direction)
            elif direction == "decode":
                enDec(text=text, shift_amount=shift,
                      switch=False, direction=direction)
        else:
            print("You don't choose a correct answer")

        r = input("\nType 'yes' if you want to continue. Otherwise type 'no': ")

        if r == 'yes':
            pass
        elif r == 'no':
            should_continue = False
            print("See you soon!")
