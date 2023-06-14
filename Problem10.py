# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

num = int(input("Enter a number: "))
num2 = str(num)*2
num3 = str(num)*3
total = int(num) + int(num2) + int(num3)
print(f"The total value of num+num2+num3: {total}")