#!/usr/bin/env python3

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key, value in student_scores.items():
    if value >= 91 and value <= 100:
        student_grades[key] = "Outstanding"
    elif value >= 81 and value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif value >= 71 and value <= 80:
        student_grades[key] = "Acceptable"
    elif value <= 70:
        student_grades[key] = "Fail"

print(student_grades)
