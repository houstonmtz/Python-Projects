# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Houston Martinez
# Section:      526
# Assignment:   Lab 4b - 3
# Date:         19 September 2019
#

print("This program will report the total number of widgets produced based on the user's imputed days.")
print()

days = int(input("Please enter the number of days: "))
if days <= 10:
    totalwidgets = days*10
    print("If it is day", days, ", then the total number of widgets produced would be", totalwidgets)
elif days <= 60 and days >= 11:
    totalwidgets = 100+((days-10)*40)
    print("If it is day", days, ", then the total number of widgets produced would be", totalwidgets)
elif days >= 61 and days <= 100:
    totalwidgets = (2100+780)-(99-days)*(100-days)/2
    print("If it is day", days, ", then the total number of widgets produced would be", totalwidgets)
