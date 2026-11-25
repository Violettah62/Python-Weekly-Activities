#Topic 2, Task 3: Employee Status

# Variables
employee_name = "Peter Otieno"
employee_age = 29
employee_salary = 85000.0
employee_active = True      

# Display using f-strings
print(f"Name: {employee_name}")
print(f"Age: {employee_age}")
print(f"Salary: {employee_salary:,.2f}")
print(f"Active: {employee_active}")

# Converting a number to a string with str() before concatenation
message = "Employee age is " + str(employee_age) + " years"
print(message)