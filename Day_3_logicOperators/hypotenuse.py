#!/usr/bin/python3

import math
print("*** hypotenuse ***")


def pythagorean(a, b):
    if a <= 0 or b <= 0:
        print("The values can't be equal to 0")

        return False
    else:
        r = (a**2)+(b**2)
        r = math.sqrt(r)
        return int(r)


if __name__ == '__main__':
    a = int(input("Value a: "))
    b = int(input("Value b: "))

    hypotenuse = pythagorean(a, b)
    if (hypotenuse):
        print(f'The hyputenuse of rectangle is {hypotenuse}')

    print("\n*** List Iterator ***")
    list = ['Audi', 'BMW', 'Mercedez', 'Mazda']
    c = 1
    for item in range(0, len(list)):
        print(f'{c}: {list[item]}')
        c += 1
