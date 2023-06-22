# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# Return True if num <= 100 else False
def between(num):
    return True if abs(1000 - num) <= 100 or abs(2000 - num) <= 100 else False

# Variable
num1 = 900

#Calling function
print(between(num1))