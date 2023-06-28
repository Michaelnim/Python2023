# 22. Write a Python program to count the number 4 in a given list.

# Function using count() to count how many 4's are in arr
def count_4(arr):
    count = arr.count(4)
    return count

# Testing variable
arr = [1,2,3,4,4]

# Returns 2
print(count_4(arr))