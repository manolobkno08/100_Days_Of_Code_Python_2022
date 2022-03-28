#!/usr/bin/env python3

def final_price_calculator(total_bill, tip, number_people):
    final_price = 0.0
    each_person = total_bill / number_people
    final_price = each_person + (tip / 100 * each_person)
    return final_price


if __name__ == '__main__':
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    number_people = int(input("How many people to split the bill? "))

    final = final_price_calculator(total_bill, tip, number_people)

    print(f"Each person should pay: ${round(final, 2)}")
