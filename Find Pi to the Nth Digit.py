# This program is designed to accept input from the user in the form of a number between 1 and 19,
# after which the program calculates pi to that (the user's input) number of decimal points.  This
# program only accepts numbers; I'm not sure how to check if it's not a number

import decimal
import math
import sys

# Initialize variables
userInput = 0
badInput = True
# while user's input is not proper format
while badInput:
    userInput = float(input("Please enter number here: "))

    # The following checks to see whether the number inputted is a whole number
    check = math.floor(userInput)
    # if the inputted number, after truncating everything after the decimal, is less than
    # the original inputted number, then ask for new input
    if check < userInput:
        print("Error: Not an integer")
        continue

    # Is the number positive?
    if userInput < 0:
        print("Error: Number must be positive")
        continue
    # if isinstance(userInput, int):
    #     pass
    # else:
    #     print("Error: Not an integer")
    #     continue

    # try:
    #     value = int(userInput)
    # except ValueError:
    #     print("Error: Not an integer")
    #     continue
    # else:
    #     pass
    # Is the number less than 20?
    if userInput < 20:
        badInput = False
    else:
        print("Error: number is not less than 20")
# while user's input is not proper format

# Calculation of pi to requested decimal point
a = decimal.Decimal(math.pi)        # Converts pi to proper type for round function
b = int(userInput)                  # Converts userInput to int
c = round(a, b)
print(c)


print("Thank you! Please press enter to end program")
input()
sys.exit()
# End program
