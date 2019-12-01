# If we run code from IDE (like VSCode) then we need absoulte path to input file.
# From console relative path is enough
from pathlib import Path
import sys
from util import Util
script_location = Path(__file__).absolute().parent
input_location = script_location / 'input01.txt'

def getFuelRequirementsSum():
    list = Util.getListFromFile(input_location)
    result = 0
    for line in list:
        result += getFuelRequired(int(line))
    return result

def getFuelRequired(n):
    return n // 3 - 2

def getFuelFuel(n):
    fuel = 0
    fuelRequired = getFuelRequired(n)
    while fuelRequired >= 0:
        fuel += fuelRequired
        fuelRequired = getFuelRequired(fuelRequired)
    return fuel    
    
def getFuelFuelRequirementsSum():
    list = Util.getListFromFile(input_location)
    result = 0
    for line in list:
        fuelRequired = getFuelFuel(int(line))
        result += fuelRequired
    return result