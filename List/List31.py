# 31. Write a Python program to count the number of elements in a list within a specified range.

# Asking for user to for list min number max number
# counting min max and everything in between
def count_element(list, min, max):
    count = 0
    for i in list:
        if min <= i <= max:
            count += 1
    return count

list1 = [10,20,30,40,40,40,70,80,99]

print(count_element(list1,10,40))