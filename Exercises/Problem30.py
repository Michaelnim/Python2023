# 30. Write a Python program that will accept the base and height of a triangle and compute its area.

# Function to return area of a triangle
# Requires user to input height and base
def area_triangle(height,base):
    return (f"Area of the triangle is: {(1/2)*height*base}")


# Testing inputing height and base out -> 400.0
print(area_triangle(20,40)) 