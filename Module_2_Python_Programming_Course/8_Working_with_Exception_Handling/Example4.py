# Exception Handling in Python

try:
    x = int(input('Enter the no between 5 and 10:'))
    assert x>=5 and x<=10, "Your input is not correct"
    print('The number entered', x)
except AssertionError as obj:
    print(obj)