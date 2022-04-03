#!/usr/bin/env python3

enemies = 1


def increase_enemies():
    #global enemies
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")
