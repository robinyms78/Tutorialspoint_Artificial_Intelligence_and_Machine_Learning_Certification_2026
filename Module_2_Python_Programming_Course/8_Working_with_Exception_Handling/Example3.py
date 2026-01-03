# Exception Handling in Python

try:
    print(1/0)
except:
    print("Raised exception caught")
finally:
    print("Bye from finally block")
print("Bye")