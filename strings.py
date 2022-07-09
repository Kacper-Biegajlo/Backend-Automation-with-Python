str = "Kacper.Biegajło"
str1 = "Consulting firm"
str3 = "Kacper"

print(str[1])

print(str[0:6]) #prints Kacper part of string

print(str+" "+str1) # concatenation

print(str3 in str) # substring check

var = str.split(".") # how to split a string
print(var)
print(var[0]) # extracting part of the string after split

str4 = " great "
print(str4.strip()) # removing whitespaces from string
print(str4.lstrip()) # removing whitespaces from string on the left
print(str4.rstrip()) # removing whitespaces from string on the left