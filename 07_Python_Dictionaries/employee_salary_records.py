# Topic 7, Task 3: Employee Salary Records

employees = {
    "Alice": 60000,
    "Brian": 55000,
    "Carol": 72000,
    "David": 48000,
    "Esther": 65000,
}

# Display all names and salaries
print("Employees:")
for name, salary in employees.items():
    print(f"  {name}: KSh {salary:,}")

employees["Brian"] = 58000     
employees["Felix"] = 50000   

# Total salary payable
total = sum(employees.values())
print(f"Total salary payable: KSh {total:,}")
