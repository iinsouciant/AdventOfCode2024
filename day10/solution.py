class Node:
    def __init__(self, val=None, loc:tuple|None=None):
        self.val = val
        self.loc = loc
    
    def __getitem__(self, attr:str):
        return self.

def getTopographyMap(path):
    with open(path, 'r') as file:
        data = file.read().splitlines()
    
    for i, row in enumerate(data):
        data[i] = list(map(int, row))
    return data



if __name__ == "__main__":
    print(getTrailheadScore(getTopographyMap("day10/data3.txt")))