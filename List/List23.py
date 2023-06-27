# 23. Write a Python program to flatten a shallow list.

# Function to take all lists and add them into one
def one_list(l1):
    # new list variable
    new_list = []
    # Iterating through list to add into new_list
    for i in l1:
        new_list += i
    return new_list

# Testing lists
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]

print(one_list(original_list))