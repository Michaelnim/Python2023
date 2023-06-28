# 27. Write a Python program that concatenates all elements in a list into a string and returns it.

# Using the join function to convert list into a str and joining them together
def concatenate(l1):
    return "".join(str(x) for x in l1)

# Testing variable
list1 = [1,2,3,4,5]

print(concatenate(list1))