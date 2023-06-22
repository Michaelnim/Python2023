# 19. Write a Python program to calculate the difference between the two lists.

# Comparing two lists using sum() function
def compare(l1, l2):
    return abs(sum(l1) - sum(l2))

# Testing variables
list1 = [1,2,3]
list2 = [1,2,4]

print(compare(list1, list2))