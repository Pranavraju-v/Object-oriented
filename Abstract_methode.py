from abc import ABC, abstractmethod
class abc:
    def print(self, x):
        print(x)
    @abstractmethod
    def task(self):
        print("We are in abs methode")
class testclass(abc):
    def task(self):
        print("We are inside testclass task")
testobj=testclass()
testobj.task()
testobj.print(100)