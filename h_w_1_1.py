# Write a Python program to display the current date and time.
import datetime
current = datetime.datetime.now()
print("current date and time : ")
print(current.strftime("%m/%d/%Y \n%H:%M:%S"))
