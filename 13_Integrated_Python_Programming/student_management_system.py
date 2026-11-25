# Topic 13, Task 2: Student Management System

class Student:
    def __init__(self):
        self.name = ""
        self.reg_no = ""
        self.course = ""
        self.mark = 0
        self.grade = ""

    def setDetails(self, name, reg_no, course, mark):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        self.mark = mark

    def calculateGrade(self):
        if self.mark >= 70:
            self.grade = "A"
        elif self.mark >= 60:
            self.grade = "B"
        elif self.mark >= 50:
            self.grade = "C"
        elif self.mark >= 40:
            self.grade = "D"
        else:
            self.grade = "F"

    def displayDetails(self):
        print(f"{self.name} | {self.reg_no} | {self.course} | Mark: {self.mark} | Grade: {self.grade}")


def displayStudents(students):
    """Display every student in the list."""
    print("\nStudent List")
    print("-" * 60)
    for s in students:
        s.displayDetails()


def read_mark(name):
    """Keep asking until a valid mark (0-100) is entered."""
    while True:
        try:
            mark = int(input(f"Enter mark for {name}: "))
            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
                continue
            return mark
        except ValueError:
            print("Invalid mark. Please enter a number.")


people = [
    ("Mary Wanjiku", "CS/001/2026", "Computer Science"),
    ("John Kamau", "CS/002/2026", "Computer Science"),
    ("Aisha Hassan", "IT/003/2026", "Information Technology"),
]

students = []                        # list that stores the Student objects
for name, reg_no, course in people:
    mark = read_mark(name)
    s = Student()
    s.setDetails(name, reg_no, course, mark)
    s.calculateGrade()
    students.append(s)

displayStudents(students)

# Save details and grades to a file, then close it
f = open("students.txt", "w")
for s in students:
    f.write(f"{s.name}, {s.reg_no}, {s.course}, {s.mark}, {s.grade}\n")
f.close()
print("\nStudent details saved to students.txt")