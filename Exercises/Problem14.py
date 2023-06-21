# 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# Date given above find the days between two dates
dates = (2014, 7, 2), (2014, 7, 11)

# Variable to hold the 2nd element in the tuple
# must you map in order to iterate through the tuple to find index needed
days = list(map(lambda x:x[2], dates))

# Taking the 2nd element of both tuple and subtracting
print(abs(days[0] - days[1]))

