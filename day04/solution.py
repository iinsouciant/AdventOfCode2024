import re

xmasPattern = re.compile(r'XMAS')

def getMatrix(path):
    rows = []
    with open(path, 'r') as file:
        rows = file.read().splitlines()
    return rows

def findXLocations(matrix):
    xLocations = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                xLocations.append((i, j))
    return xLocations

def lookUpX(x, matrix):
    if (x[0] > 2) and (matrix[(x[0]-1)][x[1]] == 'M') and (matrix[(x[0]-2)][x[1]] == 'A') and (matrix[(x[0]-3)][x[1]] == 'S'):
        return True
def lookDownX(x, matrix):
    if (x[0] < len(matrix)-3) and (matrix[(x[0]+1)][x[1]] == 'M') and (matrix[(x[0]+2)][x[1]] == 'A') and (matrix[(x[0]+3)][x[1]] == 'S'):
        return True
def lookLeftX(x, matrix):
    if (x[1] > 2) and (matrix[x[0]][(x[1]-1)] == 'M') and (matrix[x[0]][(x[1]-2)] == 'A') and (matrix[x[0]][(x[1]-3)] == 'S'):
        return True
def lookRightX(x, matrix):
    if (x[1] < len(matrix[x[0]])-3) and (matrix[x[0]][(x[1]+1)] == 'M') and (matrix[x[0]][(x[1]+2)] == 'A') and (matrix[x[0]][(x[1]+3)] == 'S'):
        return True
def lookUpLeftX(x, matrix):
    if (x[0] > 2) and (x[1] > 2) and (matrix[(x[0]-1)][(x[1]-1)] == 'M') and (matrix[(x[0]-2)][(x[1]-2)] == 'A') and (matrix[(x[0]-3)][(x[1]-3)] == 'S'):
        return True
def lookUpRightX(x, matrix):
    if (x[0] > 2) and (x[1] < len(matrix[x[0]])-3) and (matrix[(x[0]-1)][(x[1]+1)] == 'M') and (matrix[(x[0]-2)][(x[1]+2)] == 'A') and (matrix[(x[0]-3)][(x[1]+3)] == 'S'):
        return True
def lookDownRightX(x, matrix):
    if (x[0] < len(matrix)-3) and (x[1] < len(matrix[x[0]])-3) and (matrix[(x[0]+1)][(x[1]+1)] == 'M') and (matrix[(x[0]+2)][(x[1]+2)] == 'A') and (matrix[(x[0]+3)][(x[1]+3)] == 'S'):
        return True
def lookDownLeftX(x, matrix):
    if (x[0] < len(matrix)-3) and (x[1] > 2) and (matrix[(x[0]+1)][(x[1]-1)] == 'M') and (matrix[(x[0]+2)][(x[1]-2)] == 'A') and (matrix[(x[0]+3)][(x[1]-3)] == 'S'):
        return True
    
def xmasCount(x, matrix):
    count = 0
    if lookUpX(x, matrix):
        count += 1
    if lookDownX(x, matrix):
        count += 1
    if lookLeftX(x, matrix):
        count += 1
    if lookRightX(x, matrix):
        count += 1
    if lookUpLeftX(x, matrix):
        count += 1
    if lookUpRightX(x, matrix):
        count += 1
    if lookDownRightX(x, matrix):
        count += 1
    if lookDownLeftX(x, matrix):
        count += 1
    return count

def solve1(matrix):
    count = 0
    for x in findXLocations(matrix):
        count += xmasCount(x, matrix)

    return count

def findALocations(matrix):
    aLocations = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                aLocations.append((i, j))
    return aLocations

def lookDiagonalsA(a, matrix):
    count = 0
    if (a[0] > 0) and (a[1] > 0) and (a[0] < len(matrix)-1) and (a[1] < len(matrix[(a[0]+1)])-1):
        if (matrix[(a[0]-1)][(a[1]-1)] == 'M') and (matrix[(a[0]+1)][(a[1]+1)] == 'S'):
            count += 1
        if (matrix[(a[0]-1)][(a[1]-1)] == 'S') and (matrix[(a[0]+1)][(a[1]+1)] == 'M'):
            count += 1
        if (matrix[(a[0]-1)][(a[1]+1)] == 'M') and (matrix[(a[0]+1)][(a[1]-1)] == 'S'):
            count += 1
        if (matrix[(a[0]-1)][(a[1]+1)] == 'S') and (matrix[(a[0]+1)][(a[1]-1)] == 'M'):
            count += 1
    
    if count >= 2:
        return True
    else:
        return False

def solve2(matrix):
    count = 0
    for a in findALocations(matrix):
        if lookDiagonalsA(a, matrix):
            count += 1
    return count

print(solve2(getMatrix('day04/data3.txt')))