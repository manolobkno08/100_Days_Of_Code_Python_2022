#!/usr/bin/env python3

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

person_idx = random.randrange(len(names))
print(f"{names[person_idx]} is going to buy the meal today!")
