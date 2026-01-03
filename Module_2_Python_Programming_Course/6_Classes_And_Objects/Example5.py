# Base class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printdata(self):
        print(self.fname, self.lname)

# Child class
class Student(Person):
    pass

# Creating object
student1 = Student("John", "Doe")
student1.printdata()