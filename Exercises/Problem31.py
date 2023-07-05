# 31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

import math
# Used import math
def gcd(num1,num2):
    # returned greatest common divisor
    return math.gcd(num1,num2)

print(gcd(3,6))

# Another way to return gcd
# Using 2nd testing variable (4,6)
def gcd(x, y):
 # z will hold the remainder
 # z = 4
 z = x % y
 # While z != 0
 while z:
   # x = 6 -> x = 4
   x = y
   # y = 4 -> y = 2
   y = z
   # z = 2 -> z = 0
   z = x % y
 return y
print("GCD of 12 & 17 =",gcd(2, 2))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))