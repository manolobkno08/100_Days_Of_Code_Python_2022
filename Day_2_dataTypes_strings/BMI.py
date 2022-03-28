#!/usr/bin/env python3

# weight = 80
# height = 1.75
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight) / (float(height)**2)
print(f"{round(BMI)}")
