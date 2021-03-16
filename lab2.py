# Lab 2 Assignment
# 9.7.18

import sys

# Get players' names and statistics
player = input("Enter player's full name: ")
appearances = int(input("How many plate appearances?: "))
bats = int(input("How many times at bat?: "))
walk = int(input("How many walks?: "))
singles = int(input("How many singles?: "))
doubles = int(input("How many doubles?: "))
triples = int(input("How many triples: "))
runs = int(input("How many home runs?: "))

# Calculate batting average
hits = singles + doubles + triples + runs
print("Total hits: ", hits)

battingavg = (hits / bats)
print("Batting Average: ", "{0:.3f}".format(battingavg))

# Calculate slugging percentage
slugavg = float((singles + (2 * doubles) + (3 * triples) + (4 * runs)) / bats)
print("Slugging Average: ", "{0:.3f}".format(slugavg))

# Calculate OPS
ops = ((hits + walk) / appearances) + slugavg
print("OPS: ", "{0:.3f}".format(ops))
