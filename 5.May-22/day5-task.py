# List Operations
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

numbers.append(60)
print("After adding 60:", numbers)

numbers.remove(30)
print("After removing 30:", numbers)

numbers[1] = 25
print("After updating second element:", numbers)

print("List elements:")
for num in numbers:
    print(num)




# Remove Duplicates
numbers = [10, 20, 30, 20, 40, 10, 50]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original List:", numbers)
print("List after removing duplicates:", unique_numbers)




# Find Second Largest Number
numbers = [10, 25, 40, 15, 50, 35]
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("Second largest number is:", second_largest)