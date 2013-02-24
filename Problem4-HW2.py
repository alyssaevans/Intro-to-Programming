# Author: Alyssa Evans
# File: AlyssaEvans-p4.py
# Hwk #: 2

meal_cost = 44.50
tax = .0675 * int(meal_cost)
total_meal_cost = int(meal_cost) + int(tax)
tip = .15 * int(total_meal_cost)
total_bill = int(meal_cost) + int(tax) + int(tip)
print("Meal: ", meal_cost, "\nTax: ", tax, "\nTip: ", tip, "\nTotal: ", total_bill)