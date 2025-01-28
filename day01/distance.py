import csv

def getLists():
    list1 = []
    list2 = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list1.append(int(row[0]))
            list2.append(int(row[1]))
    return list1, list2

def listCompareAmount(list1, list2):
    distance = 0
    slist1 = sorted(list1)
    slist2 = sorted(list2)
    for i in range(len(slist1)):
        distance += abs(slist1[i] - slist2[i])
    return distance

def similarityScore(list1, list2):
    countDict = dict((el, 0) for el in list1)
    for i in range(len(list2)):
        if list2[i] in countDict:
            countDict[list2[i]] += 1
    score = 0
    for key in countDict.keys():
        score += int(countDict[key])*int(key)

    return score


[data1, data2] = getLists()

print(similarityScore(data1, data2))