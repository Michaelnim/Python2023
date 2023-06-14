# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

#Imported math to use pi
import math

#Creating a function to return area of circle (non side effect)
def circle_radius(r):
    return math.pi*(r**2)

#Creating varible to use function
area = circle_radius(1.1)
print(area)