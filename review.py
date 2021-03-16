import sys

def tuplesum(tuple):
    sum = 0

    for i in range(0, len(tuple)):
        sum += tuple[i]

    return sum

def main():
    tuples = (12, 8, 13)

    totalval = tuples[0] + tuples[1] + tuples[2]
    total = tuplesum(tuples)

    print(totalval)
    print(total)

main()
