# 22. Write a Python program to find the index of an item in a specified list.

# Requesting for number
index = input(str("What number are you looking for? "))
# Testing list
testing = [1,10,3,2,5]

# Iterating through list using length to find index
for i in range(len(testing)):
    # convert index into str to be sure its in the list
    if int(index) == testing[i]:
        print("Number is at index:",i)
        break
    else:
        print("Error number not in list")
        break