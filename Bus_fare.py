class Vehical:
    def __init__(self, capacity):
        self.capacity = capacity
class tickets(Vehical):
    def __init__(self, capacity):
        super().__init__(capacity) 
        self.price = self.capacity * 10 
    def show(self):
        print("Ticket Price:", (self.price))
obj = tickets(100)
obj.show()