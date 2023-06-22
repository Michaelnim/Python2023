# 20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# Returning string number of strings
# Error if n < 0
def copies(n,str):
    return (str+" ") * n if n > 0 else "Error can't do negative numbers!"
 
# Variables to test
print(copies(2,"Hello world"))
print(copies(3, "Testing"))
print(copies(0, "Error"))