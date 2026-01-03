# Creating a class
class Person:

    def insert_data(self):
        self.name = input("Enter the name:")
        self.age = int(input("Enter the age:"))

    def print_data(self):
        print("The name is:"+self.name)
        print("The name is:" ,+self.age)

# Creating an object
p1 = Person()
p2 = Person()
p1.insert_data()
p1.print_data()
p2.insert_data()
p2.print_data()