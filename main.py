from person import Person
from customer import Customer
from worker import Worker
from registration import Registration
from car_wash import CarWash, SoapOnly, ExtraService, LuxuryService
from regist_record import RegistRecord


if __name__ == "__main__":
    # Test CarWash and its derived classes
    p1 = CarWash(100)
    print(p1.perform_wash())
    
    p2 = SoapOnly(100)
    print(p2.apply_basic_service())

    p3 = ExtraService(200)
    print(p3.apply_extra_service())

    p4 = LuxuryService(500)
    print(p4.apply_luxury_service())

    # Test Customer class
    c1 = Customer("Alice", "alice@example.com", "12-12-2000")
    print(c1.membership_date)
    print(c1.payment_process(13000))

    # Test Person class (check-in, check-out)
    c2 = Person("Ali", "bisma@gmail.com")
    print(c2.check_in())
    print(c2.check_out())

    # Test Worker class with RegistRecord
    w1 = Worker("Noman", "noman.doe@gmail.com", 50000, "Engineer")
    w2 = Worker("kashif", "kashif.ali@gmail.com", 55000, "Manager")
    w3 = Worker("Abdullah", "abd@gmail.com", 550, "Technician")

    # Display worker details and history
    print(w3.display_details())

    # Change position for w3 and add to history
    w3.change_position("Supervisor")
    w3.change_position("Manager")

    # Show full position history for w3
    print(w3.display_full_history())

    # Example usage of Registration class
    r1 = Registration("3:00", "5:00", "2nd time comes")
    print(r1.update("10:00", "2:00", "4th time comes"))
    print(r1.get_details())

