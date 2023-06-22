# 19. Write a Python program to calculate the difference between the two lists.

# Comparing two lists
def compare(l1, l2):
    # Grabbing the difference from list1 and list2
    # Adding the difference together
    new_list = list(set(l1) - set(l2)) + list(set(l2) - set(l1))
    # Returning it as a new list
    return new_list

# Testing variables
list1 = [1,2,3]
list2 = [1,2,4]

print(compare(list1, list2))