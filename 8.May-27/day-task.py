# Reusable Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))




# Lambda Exercises
square = lambda x: x * x
add = lambda a, b: a + b
multiply = lambda a, b: a * b

print(square(5))
print(add(10, 20))
print(multiply(5, 6))