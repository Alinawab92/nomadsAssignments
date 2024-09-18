from worker import Worker
class CarWash:
    def __init__(self, wash_price):
        self.wash_price = wash_price

    def perform_wash(self):
        if self.wash_price == 100:
            return "Rs.100 for soap only"
        elif self.wash_price == 200:
            return "Rs.200 for soap and polish"
        elif self.wash_price == 500:
            return "Rs.500 for soap, polish, and inner clean"
        else:
            return "Invalid amount"

class Tier1(CarWash):
    def __init__(self, wash_price):
        super().__init__(wash_price)

    def apply_basic_service(self):
        if self.wash_price == 100:
            return "Applying soap only wash"
        else:
            return "Invalid amount"

class Tier2(CarWash):
    def __init__(self, wash_price):
        super().__init__(wash_price)

    def apply_extra_service(self):
        if self.wash_price == 200:
            return "Applying soap and polish wash"
        else:
            return "Invalid amount"

class Tier3(CarWash):
    def __init__(self, wash_price, worker):
        super().__init__(wash_price)
        self.worker = worker  # Has-a Worker

    def apply_luxury_service(self):
        if self.wash_price == 500:
            return f"Applying soap, polish, and inner clean wash by {self.worker.get_worker_details()}"
        else:
            return "Invalid amount"



