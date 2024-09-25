class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def check_in(self):
        return f"{self.name} is checked IN"

    def check_out(self):
        return f"{self.name} is checked OUT"
