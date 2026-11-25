# Topic 10, Task 3: Product Management

class Product:
    def __init__(self):
        self.name = ""
        self.code = ""
        self.price = 0.0
        self.quantity = 0
        self.stock_value = 0.0

    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        # Stock Value = Price x Quantity
        self.stock_value = self.price * self.quantity
        return self.stock_value

    def displayProductDetails(self):
        print(f"Product Name: {self.name}")
        print(f"Product Code: {self.code}")
        print(f"Price: KSh {self.price:,.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Stock Value: KSh {self.stock_value:,.2f}")


product = Product()
product.setProductDetails("Wireless Mouse", "P100", 1500.0, 20)
product.calculateStockValue()
product.displayProductDetails()