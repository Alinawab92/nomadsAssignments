from customer import Customer
from vehicle import Vehicle
from carwash import CarWash

# EntryRecord class
class EntryRecord:
    def __init__(self, time_in, time_out, wash_price, membership_date, vehicle_type, model):
        self.time_in = time_in
        self.time_out = time_out
        self.car_wash = CarWash(wash_price)
        self.customer = Customer("John Doe", "john.doe@example.com", membership_date, vehicle_type, model)
        self.vehicle = Vehicle(vehicle_type, model)

    def update(self, time_in, time_out):
        self.time_in = time_in
        self.time_out = time_out
        return f"Time In: {self.time_in}, Time Out: {self.time_out} updated"

    def get_details(self):
        return (f"Check IN: {self.time_in}, Check OUT: {self.time_out}, "
                f"{self.customer.get_customer_details()}, "
                f"{self.vehicle.get_vehicle_details()}, "
                f"Wash Details: {self.car_wash.perform_wash()}")




