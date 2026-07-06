# Triangle Pattern problem
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()



# Pyramid Pattern Problem
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()



# Odd/Even Checker
print("Welcome to Odd/Even Checker")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")



# Largest Among 3 Numbers
print("Welcome to Largest Number Checker")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)