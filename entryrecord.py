from vehicle import Vehicle
from carwash import CarWash
from customer import Customer

class EntryRecord:
    def __init__(self, time_in, time_out, car_wash: CarWash, customer: Customer, vehicle: Vehicle):
        self.time_in = time_in
        self.time_out = time_out
        self.car_wash = car_wash  # Has-a CarWash
        self.customer = customer  # Has-a Customer
        self.vehicle = vehicle  # Has-a Vehicle

    def update(self, time_in, time_out):
        self.time_in = time_in
        self.time_out = time_out
        return f"Time In: {self.time_in}, Time Out: {self.time_out} updated"

    def get_details(self):
        return (f"Check IN: {self.time_in}, Time Out: {self.time_out}, "
                f"{self.customer.get_customer_details()}, "
                f"{self.vehicle.get_vehicle_details()}, "
                f"Wash Details: {self.car_wash.perform_wash()}")
