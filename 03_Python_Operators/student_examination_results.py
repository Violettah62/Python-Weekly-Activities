# Topic 3, Task 3: Student Examination Results

student_name = input("Enter student name: ")
coursework = float(input("Enter coursework mark (out of 30): "))
exam = float(input("Enter examination mark (out of 70): "))

# Total Mark = Coursework Mark + Examination Mark
total_mark = coursework + exam

# Comparison operator gives True or False
passed = total_mark >= 40

print()
print(f"Student Name: {student_name}")
print(f"Coursework Mark: {coursework}")
print(f"Examination Mark: {exam}")
print(f"Total Mark: {total_mark}")
print(f"Passed: {passed}")