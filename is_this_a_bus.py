class vehicle:
    def __init__(self, name, max_speed, milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
    def show(self):
        print(self.name)
        print(self.max_speed)
        print(self.milage)
class bus(vehicle):
    pass
obj=bus("Volovo", 190, 80)
obj.show()