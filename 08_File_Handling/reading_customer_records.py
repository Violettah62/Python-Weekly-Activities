# Topic 8, Task 3: Reading Customer Records

import os

if not os.path.exists("customers.txt"):
    with open("customers.txt", "w") as sample:
        sample.write("Grace Achieng, C1001, 0712345678\n")
        sample.write("Samuel Kiprop, C1002, 0723456789\n")

f = open("customers.txt", "r")     # read mode
contents = f.read()                # read everything
print(contents)                    # display on screen
f.close()

print("File modes:")
print("r - read: open an existing file for reading only (error if missing).")
print("w - write: create a file or erase an existing one, then write.")
print("a - append: add new data to the end without deleting existing data.")