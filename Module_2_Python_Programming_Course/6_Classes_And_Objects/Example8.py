# Abstract Classes and Interface in Python

from abc import ABC, abstractmethod

#interface
class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class IBM(Printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print("Printing completed by IBM Printer")

class Epson(Printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print("Printing completed by Epson Printer")

obj1 = IBM()
obj1.printit("Print started by IBM")
obj1.disconnect()
obj1 = Epson()
obj1.printit("Print started by Epson")
obj1.disconnect()