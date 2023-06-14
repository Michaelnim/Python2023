# 2. Write a Python program to multiply all the items in a list.

#Function to multply a list
def mult_list(list):
    #Variable to hold the total
    total = 1
    #For loop to iterate through the list
    for i in list:
        total *= i
    return total

#num list
num = [1,2,3,4,5]
#Printing out total of num
print(mult_list(num))