from person import Person

# Worker class
class Worker(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary
        self.history = []

    def get_detail(self):
        return f"{self.name} and email: {self.email} and salary: {self.salary}"

    def employing_worker(self, position):
        self.history.append(position)
        return f"Position {position} added to history."

    def show_history(self):
        if self.history:
            return f"Position History: {', '.join(self.history)}"
        else:
            return "No position history available"



    

