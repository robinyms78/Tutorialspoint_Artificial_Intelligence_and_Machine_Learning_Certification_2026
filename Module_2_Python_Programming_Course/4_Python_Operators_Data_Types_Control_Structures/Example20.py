# Create a list
fruits = ["Banana", "apple", "orange", "kiwi"]
print(fruits)

# Access specific item from the list by index value
print(fruits[2])

# Change item value in the list by index
fruits[2] = "Blackcurrent"
print(fruits)

# Print all the items one by one
for fr in fruits:
    print(fr)

# Check specific item exists or not
if "Blackcurrent" in fruits:
    print("Blackcurrent exists in the list")
else:
    print("Blackcurrent does not exist in the list")

# Find length of the list
print("The length of the list is: ", +len(fruits))

# Add items with append() at the end
fruits.append("orange")
print(fruits)

# Add items with insert() using specific index
fruits.insert(2, "mango")
print(fruits)

# Remove an item with remove() by item name
fruits.remove("mango")
print(fruits)

# Remove an item with pop()
fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

# Copy one list to another using copy()
newlist = fruits.copy()
print(newlist)