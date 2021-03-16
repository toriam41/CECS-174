# Lab Assignment 3
# 9.14.18

import sys
import math

# distance (float; m)
# gunpowder (float > 0; kg )
# theta (float; degrees < 90)


gravity = 9.8

# ask user for input on target distance + angle + gunpowder
target = float(input("How far away is the object?: "))
gunpowder = float(input("How much gunpowder?: "))
angle = float(input("At what angle do we shoot the cannon?: "))

# convert degrees to radians
theta = (angle / 180) * math.pi


# calculate horizontal + vertical aspects of velocity
ivelocity = gunpowder * (10)
xvelocity = ivelocity * math.cos(theta)
yvelocity = ivelocity * math.sin(theta)

# calculate total time and distance ball travels
time = 2 * (yvelocity / gravity)
distance = time * xvelocity

# compare distances
if (target - 1) <= distance <= (target + 1):
    print("You hit the target!")
elif distance < target - 1:
    miss = target - distance
    print("Your shot landed short of the target by", "{0:.2f}".format(miss), "meters.")
else:
    miss = distance - target
    print("Your shot past the target by", "{0:.2f}".format(miss), "meters.")
