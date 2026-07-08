from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class humen(animal):
    def move(self):
        print("I move with my feet")
class dog(animal):
    def move(self):
        print("I move with my paws")
class cat(animal):
    def move(self):
        print("i also move with my paws")
class snake(animal):
    def move(self):
        print("I slither")

h= humen()
d=dog()
c=cat()
s=snake()

h.move()
d.move()
c.move()
s.move()