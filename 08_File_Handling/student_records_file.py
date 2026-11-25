# Topic 8, Task 1: Student Records File

f = open("students.txt", "w")      # write mode

print("Name: Mary Wanjiku, Reg No: CS/001/2026, Course: Computer Science, Mark: 78", file=f)
print("Name: John Kamau, Reg No: CS/002/2026, Course: Computer Science, Mark: 65", file=f)
print("Name: Aisha Hassan, Reg No: IT/003/2026, Course: Information Technology, Mark: 82", file=f)

f.close()        #close file                 
print("Records saved to students.txt")

print("Note: if students.txt already exists, opening it in 'w' mode ERASES")
print("(overwrites) all its existing contents before writing the new data.")