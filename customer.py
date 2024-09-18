# customer.py
from person import Person
from vehicle import Vehicle

class Customer(Person):
    def __init__(self, name, email, membership_date, vehicle=None):
        super().__init__(name, email)
        self.membership_date = membership_date
        self.vehicle = vehicle
    
    def payment_process(self, amount):
        return f"{self.name}, your final amount is {amount}"
    
    def get_customer_details(self):
        # Correct method call
        vehicle_details = self.vehicle.get_vehicle_details() if self.vehicle else "No vehicle assigned"
        return (f"Name: {self.name}  Email: {self.email}  Membership Date: {self.membership_date}  Vehicle: {vehicle_details}")

