# Write to Text File
file = open("sample.txt", "w")
file.write("Hello Dinesh Singh Dhami\n")
file.write("Welcome to Python Internship\n")
file.write("Learning File Handling")
file.close()
print("Data written successfully")



# Read Text File
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()



# Count Lines and Words
file = open("sample.txt", "r")
content = file.readlines()

line_count = len(content)
word_count = 0

for line in content:
    words = line.split()
    word_count += len(words)

print("Total Lines:", line_count)
print("Total Words:", word_count)

file.close()