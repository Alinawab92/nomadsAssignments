from person import Person
from vehicle import Vehicle


# Customer class
class Customer(Person):
    def __init__(
        self, name, email, membership_date, vehicle_type, model
    ):
        super().__init__(name, email)
        self.membership_date = membership_date
        self.vehicle = Vehicle(vehicle_type, model)

    def payment_process(self, amount):
        return f"{self.name}, your final amount is {amount}"

    def get_customer_details(self):
        return (
            f"Name: {self.name}, Email: {self.email}, "
            f"Membership Date: {self.membership_date}, "
            f"Vehicle: {self.vehicle.get_vehicle_details()}"
        )
