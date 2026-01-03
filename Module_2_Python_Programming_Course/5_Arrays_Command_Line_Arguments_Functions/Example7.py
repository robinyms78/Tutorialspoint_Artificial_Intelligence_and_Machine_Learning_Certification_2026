# Return Values
# Addition of two numbers using function

def sum_nos(no1, no2):
    add_nos = no1 + no2
    return add_nos

number1 = int(input("Enter the no1:"))
number2 = int(input("Enter the no2:"))

addition_nos = sum_nos(number1, number2)
print("The addition is:",+addition_nos)