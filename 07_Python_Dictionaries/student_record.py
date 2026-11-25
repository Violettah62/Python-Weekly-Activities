# Topic 7, Task 1: Student Record

student = {
    "registration_number": "CS/001/2026",
    "name": "Mary Wanjiku",
    "course": "Computer Science",
    "year_of_study": 1,
}

# Access values using their keys
print("Name:", student["name"])
print("Course:", student["course"])

# Change the year of study
student["year_of_study"] = 2

# Add a new key/value pair
student["email"] = "mary@example.com"

print("Updated dictionary:")
print(student)