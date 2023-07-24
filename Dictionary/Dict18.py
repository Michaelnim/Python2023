# 18. Write a Python program to check if a dictionary is empty or not.

# Function to return if dict is empty or not
def isempty(dict):
    # not operator inverts dont have to use it could use len
    return "Dict is empty" if not dict else "Dict is not empty"

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {}

print(isempty(dict1))
print(isempty(dict2))