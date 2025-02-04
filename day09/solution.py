def getDiskMap(path):
    with open(path, 'r') as file:
        data = list(file.read())
    return data

def checkSumA(fileString):
    result = 0
    for i in range(len(fileString)):
        if fileString[i] != ".":
            result += i * int(fileString[i])
        else:
            return result

def getFileList(diskMap):
    idNum = 0
    space = False
    fileString = []
    for num in diskMap:
        if not space:
            test1 = []
            for i in range(int(num)):
                test1.append(str(idNum))
            fileString += test1
            idNum += 1
        else:
            fileString += str('.')*int(num)
        space = not space

    return list(fileString)

def shiftFragment(fileList):
    n = 0

    for i in range(len(fileList)-1, 0, -1):
        if n >= i:
            break
        p2 = fileList[i]
        if p2 != ".":
            for j in range(n, i):
                n = j
                p1 = fileList[n]
                if p1 == ".":
                    fileList[n] = p2
                    fileList[i] = '.'
                    n += 1
                    break 
    
    return fileList

def solve1(map):
    return checkSumA(shiftFragment(getFileList(map)))

# print(solve1(getDiskMap("day09/data1.txt")))

def findSpaceEnd(fileList, start: int, end=0):
    if not end:
        end = start
    end += 1

    if fileList[end] == fileList[start]:
        end = findSpaceEnd(fileList, start, end=end)

    return end

def findSpaceStart(fileList, end: int, start=-1):
    if start == -1:
        start = end
    start -= 1

    if (fileList[start] == fileList[end]) and (start >= 0):
        start = findSpaceStart(fileList, end, start=start)

    return start

def checkSumB(fileString):
    result = 0
    for i in range(len(fileString)):
        if fileString[i] != ".":
            result += i * int(fileString[i])
    return result

def shiftFile(fileList):
    n = 0
    m = len(fileList)-1
    while m > 0:
        for p2 in range(m, 0, -1): # for p2 in range(len(fileList)-1, p1, -1):
            j = findSpaceStart(fileList, p2)
            if fileList[p2] == ".":
                m = j
                break
            else:
                swapped = False
                n = 0
                while m > n and not swapped:
                    for p1 in range(n, m):
                        i = findSpaceEnd(fileList, p1)
                        if fileList[p1] != '.':
                            n = i
                            break
                        else:
                            if (p2-j) > (i - p1):
                                n = i
                                break
                            else:
                                for fileNum in reversed(fileList[j+1:p2+1]):
                                    fileList[n] = fileNum
                                    fileList[m] = '.'
                                    n += 1
                                    m -= 1
                                swapped = True
                                break
                m = j
                break


    return fileList

def solve2(map):
    return checkSumB(shiftFile(getFileList(map)))


print(solve2(getDiskMap("day09/data1.txt")))
