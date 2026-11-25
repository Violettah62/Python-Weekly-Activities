# Topic 13, Task 1: Simple Banking System

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return
        self.balance += amount
        print(f"Deposited KSh {amount:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
        elif amount > self.balance:           # cannot overdraw
            print("Insufficient funds. Withdrawal refused.")
        else:
            self.balance -= amount
            print(f"Withdrew KSh {amount:,.2f}")

    def display(self):
        print(f"Account {self.account_number} | {self.customer_name} | "
              f"Balance: KSh {self.balance:,.2f}")


def performTransaction(account, kind, amount_text):
    """Process a 'deposit' or 'withdraw'; handles non-numeric amounts."""
    try:
        amount = float(amount_text)
    except ValueError:
        print(f"Invalid amount '{amount_text}'. Please enter a number.")
        return
    if kind == "deposit":
        account.deposit(amount)
    elif kind == "withdraw":
        account.withdraw(amount)
    else:
        print("Unknown transaction type.")


acc1 = BankAccount("ACC1001", "Grace Achieng", 10000)
acc2 = BankAccount("ACC1002", "Samuel Kiprop", 5000)

for acc in (acc1, acc2):
    print(f"\nTransaction for {acc.customer_name}")
    kind = input("Type (deposit/withdraw): ").strip().lower()
    amount_text = input("Amount: ")
    performTransaction(acc, kind, amount_text)

print("\nUpdated balances")
acc1.display()
acc2.display()

f = open("accounts.txt", "w")
for acc in (acc1, acc2):
    f.write(f"{acc.account_number}, {acc.customer_name}, {acc.balance}\n")
f.close()
print("\nAccounts saved to accounts.txt")