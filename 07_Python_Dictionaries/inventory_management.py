# Topic 7, Task 2: Inventory Management

inventory = {
    "Sugar": 120,
    "Rice": 80,
    "Milk": 200,
    "Bread": 60,
    "Flour": 150,
}

# Display the quantity of a specified product
product = input("Enter a product name to check: ")
if product in inventory:
    print(f"{product}: {inventory[product]} in stock")
else:
    print(f"{product} is not in the inventory.")

inventory["Cooking Oil"] = 90      # add a new product
inventory["Rice"] = 100            # update an existing quantity
del inventory["Bread"]             # remove a product

print("Final inventory:")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")