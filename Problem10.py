# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

#Asking for a number
num = int(input("Enter a number: "))

#Converting num to str in order to concatenating
num2 = str(num)*2
num3 = str(num)*3

#Str -> Int in order to add them together n + nn + nnn = total
#if kept as string it will just be nnnnnn
total = int(num) + int(num2) + int(num3)

#Printing out total using f-string
print(f"The total value of num+num2+num3: {total}")