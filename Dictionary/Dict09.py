# 9. Write a Python program to iterate over dictionaries using for loops.

# For loop to iterate through dictionary
# remember for dictionary have to use .items() 
def iterate(dict):
    for key, value in dict.items():
        print(key, value)
    

dict1 = {1: "person", 2: "animal", 3: "thing", 4: 1000}


print(iterate(dict1))