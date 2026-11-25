# Topic 9, Task 1: ATM Input Validation

entered = input("Enter withdrawal amount: ")

try:
    amount = int(entered)          # fails with ValueError for text
except ValueError:
    print("Invalid amount. Please enter a number.")
else:
    print(f"Withdrawal amount: {amount}")