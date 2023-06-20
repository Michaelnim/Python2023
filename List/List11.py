# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

# Function that compares 2 lists
def one_common(l1,l2):
    # Iterating through l1 (list1)
    for i in l1:
        # Comparing i to see if its in l2
        if i in l2:
            return True
    return False

# Test lists
list1 = [1,2,3,4,5]
list2 = [0,0,0,0,0]

# Calling function (should return false)
print(one_common(list1, list2))