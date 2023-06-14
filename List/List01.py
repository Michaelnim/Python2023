# 1. Write a Python program to sum all the items in a list.

#Created function that accepts a list
def sum_list(l1):
    #Return statement using for-loop
    return sum(x for x in l1)

#Variable to hold the list of nums
num_list = [1,1,1,1,1]

#Printing sum of list
print(sum_list(num_list))