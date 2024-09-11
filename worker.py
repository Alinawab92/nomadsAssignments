from person import Person
from regist_record import RegistRecord  # Correct import

class Worker(Person):
    workers_list = []

    def __init__(self, name, email, salary, position):
        super().__init__(name, email)
        self.salary = salary
        Worker.add_worker(self)

        # Initialize RegistRecord correctly
        self.regist_record = RegistRecord()  # Use RegistRecord, not Regist_Record
        self.regist_record.add_record(position)

    @classmethod
    def add_worker(cls, worker):
        cls.workers_list.append(worker)

    def change_position(self, new_position):
        self.regist_record.add_record(new_position)

    def display_details(self):
        return (f"Name: {self.name}, Email: {self.email}, Salary: {self.salary}, "
                f"{self.regist_record.get_status()}")

    def display_full_history(self):
        return self.regist_record.show_history()
