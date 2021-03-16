# Lab Assignment 7
# 10.12.18

import sys

# get highway
def getnumber():
    route = int(input("Enter the highway number: "))
    while route <= 0:
        route = int(input("Enter the highway number: "))
    return route

# determine if it's primary
def isprimary(number):
    if number < 100:
        return True
    else:
        return False

# determine orientation
def compass(number):
    key = number % 10
    if key % 2 == 0:
        return "east-west"
    else:
        return "north-south"

# determine if it's arterial
def isarterial(number):
    if number % 5 == 0:
        return True
    else:
        return False

# determine if it's auxilary
def auxilary(number):
    while (number // 10) != 0:
        number = number // 10
    if number % 2 == 0:
        return "radical"
    else:
        return "spur"

# find parent highway
def parent(number):
    number = number % 100
    return number

def main():
    run = True
    while run:
        highway = getnumber()
        type = isprimary(highway)

        # only if highway is primary
        if type:
            arterial = isarterial(highway)
            if arterial:
                 arterial = "a long-distance arterial highway"
            else:
                arterial = "not a long-distance arterial highway"

            orientation = compass(highway)
            print("Interstate", highway, "is", arterial, "and is oriented", orientation)

        # if highway isn't primary
        else:
            route = auxilary(highway)
            big = parent(highway)
            print("Interstate", highway, "is a", route, "highway whose parent is Interstate", big)

        runagain = int(input("Enter 1 to test another highway: "))
        if runagain != 1:
            run = False
main()
