import sys

notes = [("C", 60), ("D", 62), ("E", 64), ("F", 65), ("G", 67), ("A", 69), ("B", 71)]

def notetoint(note):
    # 7 if statements max, sharp/flat changes number by 1, ^ increases 12
    # loop through notes until finding matching letter value

    check = 0
    length = len(note)
    for i in range(0, length )):
        while not(note[i].isalpha):
            i += 1
            check += 1
        if note[i] == 'C':
            number = notes[0][1]
        if note[i] == 'D':
            number = notes[1][1]
        if note[i] == 'E':
            number = notes[2][1]
        if note[i] == 'F':
            number = notes[3][1]
        if note[i] == 'G':
            number = notes[4][1]
        if note[i] == 'A':
            number = notes[5][1]
        if note[i] == 'B':
            number = notes[6][1]
