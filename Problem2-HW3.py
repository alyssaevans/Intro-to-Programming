#Author: Alyssa Evans
#File: AlyssaEvans-p2HW3.py
#Hwk #: 3 - Magic Dates

month = int(input("Enter a month (MM): "))
if (month > 12) or (month < 0):
        print ("Months can only be from 01 to 12.")

day = int(input("Enter a day (DD): "))
if (month % 2 == 0) and (day > 30) or (day < 0):
	print("Incorrect amount of days for that month.")
if (month % 2 != 0) and (day > 31) or (day < 0):
	print("Incorrect amount of days for that month")
if (month == 2) and (day > 29):
	print("February has a maximum of 29 days.")
                
year = int(input("Enter a year (YY): "))
if (year > 10):
        print("You have to enter a two digit year.")

if (month * day == year):
	print("The date you chose is magic!")
else:
	print("The date you chose isn't magic.")
	


