# Abstract Classes and Interface in Python

from abc import ABC, abstractmethod

# Abstract class or interface
class MyClass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass

class sub1(MyClass):
    def calculate(self, x):
        print("The square is:", x*x)

import math
class sub2(MyClass):
    def calculate(self, x):
        print("The square root is:", math.sqrt(x))

# Create objects
s1 = sub1()
s1.calculate(16)

s2 = sub2()
s2.calculate(16)