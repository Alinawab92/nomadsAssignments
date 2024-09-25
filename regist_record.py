from vehicle import Vehicle
from worker import Worker


class RegistRecord:
    def __init__(self, vehicle_type, model, salary, id):
        self.history = []
        self.vehicle = Vehicle(vehicle_type, model)
        self.worker = Worker(salary, id)

    def add_record(self, position):
        self.history.append(position)
        return f"your current position is Added {self.history} "

    def get_status(self):
        if self.history:
            return f"Current Position: {self.history[-1]}"  # Last added is the current position
        else:
            return "No position assigned"

    def show_history(self):
        if self.history:
            return f"Position History: {', '.join(self.history)},{self.worker.display_details()}"
        else:
            return "No position history available"
