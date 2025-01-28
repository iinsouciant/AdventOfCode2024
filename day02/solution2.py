def getLists():
    data = []
    # dataPath = 
    with open('day02/data.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.strip().split(" ")])

    return data

# all the differences between the elements need to be the same sign
# all the differences between the elements need to be abs(1 -> 3)

def isSafe(row):
    diffsList = []
    for i in range(len(row)-1):
        diffsList.append(row[i+1]-row[i])

    # print(diffsList)

    for i in range(len(diffsList)): # are all of them the same sign?
        if not ((diffsList[i]*diffsList[0] > 0) and (abs(diffsList[i])>=1) and (abs(diffsList[i])<=3)):
            return False
    return True

def solve1(reports):
    return sum(map(isSafe, reports))

def isSafeReportVariation(report):
    if isSafe(report):
        return True
    else:
        for i in range(len(report)):
            if isSafe(report[:i]+ report[i+1:]):
                return True
            
        return False
    
def solve2(reports):
    return sum(map(isSafeReportVariation, reports))
            

print(solve1(getLists()))
print(solve2(getLists()))