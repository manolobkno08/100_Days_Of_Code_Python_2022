#!/usr/bin/env python3

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

x = (name1 + name2).replace(" ", "").lower()
T = x.count('t')
R = x.count('r')
U = x.count('u')
E = x.count('e')
true_c = T + R + U + E
true_c = str(true_c)

L = x.count('l')
O = x.count('o')
V = x.count('v')
E = x.count('e')
love_c = L + O + V + E
love_c = str(love_c)

score = true_c + love_c
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
