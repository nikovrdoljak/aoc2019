from pathlib import Path
from util import Util
script_location = Path(__file__).absolute().parent
input_location = script_location / 'input.txt'

def getLine():
    fhand = open(input_location)
    line = fhand.readlines()[0]
    return line

def getList(line):
    list = line.split(',')
    ilist = []
    for s in list:
        ilist.append(int(s))
    return ilist

def handleList(line, noun, verb):
    list = getList(line)
    # if change1and2:
    list[1] = noun
    list[2] = verb
    i = 0
    
    while True:
        x = list[i]
        if x == 1:
            l1 = list[i+1]
            l2 = list[i+2]
            l3 = list[i+3]
            list[l3] = list[l1] + list[l2]
        elif x == 2:
            l1 = list[i+1]
            l2 = list[i+2]
            l3 = list[i+3]
            list[l3] = list[l1] * list[l2]
        elif x == 99:
            break
        i += 4

    return list

def findNoun100Verb(line):
    for n in range(100):
        for v in range(100):
            result = handleList(line, n, v)
            print(n, v, result[0])
            if result[0] == 19690720:
                print(100 * n + v)
                exit()