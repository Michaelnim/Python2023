# 24. Write a Python program to append a list to the second list.

# Appending 2 lists into one
def merge_two(l1,l2):
    # Iterating through l2 and appending it to l1
    for i in l2:
        l1.append(i)
    return l1
    
# Testing lists
list1 = ["red","blue","green"]
list2 = [0,1,2]

print(merge_two(list1,list2))