# 13. Write a Python program to map two lists into a dictionary.

# Using dict() and zip function to fuse 2 lists into a dictionary
# only works if both lists are same size 
# if diff size use zip_longest()
def merge_dict(list1,list2):
    dict1 = dict(zip(list1,list2))
    return dict1

l1 = [1,2,3,4]
l2 = ["a","b","c","d"]

print(merge_dict(l1,l2))