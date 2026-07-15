class book:
    def __init__(self, titel, auther, is_borrowed):
        self.titel=titel
        self.auther=auther
        self.is_borrowed=True
    def borrowed(self):
        if self.is_borrowed==True:
            print("not Avalibel")
    def return_book(self):
        self.is_borrowed=False
        print("avalibel")
    def show(self):
        print(self.titel)
        print(self.auther)
obj1=book("Harry potter", "JK Rowling", True)
obj2=book("Jujutsu Kaisan", "Gege atumaki", True)
obj3=book("Dictioary", "Langenscheidet", True)

obj1.show()
obj2.show()
obj3.show()

obj1.borrowed()
obj2.borrowed()
obj3.borrowed()

obj1.return_book()
obj2.return_book()
obj3.return_book()