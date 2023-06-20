# 7. Write a Python program to remove duplicates from a list.

#Function to remove duplicates from list
def dup_remove(list):
    #Created a new list to hold the new data
    new_list = []
    #for loop to iterate through the list
    for i in list:
        #If statement (if i isn't in new_list then append it)
        if i not in new_list:
            new_list.append(i)
    return new_list

#List
testing = [1,1,2,2,3,4]
#calling for function
print(dup_remove(testing))