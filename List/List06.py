# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#Function to return sorted list by lowest to highest 2nd element
def sort_tuple(tuple):
    #Using sort method that is set to sort the 2nd element in the tuple
    tuple.sort(key = lambda x:x[1])
    return tuple

#Sample list
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#Calling for function
print(sort_tuple(sample_list))