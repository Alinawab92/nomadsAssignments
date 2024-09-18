# main.py
from vehicle import Vehicle
from customer import Customer
from carwash import Tier3
from worker import Worker
from entryrecord import EntryRecord

# examples uses
if __name__ == "__main__":
    # Creating objects
    vehicle = Vehicle("Hybrid", "2024")
    customer = Customer("Ali", "haider2@gmail.com", "11-11-2023", vehicle)
    worker = Worker(123, 88000, "Accountant")
    car_wash = Tier3(500, worker)
    entry = EntryRecord("10:00 AM", "11:00 AM", car_wash, customer, vehicle)
    worker1 = Worker(234, 33000, "Manager")

    # Output details
    print(entry.get_details())
    print(worker1.display_details())
    print(worker1.display_full_history())

