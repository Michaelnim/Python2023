# 12. Write a Python program to remove a key from a dictionary.

# Asking user for the key they want to del
# can use pop() as well dict.pop(key)
def remove_key(key,dict):
    del dict[key]
    return dict


dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

print(remove_key(1,dict1))