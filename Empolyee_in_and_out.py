class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructer called")
def Creat_object():
    print("Starting prosess.....")
    obj=Employee()
    print("Prosess done...")
    return obj
print("Calling x")
obj = Creat_object()
print("End of code..")