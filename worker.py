from regist_record import RegistRecord

class Worker:
    workers_list = []

    def __init__(self, worker_id, salary, position):
        self.worker_id = worker_id
        self.salary = salary
        self.position = position
        self.regist_record = RegistRecord()  # Initialize RegistRecord
        self.regist_record.add_record(position)
        Worker.add_worker(self)

    @classmethod
    def add_worker(cls, worker):
        cls.workers_list.append(worker)

    def change_position(self, new_position):
        self.regist_record.add_record(new_position)

    def display_details(self):
        return (f"Worker ID: {self.worker_id}, Salary: {self.salary}, ")
                #f"Position: {self.position}, {self.regist_record.get_status()}")

    def display_full_history(self):
        return self.regist_record.show_history()
    

