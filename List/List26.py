# 26. Write a Python program to check whether two lists are circularly identical.

# Using map function to iterate through lists and comparing them to list1
# If the other lists have all elements confirmed then return True
def identical_list(l1, l2):
    return "".join(map(str, l2)) in "".join(map(str, l1 * 2))

list1 = [1,1,1,1,0]
list2 = [1,1,1]
list3 = [0,1,2]

print(identical_list(list1,list2))
print(identical_list(list1,list3))
