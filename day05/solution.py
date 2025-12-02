import re

def getUpdates(path):
    with open(path, 'r') as file:
        data = file.read()
    return data.split('\n\n')

def getRulesDict(instructions):
    rules = {}
    for instruction in instructions.split('\n'):
        rule = instruction.split('|')
        if rule[0] in rules:
            rules[rule[0]].append(rule[1])
        else:
            rules[rule[0]] = [rule[1]]
    return rules

def getPagesList(pages):
    return [x.split(",") for x in pages.split("\n")]

# need to figure out if a page number is after ones it should be before
# do i just go back for each page number in the dict when it is discovered to see if it is okay?

def checkBeforeValidOld(beforePage, afterPages, visited):
    if beforePage not in visited:
        return False
    for page in afterPages:
        if page in visited:
            return False
    return True

def solve1(data):
    count = 0
    [instructions, pages] = data
    rules = getRulesDict(instructions)
    for manual in getPagesList(pages):
        visited = []
        valid = True
        for page in manual:
            visited.append(page)
            if page in rules:
                if not checkBeforeValidOld(page, rules[page], visited):
                    valid = False
                    break
        if valid:
            count += int(manual[(int(len(manual)/2))])
    return count

def rearrangePages(manual, rules):
    newManual = manual.copy()
    for i in range(len(manual)-1, 0, -1):
        swapped = False
        for n in range(i):
            # beforePage = manual[n]
            # afterPages = rules[manual[n]]
            if newManual[n+1] in rules:
                if newManual[n] in rules[newManual[n+1]]:
                    newManual[n], newManual[n+1] = newManual[n+1], newManual[n]
                    swapped = True

        if not swapped:
            break

    return newManual

def checkBeforeValid(manual, rules):
    for n in range(len(manual)-1):
        if manual[n+1] in rules:
            if manual[n] in rules[manual[n+1]]:
                return False
            
    return True

def solve2(data):
    count = 0
    [instructions, pages] = data
    rules = getRulesDict(instructions)
    for manual in getPagesList(pages):
        if not checkBeforeValid(manual, rules):
            # print(f"{manual} -> {rearrangePages(manual, rules)}")
            manual = rearrangePages(manual, rules)
            count += int(manual[(int(len(manual)/2))])
    return count
        
# print(getRulesDict(getUpdates('day05/data1.txt')[0]))
# print(solve1(getUpdates('day05/data2.txt')))
print(solve2(getUpdates('day05/data2.txt')))