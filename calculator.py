# Functions
def add(input1, input2):
    return input1 + input2

def minus(input1, input2):
    return input1 - input2

def divide(input1, input2):
    if input2 != 0: 
        return input1 / input2
    else:
        return "Can't divide by 0"

def multiply(input1, input2):
    return input1 * input2

# operations
operations = {
    '+': add,
    '-': minus,
    '/': divide,
    '*': multiply
}

# input
input1 = int(input("First number: "))
input2 = int(input("Second number: "))
operator = input("Enter operator (+ , - , / , *)")

# Calculate input number based off operator
if operator in operations:
    result = operations[operator](input1, input2)
    print(f"{input1} {operator} {input2} = {result}")
else:
    print("Invalid operator, please try again.")