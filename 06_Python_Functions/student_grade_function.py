# Topic 6, Task 2: Student Grade Function

def calculate_grade(mark):
    """Return the grade that matches the given mark."""
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


mark = int(input("Enter the student's mark: "))
grade = calculate_grade(mark)
print(f"Grade: {grade}")