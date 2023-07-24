# 16. Write a Python program to get a dictionary from an object's fields.

# Creating class
class dictObj:
    # Constructor (method)
    def __init__(self):
        self.r = "red"
        self.b = "blue"
        self.g = "green"
    # Printing out string
    def sysout(self):
        print("Objects of dict are: ")

# Variables
color = dictObj()
color.sysout()
print(color.__dict__)