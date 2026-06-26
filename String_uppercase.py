class IOString:
    def __init__(self):
        self.str1=""
    def input1(self):
        self.str1=input("Enter str: ")
    def print1(self):
        print("Result is:", self.str1.upper())
str1=IOString()
str1.input1()
str1.print1()