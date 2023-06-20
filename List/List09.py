# 9. Write a Python program to clone or copy a list.

# Returns a copy of list
def copy_list(list):
    return list.copy()

# list of numbers
num_list = [1,2,3,4,5]

# Calling for function
print(copy_list(num_list))