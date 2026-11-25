# Topic 10, Task 1: Bank Account

class BankAccount:
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = 0.0

    def deposit(self, amount):
        """Add money to the balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Deduct money from the balance."""
        self.balance -= amount

    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: KSh {self.balance:,.2f}")


account = BankAccount()
account.account_number = "ACC1001"
account.customer_name = "Grace Achieng"
account.balance = 10000          # opening balance
account.deposit(5000)
account.withdraw(2000)
account.displayAccount()