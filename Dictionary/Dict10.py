# 10. Write a Python program to sum all the items in a dictionary.

# Used sum function to return the sum of all items
# .values() to only use the value in the dictionary and not KEY
def sum_dict(dict):
    return sum(dict.values())

dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

print(sum_dict(dict1))
        