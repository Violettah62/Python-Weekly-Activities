# Topic 11, Task 3: Transport System

class Vehicle:
    def __init__(self, registration_number, model):
        self.registration_number = registration_number
        self.model = model

    def displayVehicle(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Model: {self.model}")


class Bus(Vehicle):
    def __init__(self, registration_number, model, passenger_capacity):
        super().__init__(registration_number, model)
        self.passenger_capacity = passenger_capacity

    def displayBus(self):
        self.displayVehicle()                  # reuse the parent method
        print(f"Passenger Capacity: {self.passenger_capacity}")


bus = Bus("KDA 123X", "Isuzu NQR", 51)
bus.displayBus()