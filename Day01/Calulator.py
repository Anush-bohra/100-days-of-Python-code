def add(x ,y):
    return x + y

def subtract(x ,y):
    return x - y

def multiply(x ,y):
    return x * y

def divide(x ,y):
    if y != 0:
        return x / y
    else:
        return "Division by zero error"
    
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", add(input1, input2))
elif operation == "-":
    print("Result:", subtract(input1, input2))
elif operation == "*":
    print("Result:", multiply(input1, input2))
elif operation == "/":
    print("Result:", divide(input1, input2))
else:
    print("Invalid operation")