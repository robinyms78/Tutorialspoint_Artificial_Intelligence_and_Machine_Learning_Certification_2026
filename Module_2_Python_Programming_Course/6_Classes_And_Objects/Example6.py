# Base class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printdata(self):
        print(self.fname, self.lname)

# Child class
class Student(Person):
    def __init__(self, fname, lname, gradyear):
        super().__init__(fname, lname)
        self.gradyear = gradyear

    def welcome(self):
        print("Welcome", self.fname, self.lname, "To the class of", self.gradyear)

# Creating object
student1 = Student("John", "Doe", 2021)
student1.welcome()