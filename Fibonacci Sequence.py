import math


def F(n):
    return ((1+math.sqrt(5))**n - (1-math.sqrt(5))**n)/(2**n*math.sqrt(5))


def fibseq(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return F(x-1)+F(x-2)

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

    # Is the number less than 20?
    if userInput < 20:
        badInput = False
    else:
        print("Error: number is not less than 20")
# while user's input is not proper format

for i in range(int(userInput)):
    number = fibseq(i)
    print(number, " ")