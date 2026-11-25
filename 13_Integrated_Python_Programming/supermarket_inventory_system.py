# Topic 13, Task 3: Supermarket Inventory System

class Product:
    def __init__(self):
        self.name = ""
        self.code = ""
        self.price = 0.0
        self.quantity = 0

    def setDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        return self.price * self.quantity   

    def display(self):
        print(f"{self.name} | {self.code} | Price: {self.price:,.2f} | "
              f"Qty: {self.quantity} | Stock Value: {self.calculateStockValue():,.2f}")


def read_number(prompt, kind):
    """Ask until the user enters a valid number of the given type (int/float)."""
    while True:
        try:
            value = kind(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


items = [("Sugar 1kg", "P001"), ("Rice 2kg", "P002"), ("Milk 500ml", "P003")]

products = []    # list of Product objects
for name, code in items:
    price = read_number(f"Enter price of {name}: ", float)
    qty = read_number(f"Enter quantity of {name}: ", int)
    p = Product()
    p.setDetails(name, code, price, qty)
    products.append(p)

print("\nInventory")
print("-" * 60)
total_value = 0
for p in products:
    p.display()
    total_value += p.calculateStockValue()
print("-" * 60)
print(f"Total value of all products in stock: KSh {total_value:,.2f}")

# Save inventory to a file and close it
f = open("inventory.txt", "w")
for p in products:
    f.write(f"{p.name}, {p.code}, {p.price}, {p.quantity}, {p.calculateStockValue()}\n")
f.write(f"Total stock value, {total_value}\n")
f.close()
print("Inventory saved to inventory.txt")