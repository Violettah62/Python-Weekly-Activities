# Topic 4, Task 2: Customer Details Using a Tuple

customer = ("Grace Achieng", "C1001", "0712345678", "grace@example.com")

print("Customer:", customer)
print("Name:", customer[0])
print("Telephone:", customer[2])
print("Number of items:", len(customer))

# Attempt to modify the telephone number 
try:
    customer[2] = "0799999999"
except TypeError as error:
    print("Modification failed:", error)

print("Reason: a tuple is immutable - once created, its items cannot be")
print("changed, added or removed. That is why it suits data that must not")
print("be modified during program execution.")