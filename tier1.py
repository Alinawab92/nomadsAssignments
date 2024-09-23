from carwash import CarWash
class Tier1(CarWash):
    def __init__(self, basic_service):
        super().__init__(basic_service)
        self.basic_service = basic_service

    def perform_wash(self):
        if self.basic_service == 100:
            return "Applying soap only wash"
        else:
            return "Invalid amount"