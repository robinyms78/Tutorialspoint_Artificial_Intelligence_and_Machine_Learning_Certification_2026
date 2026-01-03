# Creating and printing a dictionary
cardict = {"brand": "Ford", "name": "Mustang", "year": 2000}
print(cardict)

# Access the values from dictionary
print("The brand of the car is:",cardict["brand"])
print("The Name of the car is:",cardict.get("name"))

# Change the values in the dictionary
cardict["year"] = 2010
print(cardict)

# Accessing key values in the dictionary
for key in cardict:
    print(key)

# Print all the values in the dictionary
for key, values in cardict.items():
    print(key, values)

# Check whther the key exists or not in dictionary
if "brand" in cardict:
    print("Brand exists")
else:
    print("Brand does not exists")

# Finding the length of the dictionary
print("The length of the dicitonary is", +len(cardict))

# Adding new items(key-pair) in the dictionary
cardict["colour"] = "red"
print(cardict)

# Removing the items from dictionary using pop()
cardict.pop("colour")
print(cardict)

cardict.popitem()
print(cardict)

# copy dictionary
newdict = cardict.copy()
print(newdict)

# clear the dictionary using clear()
cardict.clear()
print(cardict)