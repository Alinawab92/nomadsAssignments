class Registration:
    def __init__(self, time_in, time_out, car_track):
        self.time_in = time_in
        self.time_out = time_out
        self.car_track = car_track

    def update(self, time_in, time_out, car_track):
        self.time_in = time_in
        self.time_out = time_out
        self.car_track = car_track
        return f"{self.time_in}, {self.time_out} and {self.car_track} updated"

    def get_details(self): 
        return f"Check IN: {self.time_in}, Time Out: {self.time_out}, Car Tracker: {self.car_track}"
    
