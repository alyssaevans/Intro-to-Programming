#Author: Alyssa Evans
#File: AlyssaEvans-p3HW.py
#Hwk #: 3 - Areas of Rectangles

length1 = int(input("Enter a length for Rectangle 1: "))
width1 = int(input("Enter a width for Rectangle 1: "))
areaRectangle1 = length1 * width1

length2 = int(input("Enter a length for Rectangle 2: "))
width2 = int(input("Enter a width for Rectangle 2: "))
areaRectangle2 = length2 * width2

if (areaRectangle2 > areaRectangle1):
	print("The area of Rectangle 2 is greater than the area of Rectangle 1.")
elif (areaRectangle1> areaRectangle2):
	print("The area of Rectangle 1 is greater than the area of Rectangle 2.")
else:
	print("The rectangles have the same area.")
