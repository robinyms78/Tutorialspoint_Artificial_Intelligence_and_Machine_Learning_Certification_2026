# Creating a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print("The name is:"+self.name)
        print("The name is:",+self.age)

# Creating an object
p1 = Person("John", 35)
p2 = Person("Kelly", 30)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
p1.print_data()
p2.print_data()