file = open('test.txt')
print(file.read()) # read all the contents of file
file.close()
file = open('test.txt')

print("\n")
print(file.read(2)) # read first 2 characters or bites
file.close()

file = open('test.txt')
print("\n")
print(file.readline()) # reads one line at the time
file.close()

file = open('test.txt')
print("\n")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

# another method not mentioned
print("\n")
with open('test.txt') as file_object:
    contents = file_object.read()
print(contents)


# another method not mentioned / ok this was mentioned
print("\n")
with open('test.txt') as file_object:
    for line in file_object:
        print(line)