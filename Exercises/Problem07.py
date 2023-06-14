# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

#Created input for filename
filename = str(input("Please type in a file name: "))
#Splited the filename by (".")
file_split = filename.split(".")
#Printed the extension
print(file_split[1])
