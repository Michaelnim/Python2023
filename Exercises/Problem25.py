# 25. Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# Function to check if num is in list
def contains_num(num, l1):
    return True if num in l1 else False

# Testing variables
list1 = [1,5,8,3]
print(contains_num(3, list1))
print(contains_num(-1, list1))