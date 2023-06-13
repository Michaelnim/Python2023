# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

#Created a function that accepts first and last name
def name(first,last):
    #returns last name then first
    return last + " " + first

#Varible to hold function
testing = name("Mike", "Wazowski")

#Printing variable
print(testing)