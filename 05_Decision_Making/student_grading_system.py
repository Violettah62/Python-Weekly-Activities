# Topic 5, Task 1: Student Grading System

name = input("Enter your name: ")
mark = int(input("Enter your examination mark: "))

# Validate first, then grade with if...elif...else
if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    if mark >= 70:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"Name: {name}")
    print(f"Mark: {mark}")
    print(f"Grade: {grade}")