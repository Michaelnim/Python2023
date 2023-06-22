# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

# Check if the first 2 letters are is
# changed str to lower for case sensitivity
def prefix(str):
    test = str.lower()
    # Tests if first 2 letters are is
    if test[0:2] != "is":
        return "Is" + str
    return str

# Variables to test 
array = "array"
isarray = "isArray"

print(prefix(array))
print(prefix(isarray))