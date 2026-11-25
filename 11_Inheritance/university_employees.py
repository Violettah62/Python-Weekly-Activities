# Topic 11, Task 1: University Employees

class Employee:
    def __init__(self):
        self.name = ""
        self.employee_id = ""

    def displayEmployee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


class Lecturer(Employee):          # Lecturer inherits from Employee
    def __init__(self):
        super().__init__()
        self.teaching_subject = ""

    def displayLecturer(self):
        self.displayEmployee()                 # reuse the parent method
        print(f"Teaching Subject: {self.teaching_subject}")


lecturer = Lecturer()
lecturer.name = "Dr. Jane Mwangi"
lecturer.employee_id = "E2001"
lecturer.teaching_subject = "Python Programming"
lecturer.displayLecturer()