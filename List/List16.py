# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# Prints out square of numbers from 1 ~ 30
def sqrt():
    # Created an empty list
    new_list = []
    # Iterating through 1 ~ 30
    for i in range(1,31):
        # Taking each number **2
        new_list.append(i**2)
    #Print the list from 0 ~ 4
    print(new_list[:5])
    #Print the list 31 ~ 26
    print(new_list[-5:])

sqrt()

