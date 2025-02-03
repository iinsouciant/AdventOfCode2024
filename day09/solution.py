def getDiskMap(path):
    with open(path, 'r') as file:
        data = list(file.read())
    return data

def checkSum(fileString):
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

def shiftFile(fileList):
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
    return checkSum(shiftFile(getFileList(map)))


print(solve1(getDiskMap("day09/data1.txt")))