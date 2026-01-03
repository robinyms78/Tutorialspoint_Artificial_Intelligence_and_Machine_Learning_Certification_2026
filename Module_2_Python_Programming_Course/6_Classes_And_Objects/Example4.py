# Creating a class
class Sample:
    def __init__(self):
        self.x = 10

    def modify(self):
        self.x = input("Enter the new value of x: ")

    def print_data(self):
        print("The value of x is",self.x)

# Create the objects
s1 = Sample()
s1.print_data()
s1.modify()
s1.print_data()