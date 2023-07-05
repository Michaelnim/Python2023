# 4. Write a Python script to check whether a given key already exists in a dictionary.

# Function that asks for users dictionary and key they are looking for
def exists(key,dict):
    if key in dict:
        return "Key is in dictionary"
    return "Key is not in dictionary"


dict1 = {1:10, 2:20}

print(exists(1,dict1))
print(exists(3,dict1))