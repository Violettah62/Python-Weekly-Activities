# Topic 12, Task 1: Payment System

from abc import ABC, abstractmethod


class Payment(ABC):                # abstract class: cannot be instantiated
    @abstractmethod
    def makePayment(self):
        pass


class MobileMoneyPayment(Payment):
    def makePayment(self):
        print("Payment made using Mobile Money")


class CardPayment(Payment):
    def makePayment(self):
        print("Payment made using Bank Card")


payments = [MobileMoneyPayment(), CardPayment()]
for payment in payments:
    payment.makePayment()      

print()
print("Explanation:")
print("Abstraction: Payment defines WHAT every payment must do (makePayment)")
print("without saying HOW; it cannot be used to create objects directly.")
print("Polymorphism: each subclass implements makePayment() in its own way, so")
print("the same method call gives different results depending on the object.")