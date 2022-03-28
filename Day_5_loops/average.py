#!/usr/bin/env python3

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
avg = 0
for i in student_heights:
    count += 1
    avg += i
res = avg / count
print(round(res))
