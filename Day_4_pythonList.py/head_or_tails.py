#!/usr/bin/env python3
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

r = random.randint(0, 1)
if r == 1:
    print("Heads")
if r == 0:
    print("Tails")
