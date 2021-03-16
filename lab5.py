# Lab Assignment 5
# 9.28.18

import sys
import random

secret = random.randrange(1, 11)
guess = int(input("Please guess a number between 1 and 10 inclusive: "))
tries = 0

while guess != secret:
    tries += 1
    guess = int(input("Please try again: "))

if tries <= 5:
    print("Congratulations! You've guessed the right number.")
elif 5 < tries <= 10:
    print("You're unlucky but you got it.")
else:
    print("Think harder next time.")
