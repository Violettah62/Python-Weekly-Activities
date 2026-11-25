# Topic 8, Task 2: Sales Records

product = input("Enter product name: ")
quantity = input("Enter quantity sold: ")
amount = input("Enter total sales amount: ")

f = open("sales.txt", "a")         # adds to the end of the file
f.write(f"{product}, {quantity}, {amount}\n")
f.close()

print("Sales record saved to sales.txt")
print("Why append mode: each day's sales are added to the end of the file,")
print("so earlier records are kept. Write mode would erase them every time.")