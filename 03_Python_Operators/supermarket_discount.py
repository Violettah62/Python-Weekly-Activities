# Topic 3, Task 2: Supermarket Discount

purchase_amount = float(input("Enter the total purchase amount (KSh): "))

# Comparison operator: is the purchase at least KSh 10,000?
qualifies = purchase_amount >= 10000

if qualifies:
    discount = 0.15 * purchase_amount       
else:
    discount = 0.0                          

# Final Amount
final_amount = purchase_amount - discount

print()
print(f"Purchase Amount: KSh {purchase_amount:,.2f}")
print(f"Discount: KSh {discount:,.2f}")
print(f"Final Amount: KSh {final_amount:,.2f}")