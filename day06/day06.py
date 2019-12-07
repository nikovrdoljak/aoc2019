from pathlib import Path
from util import Util
import copy
script_location = Path(__file__).absolute().parent
input_location = script_location / 'input.txt'

    
def getDistance():
    list = Util.getListFromFile(input_location)
    d = findDistance('YOU', 'SAN', list, 0)
    # print('END:', d)

def findDistance(find, end, list, distance):

    for item in list:
        part1 = item.split(')')[0]
        part2 = item.split(')')[1]
        if find == end:
            print('Distance:', distance - 2)

        
        if part1 == find:
            newList = copy.deepcopy(list)
            newList.remove(item)
            findDistance(part2, end, newList, distance + 1)
        if part2 == find:
            newList = copy.deepcopy(list)
            newList.remove(item)
            findDistance(part1, end, newList, distance + 1)
            # list.remove(item)

    return distance + 1

def getTotalOrbits():
    list = Util.getListFromFile(input_location)

    clist = []    
    cnt = calcOrbits('COM', 0, list, clist)
    
    return sum(clist)

def calcOrbits(name, cnt, list, clist):
    if len(list) == 0:
        return cnt

    for item in list:
        if item.split(')')[0] == name:
            cnt += 1
            # list.remove(item)
            newName = item.split(')')[1]
            # clist.append(cnt)
            cnt = calcOrbits(newName, cnt, list, clist)
    
    clist.append(cnt)
    # print (name, cnt)
    return cnt - 1
