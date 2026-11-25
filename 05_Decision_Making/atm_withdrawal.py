# Topic 5, Task 2: ATM Withdrawal

balance = 50000     # initial balance 

amount = int(input("Enter withdrawal amount (KSh): "))

# Check each condition and show a suitable error message if it fails
if amount <= 0:
    print("Error: withdrawal amount must be greater than zero.")
elif amount > balance:
    print("Error: insufficient funds. Amount exceeds your balance.")
elif amount % 500 != 0:
    print("Error: amount must be a multiple of KSh 500.")
else:
    balance -= amount
    print("Withdrawal successful.")
    print(f"Remaining balance: KSh {balance:,}")