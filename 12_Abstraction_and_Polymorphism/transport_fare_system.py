# Topic 12, Task 2: Transport Fare System

class Vehicle:
    def calculateFare(self, distance):
        raise NotImplementedError("Subclasses must implement calculateFare()")


class Bus(Vehicle):
    def calculateFare(self, distance):
        return distance * 50    # Fare 


class Taxi(Vehicle):
    def calculateFare(self, distance):
        return distance * 100    # Fare



bus = Bus()
taxi = Taxi()
distance = 10   # kilometres

print(f"Bus fare for {distance} km: KSh {bus.calculateFare(distance)}")
print(f"Taxi fare for {distance} km: KSh {taxi.calculateFare(distance)}")

print()
print("Explanation: both objects are called with the same method name,")
print("calculateFare(), but each class overrides it with its own formula")
print("(Bus: 50 per km, Taxi: 100 per km). Python chooses the version that")
print("belongs to the object - this is polymorphism (method overriding).")