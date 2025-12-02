from pathlib import Path

def getLists():
    data = []
    # dataPath = 
    with open('day02/data.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.strip().split(" ")])

    return data

    count = 0
    for row in matrix:
        safe = True
        inc = True
        for i in range(len(row)):
            if (i==0):
                if (row[i] == row[i+1]):
                    safe = False
                    break
                elif (row[i] < row[i+1]):
                    inc = True
                else: 
                    inc = False
                continue

            if (inc == True):
                if (row[i] - row[i-1] == 1) or (row[i] - row[i-1] == 2) or (row[i] - row[i-1] == 3):
                    continue
                else:
                    print(f"unsafe val change row: {row}, {row[i]}-{row[i-1]}")
                    safe = False
                    break

            if (inc == False):
                if (row[i] - row[i-1] == -1) or (row[i] - row[i-1] == -2) or (row[i] - row[i-1] == -3):
                    continue
                else:
                    print(f"unsafe val change in row: {row}, {row[i]}-{row[i-1]}")
                    safe = False
                    break
        if (safe == True):
            count += 1
    return count

def checkLevelChange(row, inc):
    for i in range(len(row)):
        if (i == 0):
            continue
        if (inc == True):
            if (row[i] - row[i-1] == 1) or (row[i] - row[i-1] == 2) or (row[i] - row[i-1] == 3):
                continue
            else:
                return False, i
        if (inc == False):
            if (row[i] - row[i-1] == -1) or (row[i] - row[i-1] == -2) or (row[i] - row[i-1] == -3):
                continue
            else:
                return False, i
    return True, i

def removalTest(row, i, inc):
    row2 = row.copy()
    del row2[i]
    return checkLevelChange(row2, inc)
    
def safeCounterDampener(matrix):
    count = 0
    for row in matrix:
        inc = True
        removalShield = True

        if (row[0] == row[1]):
            if removalTest(row, 0, True):
                removalShield = False
                print(f"init row: {row}\n removing {0}")
                del row[0]
                print(f"new row: {row}")
            elif removalTest(row, 0, False):
                removalShield = False
                print(f"init row: {row}\n removing {0}")
                del row[0]
                print(f"new row: {row}")
                inc = False
            else:
                safe = False
                print("skipping to next row")
                continue
        elif (row[0] < row[1]):
            inc = True
        else: 
            inc = False
        
        [safeCheck,invalidI] = checkLevelChange(row, inc)
        if (safeCheck):
            count += 1
            continue
        elif (safeCheck == False) and (removalShield == True):
            print(f"unsafe increase in row: {row}, {row[invalidI]}-{row[invalidI-1]}\nshield:{removalShield}")
            [safeCheck2,invalidI2] = removalTest(row, invalidI, inc)
            removalShield = False
            if (safeCheck2):
                count += 1
                continue
            elif (invalidI2 == len(row)-1):
                del row[invalidI]
                print(f"new row: {row}")
                count += 1
                continue
            else:
                print("skipping to next row")
                continue
        else:
            print("skipping to next row")
            continue

    return count

print(safeCounterDampener(getLists()))