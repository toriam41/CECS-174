# Tori McDonald
# Homework Assignment 1
# 10.5.18

import sys

run = True

while run:
    print("Here are the available calucations:")
    print("1. Cost of Fuel\n2. Used Value\n3. Stopping Distance\n4. Quit")

    selection = int(input("Select the number of the operation you'd like: "))

    if selection == 1:
        ecar = float(input("Enter the electric car's kW-h/mi: "))
        while ecar <= 0:
            ecar = float(input("Enter the electric car's kW-h/mi: "))
        cost1 = float(input("Enter cost per kW-h: "))
        while cost1 <= 0:
            cost1 = float(input("Enter cost per kW-h: "))
        gcar = float(input("Enter car's MPG: "))
        while gcar <= 0:
            gcar = float(input("Enter car's MPG: "))
        cost2 = float(input("Enter gas cost per gallon: "))
        while cost2 <= 0:
            cost2 = float(input("Enter gas cost per gallon: "))
        distance = float(input("How many miles do you travel per month on average?: "))
        while distance <= 0:
            distance = float(input("How many miles do you travel per month on average?: "))

        yearcost1 = ((distance * 12) / ecar) * cost1
        yearcost2 = ((distance * 12) / gcar) * cost2

        if yearcost1 < yearcost2:
            saved = yearcost2 - yearcost1
            print("The electric car is cheaper by $", "{:.2f}".format(saved))
        elif yearcost2 < yearcost1:
            saved = yearcost1 - yearcost2
            print("The gas car is cheaper by $", "{:.2f}".format(saved))
        else:
            print("Both cars cost the same per year.")

    elif selection == 2:
        price = float(input("What is the original price of the car?: "))
        while price <= 0:
            price = float(input("What is the original price of the car?: "))
        years = int(input("How many years are you tracking the car?: "))
        while years <= 0:
            years = int(input("How many years are you tracking the car?: "))
        for i in range(1, years + 1):
            worth = price - (price * .18)
            print("Year", i, "value is", "{:.2f}".format(worth), "dollars")
            price = worth

    elif selection == 3:
        vi = float(input("Enter car's initial speed in mph: "))
        while vi <= 0:
            vi = float(input("Enter car's initial speed: "))
        tires = int(input("What was the condition of the tires? (1 = new tires, 2 = good tires, 3 = poor tires): "))
        while tires <= 0 or tires > 3:
            tires = int(input("What was the condition of the tires? (1 = new tires, 2 = good tires, 3 = poor tires): "))
        # mu constants
        new = .8
        good = .6
        poor = .5

        # velocity is in miles/hour and g is in feet/seconds^2
        sconvert = 1 / 60**2
        fconvert = 5280
        velocity = vi * sconvert * fconvert

        if tires == 1:
            distance = velocity**2 / (2 * new * 32.174)
            condition = "new"
        elif tires == 2:
            distance = velocity**2 / (2 * good * 32.174)
            condition = "good"
        else:
            distance = velocity**2 / (2 * poor * 32.174)
            condition = "poor"
        print("At", vi, "mph with", condition, "tires, the car will travel", "{:.2f}".format(distance), "feet before stopping.")

    elif selection == 4:
        run = False
