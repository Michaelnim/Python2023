# 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

# Function to print first 2 letters of string x number of times
# If x <= 0 return "Error message"
def n_copies(str,n):
    if n <= 0:
        return "Error can't use negative numbers or 0"
    return str[:2] * n

# Testing variables
print(n_copies("red",3))
print(n_copies("p",10))
print(n_copies("red",0))