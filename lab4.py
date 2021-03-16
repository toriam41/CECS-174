# Lab Assignment 4
# 8.21.18

import sys

# variables (40 (10 ticks) 30 (20 ticks) 10 (35 ticks) 15) 1740(23 ticks)17(18 ticks)35(36)39)
position = 40

# Ask user for lock combo
combo1 = int(input("What's the first combination number?: "))
combo2 = int(input("What's the second combination number?: "))
combo3 = int(input("What's the last combination number?: "))

# Ask user for ticks clockwise
numticks = position - combo1
ticks = int(input("How many ticks CLOCKWISE?: "))

while ticks == numticks:
    position = (position - ticks) % 40

    ticks = int(input("How many ticks COUNTERCLOCKWISE?: "))
    position = (position + ticks) % 40

    if position == combo2:
        ticks = int(input("How many ticks CLOCKWISE?: "))
        position = position + (40 - ticks)

        if position == combo3:
                print("Congrats! You win a million dollars!")
        else:
                print("Wrong Combo")
    else:
        print("Wrong combo. Try again.")
        break
