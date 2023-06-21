# 15. Write a Python program to get the volume of a sphere with radius six.

# Imported math mod to use pi
import math

# Function to return volume of sphere
def volume_sphere(radius):
    return (4/3)*math.pi*radius**3

# Radius of sphere
radius = 6

print(volume_sphere(radius))