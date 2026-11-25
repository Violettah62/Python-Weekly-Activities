# Topic 10, Task 2: Student Management

class Student:
    def __init__(self):
        self.name = ""
        self.reg_no = ""
        self.course = ""
        self.mark = 0
        self.grade = ""

    def setStudentDetails(self, name, reg_no, course, mark):
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

    def displayStudentDetails(self):
        print(f"Name: {self.name}")
        print(f"Registration Number: {self.reg_no}")
        print(f"Course: {self.course}")
        print(f"Mark: {self.mark}")
        print(f"Grade: {self.grade}")


student = Student()
student.setStudentDetails("Mary Wanjiku", "CS/001/2026", "Computer Science", 78)
student.calculateGrade()
student.displayStudentDetails()