from worker import Worker
from carwash import CarWash


class Tier3(CarWash):
    def __init__(self, luxury_service, name, email, salary):
        super().__init__(luxury_service)
        self.luxury_service = luxury_service
        self.worker = Worker(name, email, salary)

    def perform_wash(self):
        if self.luxury_service == 500:
            return f"Applying soap, polish, and inner clean by {self.worker.get_detail()}"
        else:
            return "Invalid amount"
