# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Houston Martinez
# Section:      526
# Assignment:   Lab 4b - 2
# Date:         19 September 2019
#

print("This program will calculate the Reynold Number based on the user's inputs. It will also tell the user whether"
      " the flow is laminar, in transition, or turbulent.")
print()

V = int(input("Please enter the characteristic velocity of the flow in meters/seconds (m/s):"))
d = int(input("Please enter the pipe diameter in meters (m):"))
v = int(input("Please enter the fluid kinematic viscosity in meters^2/seconds (m^2/s):"))

ReynoldsNum = (V*d)/v

if ReynoldsNum < 2300:
    print("Reynolds Number is", ReynoldsNum, "and the flow is laminar.")
if ReynoldsNum >= 2300 and ReynoldsNum <= 2900:
    print("Reynolds Number is", ReynoldsNum, "and the flow is in transition.")
if ReynoldsNum > 2900:
    print("Reynolds Number is", ReynoldsNum, "and the flow is turbulent.")
