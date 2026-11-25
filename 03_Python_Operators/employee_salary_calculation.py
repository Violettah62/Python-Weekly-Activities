# Topic 3, Task 1: Employee Salary Calculation

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
deduction = float(input("Enter monthly deduction: "))

# Housing Allowance 
housing_allowance = 0.10 * basic_salary

# Gross Salary 
gross_salary = basic_salary + housing_allowance

# Net Salary 
net_salary = gross_salary - deduction

print()
print(f"Employee Name: {employee_name}")
print(f"Basic Salary: KSh {basic_salary:,.2f}")
print(f"Housing Allowance: KSh {housing_allowance:,.2f}")
print(f"Gross Salary: KSh {gross_salary:,.2f}")
print(f"Deduction: KSh {deduction:,.2f}")
print(f"Net Salary: KSh {net_salary:,.2f}")