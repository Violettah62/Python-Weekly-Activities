# Topic 11, Task 2: Bank Accounts

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: KSh {self.balance:,.2f}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate    

    def calculateInterest(self):
        # Interest 
        return self.balance * self.interest_rate / 100


savings = SavingsAccount("SAV3001", 80000, 5)
savings.displayAccount()
print(f"Interest Rate: {savings.interest_rate}%")
print(f"Interest: KSh {savings.calculateInterest():,.2f}")