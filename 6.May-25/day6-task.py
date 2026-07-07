# Dictionary Frequency Counter
numbers = [1, 2, 3, 2, 1, 4, 3, 2]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)



# Character Count in String
text = input("Enter a string: ")
count = 0
for char in text:
    count += 1
print("Total characters:", count)



# Word Count
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words:", len(words))