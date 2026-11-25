# Topic 9, Task 2: Student Age Registration

entered = input("Enter your age: ")

try:
    age = int(entered)
    print("Age successfully recorded")
except ValueError:

    print("Invalid age entered")

print("Program finished normally.")