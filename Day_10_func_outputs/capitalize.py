#!/usr/bin/env python3

def cap(name, lastName):
    """Take values and return title version"""
    if name == "" and lastName == "":
        return "You didn't provide valid inputs"
    n = name.title()
    l = lastName.title()
    return f"{n} {l}"


if __name__ == '__main__':
    name = input("Name: ")
    lastName = input("Last Name: ")
    print(cap(name, lastName))
