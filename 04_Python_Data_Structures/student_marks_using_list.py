# Topic 4, Task 1: Student Marks Using a List

marks = [78, 65, 89, 54, 72]     # five subject marks

print("Marks:", marks)

total = sum(marks)               # total of all marks
print("Total marks:", total)

average = total / len(marks)     # average mark
print("Average mark:", average)

print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

# Modify the third subject and show the updated list
marks[2] = 95
print("Updated marks:", marks)