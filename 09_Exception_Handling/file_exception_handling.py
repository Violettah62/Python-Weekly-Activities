# Topic 9, Task 3: File Exception Handling

try:
    f = open("employees.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("The employee file was not found.")
finally:
    # runs whether or not an error occurred
    print("File processing completed.")