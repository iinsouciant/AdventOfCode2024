import re
import copy

exit = False

def getMap(path):
    with open(path, 'r') as file:
        data = file.read().splitlines()

    return [list(x) for x in data]

def getPos(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if re.match(r"[\^v<>]",map[i][j]):
                return [[i, j], map[i][j]]

def moveUp(currentPos, map):
    global exit 
    obstacleAhead = False
    i = 0
    while (not obstacleAhead) and (not exit) and (i < 1000):
        map[currentPos[0]][currentPos[1]] = 'X'
        currentPos[0] -= 1
        if currentPos[0] < 0:
            exit = True
            return currentPos, '^'
        else:
            if (map[currentPos[0]][currentPos[1]] == '#') or (map[currentPos[0]][currentPos[1]] == 'O'):
                obstacleAhead = True
                currentPos[0] += 1
                map[currentPos[0]][currentPos[1]] = '>'
                return currentPos, map[currentPos[0]][currentPos[1]]

            map[currentPos[0]][currentPos[1]] = '^'
        i += 1
    return currentPos, map[currentPos[0]][currentPos[1]]

def moveRight(currentPos, map):
    global exit
    obstacleAhead = False
    i = 0
    while (not obstacleAhead) and (not exit) and (i < 1000):
        map[currentPos[0]][currentPos[1]] = 'X'
        currentPos[1] += 1
        if currentPos[1] >= len(map[currentPos[0]]):
            exit = True
            return currentPos, '>'
        else:
            if (map[currentPos[0]][currentPos[1]] == '#') or (map[currentPos[0]][currentPos[1]] == 'O'):
                obstacleAhead = True
                currentPos[1] -= 1
                map[currentPos[0]][currentPos[1]] = 'v'
                return currentPos, map[currentPos[0]][currentPos[1]]

            map[currentPos[0]][currentPos[1]] = 'v'
        i += 1
    return currentPos, map[currentPos[0]][currentPos[1]]

def moveDown(currentPos, map):
    global exit 
    obstacleAhead = False
    i = 0
    while (not obstacleAhead) and (not exit) and (i < 1000):
        map[currentPos[0]][currentPos[1]] = 'X'
        currentPos[0] += 1
        if currentPos[0] >= len(map):
            exit = True
            return currentPos, 'v'
        else:
            if (map[currentPos[0]][currentPos[1]] == '#') or (map[currentPos[0]][currentPos[1]] == 'O'):
                obstacleAhead = True
                currentPos[0] -= 1
                map[currentPos[0]][currentPos[1]] = '<'
                return currentPos, map[currentPos[0]][currentPos[1]]

            map[currentPos[0]][currentPos[1]] = 'v'
        i += 1
    return currentPos, map[currentPos[0]][currentPos[1]]

def moveLeft(currentPos, map):
    global exit
    obstacleAhead = False
    i = 0
    while (not obstacleAhead) and (not exit) and (i < 1000):
        map[currentPos[0]][currentPos[1]] = 'X'
        currentPos[1] -= 1
        if currentPos[1] < 0:
            exit = True
            return currentPos, '<'
        else:
            if (map[currentPos[0]][currentPos[1]] == '#') or (map[currentPos[0]][currentPos[1]] == 'O'):
                obstacleAhead = True
                currentPos[1] += 1
                map[currentPos[0]][currentPos[1]] = '^'
                return currentPos, map[currentPos[0]][currentPos[1]]

            map[currentPos[0]][currentPos[1]] = '<'
    return currentPos, map[currentPos[0]][currentPos[1]]

def getDistinctPositions(map):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'X':
                count += 1
    return count

def solve1(path):
    global exit
    i = 0
    map = getMap(path)
    currentPos, direction = getPos(map)
    while (not exit) and (i < 1000):
        if direction == '^':
            currentPos, direction = moveUp(currentPos, map)
        elif direction == '>':
            currentPos, direction = moveRight(currentPos, map)
        elif direction == 'v':
            currentPos, direction = moveDown(currentPos, map)
        elif direction == '<':
            currentPos, direction = moveLeft(currentPos, map)
        i += 1

    return getDistinctPositions(map)

# print(solve1('day06/data2.txt'))

def loopTest(map):
    global exit
    i = 0
    currentPos, direction = getPos(map)
    pastLefts = []
    pastRights = []
    pastUps = []
    pastDowns = []
    while (not exit) and (i < 1000):
        if direction == '^':
            currentPos, direction = moveUp(currentPos, map)
        elif direction == '>':
            currentPos, direction = moveRight(currentPos, map)
        elif direction == 'v':
            currentPos, direction = moveDown(currentPos, map)
        elif direction == '<':
            currentPos, direction = moveLeft(currentPos, map)

        if direction == '^':
            if currentPos in pastUps:
                return True
            else:
                pastUps.append(copy.deepcopy(currentPos))
        elif direction == '>':
            if currentPos in pastRights:
                return True
            else:
                pastRights.append(copy.deepcopy(currentPos))
        elif direction == 'v':
            if currentPos in pastDowns:
                return True
            else:
                pastDowns.append(copy.deepcopy(currentPos))
        elif direction == '<':
            if currentPos in pastLefts:
                return True
            else:
                pastLefts.append(copy.deepcopy(currentPos))
        i += 1

    return False

def solve2(path):
    global exit
    loopCount = 0
    i = 0
    map = getMap(path)
    testMap = [[]]
    for i in range(len(map)):
        for j in range(len(map[i])):
            testMap = copy.deepcopy(map)
            exit = False
            if (map[i][j] != '#') and (map[i][j] != '^'):
                testMap[i][j] = 'O'
                if loopTest(testMap):
                    loopCount += 1

    return loopCount

print(solve2('day06/data2.txt'))
