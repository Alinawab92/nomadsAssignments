class Vehicle:
    def __init__(self, vehicle_type, model):
        self.vehicle_type = vehicle_type
        self.model = model

    def get_vehicle_details(self):
        return f"Your vehicle type is: '{self.vehicle_type}' and model number is: '{self.model}'"


