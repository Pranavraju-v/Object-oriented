class MyClass:
    __private_var=27
    def __priveMeth(self):
        print("Private message")
    def hello(self):
        print(MyClass.__private_var)
obj=MyClass()
obj.hello()
obj.__priveMeth()