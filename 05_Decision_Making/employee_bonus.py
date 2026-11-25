# Topic 5, Task 3: Employee Bonus

name = input("Enter employee name: ")
years = int(input("Enter years of service: "))
rating = int(input("Enter performance rating: "))

# Logical operator: check if years of service is at least 3 and rating is at least 4
if years >= 3 and rating >= 4:
    result = "Employee qualifies for a bonus"
else:
    result = "Employee does not qualify for a bonus"

print()
print(f"Employee Name: {name}")
print(f"Years of Service: {years}")
print(f"Performance Rating: {rating}")
print(result)