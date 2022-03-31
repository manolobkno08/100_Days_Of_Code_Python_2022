#!/usr/bin/env python3

def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")

    else:
        print("It's not a prime number.")


if __name__ == '__main__':
    n = int(input("Check this number: "))
    prime_checker(number=n)
