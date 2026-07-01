class person:
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self, name, idnumber, salery, post):
        self.salery=salery
        self.post=post
        person.__init__(self, name, idnumber)
    def display1(self):
        print(self.salery)
        print(self.post)
obj=employee("Max", 19234, 2000, "Intern")
obj.display()
obj.display1()