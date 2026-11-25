# Topic 2, Task 1: Employee Information

# Accept input from the keyboard 
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
employee_age = input("Enter employee age: ")
basic_salary = input("Enter basic salary: ")

# Convert age to int and salary to float
employee_age = int(employee_age)
basic_salary = float(basic_salary)

annual_salary = basic_salary * 12

# Display the details using an f-string, salaries to 2 decimal places
print()
print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Age: {employee_age}")
print(f"Basic Salary: {basic_salary:,.2f}")
print(f"Annual Salary: {annual_salary:,.2f}")