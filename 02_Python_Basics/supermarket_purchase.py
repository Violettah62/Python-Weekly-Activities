# Topic 2, Task 2: Supermarket Purchase

# Ask the customer for the details
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = input("Enter quantity purchased: ")
price = input("Enter price per item: ")

# Convert quantity to int and price to float
quantity = int(quantity)
price = float(price)

# Total cost = quantity x price
total_cost = quantity * price

# Display using an f-string; price and total cost to 3 decimal places
print()
print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price: {price:.3f}")
print(f"Total Cost: {total_cost:.3f}")