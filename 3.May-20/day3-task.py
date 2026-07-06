# Reverse a Number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed Number:", reverse)



# Palindrome Checker
num = input("Enter a number or string: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



# Fibonacci Series
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c