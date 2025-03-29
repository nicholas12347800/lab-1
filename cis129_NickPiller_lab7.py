# CIS129 - Dice Game Lab
# Name: Nicholas Piller
# Date: March 28, 2025
# This program simulates a dice game between two players

import random

def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':
        # populate variables
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

        # call to displayInfo
        displayInfo(winnerName)

        endProgram = input('Do you want to end program? (yes/no): ')

# gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter Player One's name: ")
    playerTwo = input("Enter Player Two's name: ")
    return playerOne, playerTwo

# gets the random dice values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    print(playerOne, "rolled:", p1number)
    print(playerTwo, "rolled:", p2number)

    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = "TIE"

    return winnerName

# displays the winner
def displayInfo(winnerName):
    if winnerName == "TIE":
        print("It's a tie!")
    else:
        print("The winner is", winnerName)

# calls main
main()
