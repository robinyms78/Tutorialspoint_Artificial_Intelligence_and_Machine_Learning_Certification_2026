# File Handling in Python

# Create a file with open
f = open("file1.txt", "w")

# Writing in the file with write()
f.write("Welcome to python session  \n")
f.write("Of file handling") 
f.close()

f = open("file1.txt", "r")

# Read the contents with read()
print(f.read(4))
print(f.read())
print("The current file pointer position is: ", f.tell())
f.seek(0)
print("The current file pointer position is: ", f.tell())
print(f.read())

# Close file
f.close()