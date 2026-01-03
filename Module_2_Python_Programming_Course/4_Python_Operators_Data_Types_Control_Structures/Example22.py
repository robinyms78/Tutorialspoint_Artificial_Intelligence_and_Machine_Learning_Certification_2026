# Creating a set with {} braces
fruits = {"banana", "apple", "orange"}
print(fruits)
print(fruits)
print(fruits)

# Loop through the set
for s in fruits:
    print(s)

# Add bew item in set with add()
fruits.add("Kiwi")
print(fruits)

# Add multiple items with update()
fruits.update(["grapes", "guava"])
print(fruits)

# Finding the length of the set using len() method
print("The length of the set is", +len(fruits))

# Removing the item from the set using remove()
fruits.remove("grapes")
fruits.discard("Kiwi")
print(fruits) 

# Empty the set using clear()
fruits.clear()
print(fruits)

# Delete the set using del keyword
del fruits
print(fruits)