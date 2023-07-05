# 5. Write a Python program to iterate over dictionaries using for loops.

# Iterating through the dictionary and printing key and value
def iterate(dict):
    for key, value in dict.items():
        print(f"{key} --> {value}")

# Testing dict
d = {'x': 10, 'y': 20, 'z': 30} 

# calling function
iterate(d)