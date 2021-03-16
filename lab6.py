# Lab Assignment 6
#10.6.18

import sys

def getmagnitude(number):
    if number == 1:
        magnitude = float(input("Please enter the magnitude for earthquake 1: "))
        while magnitude <= 0:
            magnitude = float(input("Please enter the magnitude for earthquake 1: "))
    else:
        magnitude = float(input("Please enter the magnitude for earthquake 2: "))
        while magnitude <= 0:
            magnitude = float(input("Please enter the magnitude for earthquake 1: "))
    return magnitude

def comparemagnitude(magnitude1, magnitude2):
    f = 10**(1.5 * (magnitude1 - magnitude2))
    return f

def runagain():
    choice = int(input("Enter 1 to compare two more earthquakes: "))
    if choice == 1:
         return True
    else:
        return False

def main():
    test = True
    while test:
        mag1 = getmagnitude(1)
        mag2 = getmagnitude(2)

        if mag2 > mag1:
            magnitude1 = mag2
            magnitude2 = mag1
            print("Earthquake 2 was", magnitude1, "which is", "{0:.1f}".format(comparemagnitude(magnitude1, magnitude2)), "times stronger than earthquake 1 at", magnitude2)
        else:
            magnitude1 = mag1
            magnitude2 = mag2
            print("Earthquake 1 was", magnitude1, "which is", "{0:.1f}".format(comparemagnitude(magnitude1, magnitude2)), "times stronger than earthquake 2 at", magnitude2)

        test = runagain()

main()
