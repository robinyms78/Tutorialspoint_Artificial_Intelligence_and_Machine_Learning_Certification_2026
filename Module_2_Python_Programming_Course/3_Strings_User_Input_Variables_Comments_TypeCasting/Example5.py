# Python strings operations

string1 = "Hello how are you"
string2 = 'I am fine'
print("First String is:" +string1)
print("Second String is:" +string2)

# Extracting specific character from string
# index or position value starts with 0.
print("The character at 5th position is:", string1[4])

# Extracting a substring
print("The substring is:"+string1[0:5])

# Using Strip() to remove whiet spaces
print("String after removing White spaces is:"+string1.strip())

# Using Lower() to convert string in lower case
print("The converted lower case string is:"+string1.lower())

# Using Upper() to convert string in upper case
print("The converted upper case string is:"+string1.upper())

# Using replace() to replace the characters in string
print("The replaced new string is:"+string1.replace("H", "J"))

# Using split() to split the sentence
print(string1.split(" "))