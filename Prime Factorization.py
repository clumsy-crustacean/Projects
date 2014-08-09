import math


def PF(current):
    PFList = [1]
    treeIncomplete = True
    while treeIncomplete:
        for x in range(int(current)):
            if (x+1) < current:
                if (x+1) > 1:
                   temp = current / (x+1)
                   check = math.floor(temp)
                   if check < temp:
                       continue
                   else:
                       PFList.append(x+1)
                       current = temp
                       break
                else:
                    continue
            else:
                PFList.append(int(current))
                treeIncomplete = False
                break
    return PFList


def main():
    badInput = True
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
        if userInput < 1:
            print("Error: Number must be greater than zero")
            continue
        else:
            badInput = False

    primeFactors = PF(userInput)
    for i in range(len(primeFactors)):
        print(primeFactors[i])

main()