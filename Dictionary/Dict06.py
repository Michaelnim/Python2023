# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Asking for the length of the dictionary
def generate_dict(length):
    # Creating new dict
    new_dict = {}
    # Iterating through dict starting from 1 ~ 6
    for i in range(1,length+1):
        #Adding [i] to key = value i*i
        new_dict[i] = i*i
    # return new_dictionary
    return new_dict

print(generate_dict(5))

       