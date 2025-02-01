import re

def getMap(path):
    with open(path, 'r') as file:
        data = file.read().splitlines()
    return [list(c) for c in data]

def getNodeLocations(map):
    freqRegex = r"(?i)[\da-z]"
    nodeLocations = {}
    # could probably rework this to match each line and use the start and end methods for locations 
    for i in range(len(map)):
        for j in range(len(map[i])):
            test = re.match(freqRegex, map[i][j])
            if  test is not None:
                testMatch = test.group()
                if testMatch in nodeLocations:
                    nodeLocations[testMatch].append((i, j))
                else:
                    nodeLocations[testMatch] = [(i, j)]

    return nodeLocations

def getAntinodeLocationsOld(loc1,loc2):
    distance = [loc2[0]-loc1[0],loc2[1]-loc1[1]] # relative to loc 1
    return [(loc1[0]-distance[0],loc1[1]-distance[1]),(loc2[0]+distance[0],loc2[1]+distance[1])]

def validateLocation(loc, map):
    if (loc[0] < len(map)) and (loc[1] < len(map[0])) and (loc[0] >= 0) and (loc[1] >= 0):
        return True
    else: 
        return False

def compareMaps(map1, map2):
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                map1[i][j] = "!"
                print(f"Mismatch at ({i},{j})")

    print(map1)


def solve1(path):
    count = 0
    map = getMap(path)
    nodes = getNodeLocations(map)
    for freq in nodes:
        for i1 in range(len(nodes[freq])):
            for i2 in range(i1+1, len(nodes[freq]), 1):
                for loc in getAntinodeLocationsOld(nodes[freq][i1], nodes[freq][i2]):
                    if validateLocation(loc, map) and (map[loc[0]][loc[1]] != '#'):
                        count += 1
                        map[loc[0]][loc[1]] = '#'
    
    # compareMaps(map,getMap("day08/data3.txt"))
    return count

def getAntinodeLocations(loc1,loc2, map):
    cont = True
    distance = [loc2[0]-loc1[0],loc2[1]-loc1[1]] # relative to loc 1
    antinodes = [(loc1[0],loc1[1])]
    n = 1
    while cont:
        testLoc = (loc1[0]-(n*distance[0]),loc1[1]-(n*distance[1]))
        if validateLocation(testLoc, map):
            antinodes.append(testLoc)
            n += 1
        else:
            n = 1
            cont = False

    cont = True
    while cont:
        testLoc = (loc1[0]+(n*distance[0]),loc1[1]+(n*distance[1]))
        if validateLocation(testLoc, map):
            antinodes.append(testLoc)
            n += 1
        else:
            n = 1
            cont = False
        
    return antinodes

def solve2(path):
    count = 0
    map = getMap(path)
    nodes = getNodeLocations(map)
    for freq in nodes:
        for i1 in range(len(nodes[freq])):
            for i2 in range(i1+1, len(nodes[freq]), 1):
                for loc in getAntinodeLocations(nodes[freq][i1], nodes[freq][i2], map):
                    if validateLocation(loc, map) and (map[loc[0]][loc[1]] != '#'):
                        count += 1
                        map[loc[0]][loc[1]] = '#'
    
    # compareMaps(map,getMap("day08/data4.txt"))
    return count

print(solve2("day08/data1.txt"))
