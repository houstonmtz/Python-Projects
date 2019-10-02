# Name:         Houston Martinez
# Date:         26 September 2019

print("This program will calculate the sum of all the integers from 0 to the number entered from the user using a for"
      " loop.")
integer = int(input("Please enter the integer to calculate the sum of all integers before it to 0: "))
totalvalue = 0
numbersbelow = 1
integer = integer + 1
for numbersbelow in range(integer):
    totalvalue += numbersbelow

print(totalvalue)
print("-------------------------------------------------------------------------------------------------------")

print("This program will calculate the sum of all the integers from 0 to the number entered from the user using a while"
      " loop.")
integer = int(input("Please enter the integer to calculate the sum of all integers before it to 0: "))

if integer > 0:
    integerbelow = integer - 1
    totalvalue = integer + integerbelow
    while integerbelow >= 0:
        integerbelow = integerbelow - 1
        totalvalue += integerbelow
        if integerbelow <= 0:
            break
else:
    print("Error! First value entered was equal to or below 0.")
print(totalvalue)
print("-------------------------------------------------------------------------------------------------------")

print("This program will calculate the product of all the integers from 1 to the number entered from the user using a "
      "for loop.")
integer = int(input("Please enter the integer to calculate the product of all integers before it to 1: "))
totalvalue = 1
numbersbelow = 1
integer += 1
for numbersbelow in range(1, integer):
    totalvalue *= numbersbelow

print(totalvalue)
print("-------------------------------------------------------------------------------------------------------")

print("This program will calculate the product of all the integers from 1 to the number entered from the user using a"
      " while loop.")
integer = int(input("Please enter the integer to calculate the product of all integers before it to 1: "))
if integer > 1:
    integerbelow = integer - 1
    totalvalue = integer * integerbelow
    while integerbelow >= 1:
        integerbelow = integerbelow - 1
        totalvalue *= integerbelow
        if integerbelow <= 1:
            break

print(totalvalue)
print("-------------------------------------------------------------------------------------------------------")
