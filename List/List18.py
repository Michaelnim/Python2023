# 18. Write a Python program to generate all permutations of a list in Python.

# Module to permutate list
from itertools import permutations

# Function to permutate
def perm(l1):
    # Variable to hold permutation of list
    test = permutations(l1)
    # iterating through test and adding it into new_list
    new_list = [x for x in test]
    return new_list

test = [1,2,3]
print(perm(test))