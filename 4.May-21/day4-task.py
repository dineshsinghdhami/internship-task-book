# Prime Number Finder
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")
else:
    print("Not Prime Number")



# Factorial
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)



# Armstrong Number
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10
if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")