# Homework 2 Assignment

import sys
import math

def menu():
    print("Menu options:\n1. Check a palindrome\n2. Check a word square\n3. Quit")

def menuchoice():
    choice = int(input("Please select an option: "))

    while choice < 0 or choice > 3:
            choice = int(input("Please select an option: "))

    return choice

def getphrase():
    phrase = input("Please enter a phrase: ")

    while len(phrase) < 1:
        phrase = input("Please enter an actual phrase: ")

    return phrase

def ispalindrome(phrase):
    word = phrase.lower()
    i = 0
    j = -1
    palindrome = True

    for x in range(i, len(word)):
        while not(word[i].isalpha()):
            i += 1

        while not(word[j].isalpha()):
            j -= 1

        if word[i] != word[j]:
            palindrome = False
            break

        return palindrome

def checkpalindrome():
    message = getphrase()
    check = ispalindrome(message)

    if check == True:
        print(message, "is a palindrome!")
    else:
        print(message, "is not a palindrome!")

def getwordsquare():
    first = input("Enter first line of square: ")
    order = len(first)
    square = first

    for i in range (1, order):
        line = input("Please enter next line of square: ")
        square += line

    return square

def checkwordsquare(square):
    length = len(square)
    order = int(math.sqrt(length))
    k = 0
    word = ''
    wordsquare = True

    while k < order:
        for i in range(0, order):
            vertical = square[i:length:order]
            i += order

            for a in range(0, order):
                word += square[(k*order) + a]

            if vertical != word:
                wordsquare = False

            k += 1
            word = ''

    return wordsquare

def menusquare():
    potential = getwordsquare()
    wsquare = checkwordsquare(potential)
    length = len(potential)
    order = int(math.sqrt(length))

    for i in range(0, order):
        vertical = potential[i:length:order]
        print(vertical)
        i += order

    if wsquare == True:
        print("is a word square!")
    else:
        print("is not a word square!")



def main():

    run = 1
    while run == 1:
        menu()

        choice = menuchoice()

        if choice == 1:
            checkpalindrome()

        elif choice == 2:
            menusquare()

        else:
            print("Bye")
            run = 2

main()
