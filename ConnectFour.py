import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], [
    "", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]

rows = 6
cols = 7


def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if (gameBoard[x][y] == "🔵"):
                print("", gameBoard[x][y], end=" |")
            elif (gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")


def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn


def checkForWinner(chip):
    # horizontal
    for y in range(rows):
        for x in range(cols - 3):
            if gameBoard[y][x] == chip and gameBoard[y][x+1] == chip and gameBoard[y][x+2] == chip and gameBoard[y][x+3] == chip:
                print("\nGame over!", chip, "wins! Thank you for playing")
                return True

# vertical
    for x in range(cols):
        for y in range(rows - 3):
            if gameBoard[y][x] == chip and gameBoard[y+1][x] == chip and gameBoard[y+2][x] == chip and gameBoard[y+3][x] == chip:
                print("\nGame over!", chip, "wins! Thank you for playing")
                return True

    # Check  right to bottom left diagonal spaces
    for x in range(rows - 3):
        for y in range(3, cols):
            if gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check  left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False


def coordinateParser(inputString):
    coordinate = [None] * 2
    if (inputString[0] == "A"):
        coordinate[1] = 0
    elif (inputString[0] == "B"):
        coordinate[1] = 1
    elif (inputString[0] == "C"):
        coordinate[1] = 2
    elif (inputString[0] == "D"):
        coordinate[1] = 3
    elif (inputString[0] == "E"):
        coordinate[1] = 4
    elif (inputString[0] == "F"):
        coordinate[1] = 5
    elif (inputString[0] == "G"):
        coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate


def isSpaceAvailable(intendedCoordinate):
    if (gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
        return False
    elif (gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
        return False
    else:
        return True


def gravityChecker(intendedCoordinate):
    # Calculate space below
    spaceBelow = [None] * 2
    spaceBelow[0] = intendedCoordinate[0] + 1
    spaceBelow[1] = intendedCoordinate[1]
    # Is the coordinate at ground level
    if (spaceBelow[0] == 6):
        return True
    # Check if there's a token below
    if (isSpaceAvailable(spaceBelow) == False):
        return True
    return False


leaveLoop = False
turnCounter = 0
while (leaveLoop == False):
    if (turnCounter % 2 == 0):
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space: ")
            coordinate = coordinateParser(spacePicked)
            try:
                # Check if the space is available
                if (isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, '🔵')
                    break
                else:
                    print("Not a valid coordinate")
            except:
                print("Error occured. Please try again.")
        winner = checkForWinner('🔵')
        turnCounter += 1
    # computer controls
    else:
        while True:
            cpuChoice = [random.choice(possibleLetters), random.randint(0, 5)]
            cpuCoordinate = coordinateParser(cpuChoice)
            if (isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
                modifyArray(cpuCoordinate, '🔴')
                break
        turnCounter += 1
        winner = checkForWinner('🔴')

    if (winner):
        printGameBoard()
        break
