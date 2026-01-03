# Array creation
from array import *

int_array = array('i', [10, 20, 30, 40, 50])
for i in int_array:
    print(i)
print("Length of the Array is:",+len(int_array))

# Slicing
print("Slicing output")
print(int_array[1:3])

# Inserting value in array with insert()
int_array.insert(1, 100)
for i in int_array:
    print(i)

# Delete value in array wuth remove()
int_array.remove(100)
for i in int_array:
    print(i)

# Search within an array with index()
print("The position of 30 is", int_array.index(30))

# Updating value in array
int_array[0] = 200
for i in int_array:
    print(i)