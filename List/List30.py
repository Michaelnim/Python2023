# 30. Write a Python program to get the frequency of elements in a list.

# Function to count how many elements are the same using dictionary
# Key, value
def count_elements(list):
    # Creating a dictionary
    count = dict()
    # iterating through list to get elements and keep count
    for i in list:
        count[i] = count.get(i, 0) + 1
    return count

l1 = [1,1,1,2,2,3,3,4,5,10,10,10]

print(count_elements(l1))