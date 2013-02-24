#Author: Alyssa Evans
#File: AlyssaEvans-p1HW3.py
#Hwk #: 3 - Roman Numeral Converter



x = int(input("Enter a whole number between 1 and 10: "))

s = ""

if (0 < x < 11):
       while ( x != 0):
               if (x == 10):
                       print("X")
                       x = 0
               if (x == 9):
                       print("IX")
                       x = 0
               if (x/5 >= 1):
                       s += ("V")
                       x = x - 5
               if (x/4 >= 1):
                       s += ("IV")
                       x = x - 4
               if (x/1 >= 1):
                       s += ("I")
                       x = x - 1
else:
    print("Error: The number you entered is not within the range.")
    
print (s)

