from itertools import product

def getEquations(path):
    with open(path, 'r') as file:
        data = file.read().splitlines()

    return [eq.split(": ") for eq in data]


def tryOperators(result, nums):
    eqSplit = nums.split(' ')
    for chars in product(['+',"*","||"],repeat=len(eqSplit)-1): 
        # first chars = ('+') when getOperatorCombos('+*',2-1)
        # first loop, go through each num in eqsplit, and use each char in first string in chars
        # then loop to go through each num in eqsplit, use each char in next string in combo
        # repeat for every string in combo
        testResult = int(eqSplit[0])
        for i, oper in enumerate(chars):
            # has to evaluate from left to right so add first one, then proceed depending on next char
            if oper == '+':
                testResult += int(eqSplit[i+1])
            elif oper == '*':
                testResult *= int(eqSplit[i+1])
            elif oper == '-':
                testResult -= int(eqSplit[i+1])
            elif oper == '/':
                testResult /= int(eqSplit[i+1])
            elif oper == '||':
                testResult = int(str(testResult)+eqSplit[i+1])
                
        if testResult == int(result):
            return testResult
    return 0

def solve1(path):
    sum = 0
    equations = getEquations(path)
    for eq in equations:
        sum += tryOperators(eq[0],eq[1])

    return sum

print(solve1("day07/data2.txt"))