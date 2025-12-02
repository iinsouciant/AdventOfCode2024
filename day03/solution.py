# goal of the program is to multiply some ints together
# invalid sequences to be ignored if they have
import re

def getRows(path):
    rows = []
    with open(path, 'r') as file:
        rows = file.read().splitlines()
    return ''.join(rows)

def getMult(row):
    regexFull = r"(mul\(\d{1,3},\d{1,3}\))"
    regexNum = r"\d{1,3}"
    multSum = 0
    for match in re.findall(regexFull, row):
        numIterator = map(int, re.findall(regexNum, match))
        multSum += next(numIterator)*next(numIterator)
    return multSum

def solve1(rows):
    return sum(map(getMult, rows))

    # split each row at the dont match. if there is a dont match, search for a do match and split at that point
    # search in that section for a dont match and if there is a split, repeat the process
def multRecursion(aString):
    regexDont = r"don\'t\(\)"
    regexDo = r"do\(\)"
    testDontSplit = re.split(regexDont, aString, maxsplit=1)
    if len(testDontSplit) == 1:
        return getMult(testDontSplit[0])
    else:
        testDoSplit = re.split(regexDo, testDontSplit[1], maxsplit=1)
        if len(testDoSplit) == 1:
            return getMult(testDontSplit[0])
        else:
            return getMult(testDontSplit[0]) + multRecursion(testDoSplit[1])

def solve2(rows):
    return multRecursion(rows)

# print(solve1(getRows('day03/data1.txt')))
print(solve2(getRows('day03/data1.txt')))