# 11. Write a Python program to multiply all the items in a dictionary.

# Multiplying all the values
def multi_items(dict):
    # product variable to hold 
    product = 1
    for key, value in dict.items():
        product *= value
    return product

dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

print(multi_items(dict1))