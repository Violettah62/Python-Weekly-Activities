# Topic 6, Task 1: Electricity Bill Function

def calculate_bill(units_consumed, cost_per_unit):
    """Return the bill = units consumed x cost per unit."""
    bill = units_consumed * cost_per_unit
    return bill


units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit (KSh): "))

total_bill = calculate_bill(units, cost)    # call the function
print(f"Electricity bill: KSh {total_bill:,.2f}")