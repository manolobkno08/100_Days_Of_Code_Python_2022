#!/usr/bin/python3

def gauss(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    print(sum)


if __name__ == '__main__':
    gauss(100)
