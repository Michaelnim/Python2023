# 29. Write a Python program to get unique values from a list.

# Function to return only one number of the same element
# Used set 
def unique(list):
    return set(list)

l1 = [1,1,2,2,3,3,4,4,5,5]

print(unique(l1))