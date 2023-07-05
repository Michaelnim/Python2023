# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# Didn't really need a function but wrote one anyways
def square_dict():
    # New dictionary
    new_dict = {}
    # creating length of dictionary using range
    for i in range(1,15+1):
        # new_dict[i] = 1 and will continue to 16
        # squaring the value
        new_dict[i] = i*i
    #returning new dict
    return new_dict

# calling for function
print(square_dict())