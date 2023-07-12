# 32. Write a Python program to check whether a list contains a sublist.

# sub_list has to be in the same order as list or false
def sub_set(list, sub):
    # Keeping count of length for sub_list
    length_count = 0
    # Iterating through the length of list
    for i in range(len(list)):
        # If list[i] == sub[0]; [4] == [4]
        if list[i] == sub[0]:
            # length count + 1
            length_count +=1
            if list[i+length_count] == sub[length_count]:
                return True
    return False


list = [1,2,3,4,5]
sub_list = [3,4]

print(sub_set(list,sub_list))
