#!/usr/bin/env python3
from art import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter a first number: "))

    for key in operations.keys():
        print(key)

    op_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("Enter a second number: "))

    f = operations[op_symbol]
    answer = f(num1, num2)

    print(f"{num1} {op_symbol} {num2} = {answer}")

    run = True
    while run:
        c = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to exit.\n")

        if c == "y":
            op_symbol = input("Pick another operation: ")
            nextNum = float(input("Enter the next number: "))
            f = operations[op_symbol]
            newAnswer = f(answer, nextNum)
            prevAnswer = answer
            answer = newAnswer

            print(f"{prevAnswer} {op_symbol} {nextNum} = {newAnswer}")
        elif c == "n":
            os.system('clear')
            run = False
            calculator()


if __name__ == '__main__':
    calculator()
