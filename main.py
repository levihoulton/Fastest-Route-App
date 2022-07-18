import numpy as np
import math

coordsList = []
distanceList = 0
currInput = "running"

while currInput != "exit":
    coordX = input('Enter x value or e when done \n')
    coordY = input('Enter Y value or e when done \n')
    if coordX == "e" or coordY == "e":
        currInput = "exit"

    if coordX != "e" and coordY != "e":
        coordsList.append((int(coordX), int(coordY)))


def getDistance(coord1, coord2):
    return math.dist(coord1, coord2)


DistList = []
totalDist = 0
i = 0

while i < len(coordsList) - 1:
    totalDist += getDistance(coordsList[i], coordsList[i + 1])
    flo = getDistance(coordsList[i], coordsList[i + 1])
    DistList.append(flo)
    i += 1
print(coordsList, DistList, totalDist)

matrix = np.zeros((len(coordsList),len(coordsList)))

iIndex = 0
for i in coordsList:
    jIndex = 0
    for j in coordsList:
        matrix[iIndex][jIndex] = float(getDistance(i, j))
        jIndex += 1
    iIndex += 1

print(matrix)
#
# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
