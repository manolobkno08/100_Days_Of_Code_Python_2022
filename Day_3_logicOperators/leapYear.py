#!/usr/bin/env python3

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap year.")
    print("Leap year.")
else:
    print("Not leap year.")
