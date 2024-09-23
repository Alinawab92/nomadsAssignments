from carwash import CarWash
class Tier2(CarWash):
    def __init__(self, extra_service):
        super().__init__(extra_service)
        self.extra_service = extra_service

    def perform_wash(self):
        if self.extra_service == 200:
            return "Applying soap and polish wash"
        else:
            return "Invalid amount"