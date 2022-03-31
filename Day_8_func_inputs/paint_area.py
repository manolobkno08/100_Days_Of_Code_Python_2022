#!/usr/bin/env python3
import math


def paint_calc(height, width, cover):
    x = math.ceil((height * width) / cover)
    print(f"You'll need {x} cans of paint.")


if __name__ == "__main__":
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)
