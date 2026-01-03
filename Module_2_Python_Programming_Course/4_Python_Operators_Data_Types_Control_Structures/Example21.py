# Creating a tuple with () brackets
fruits = ("Banana", "Kiwi", "Orange")
print(fruits)

# Access the item from the tuple
print(fruits[1])

# Selecting the items from the tuple one by one
for t in fruits:
    print(t)

# To check whether the item exists or not
if "apple" in fruits:
    print("Apple exists in tuple")
else:
    print("Apple does not exists in tuple")

# To find the length of the tuple with len()
print("The length of the tuple is:", +len(fruits))

# Delete the tuple completely with del
del fruits
print(fruits)
