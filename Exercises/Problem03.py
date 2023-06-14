# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

#Needed to get datetime
from datetime import datetime

#created a today varible to hold method
today = datetime.today()

#printing out datetime in a certain order using % sign
dt_string = today.strftime("%m/%d/%Y %H:%M:%S")
print(dt_string)