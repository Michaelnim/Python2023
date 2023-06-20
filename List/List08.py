# 8. Write a Python program to check if a list is empty or not.

# A return statment to tell user if list is empty or not
def check_empty(list):
    return "List is not empty" if len(list) > 0 else "List is empty"

# 2 list variables one empty one not
empty_list = []
num_list = [1,2,3,4,5]

# Calling for function to see if it works
print(check_empty(empty_list))
print(check_empty(num_list))