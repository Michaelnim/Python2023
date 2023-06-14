# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

#User input for numbers with commas
numbers = input("Enter comma seperated numbers: ")

#Spliting the numbers by commas
comma_split = numbers.split(",")

#Printing out comma_split into list/tuple
print(list(comma_split))
print(tuple(comma_split))
