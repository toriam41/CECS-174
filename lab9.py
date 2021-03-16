import sys
import math


# get country
def getcountry():
    country = input("Please enter a country or quit: ")
    return country

# determine the rank of the country
def getplacings(standings, country):
    found = False

    for i in range(0, len(standings)):
        if standings[i].startswith(country):
            found = True
            rank = i + 1
            break

    if found == False:
        rank = 0

    return rank

def main():
    
    # define order of teams
    placings = ["United States", "Sweden", "Switzerland", "Canada", "Great Britain", "Norway", "South Korea", "Japan", "Italy", "Denmark"]
    loop = True

    while loop:
        nation = getcountry()

        # end program
        if nation == "quit":
            print("bYE")
            loop = False
        else:
            ranking = getplacings(placings, nation)
            medal = ""

            # determine if team is top 3
            if ranking > 0:
                if ranking == 1:
                    medal = "(gold medal)"
                elif ranking == 2:
                    medal = "(silver medal)"
                elif ranking == 3:
                    medal = "(bronze medal)"

                print(placings[ranking - 1], "placed", ranking, medal)
            else:
                    print(nation, "did not compete.")














main()
