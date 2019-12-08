from pathlib import Path
from util import Util
import os
script_location = Path(__file__).absolute().parent
input_location = script_location / 'input.txt'

w = 25
h = 6

def processLayer():
    data = Util.getStringFromFile(input_location)
    # data = '0222112222120000'
    # w = 2
    # h = 2
    layers = getLayers(data, w, h)
    result = mergeLayers(layers)
    image = os.linesep
    for j in range(h):
        image += result[j*w:(j+1)*w] + os.linesep

    return image

def mergeLayers(layers):
    result = ''
    c = '2'
    for i in range(len(layers[0])):
        for layer in layers:
            d = layer[i]
            if d == '0' or d == '1':
                c = d
                break

        result += c
    return result


def mergeLayers2(layers):
    resultLayer = layers[0]
    for layer in layers:
        i = 0
        for c in layer:
            if c == '0' or c == '1':
                resultLayer[i] = c
            i += 1
    return resultLayer        
    

def getLayers(data, w, h):
    i = 0
    layer = ''
    layers = []
    for c in data:
        i += 1
        layer += c
        if i % (w * h) == 0:
            layers.append(layer)
            layer = ''
    return layers


def readInput():
    data = Util.getStringFromFile(input_location)
    i = 0
    layer = ''
    layers = 0
    result = None
    minZeros = Util.maxInt()
    for c in data:
        i += 1
        layer += c
        if i % (w * h) == 0:
            zeros = countDigit(layer, '0')
            ones = countDigit(layer, '1')
            twos = countDigit(layer, '2')
            
            if zeros < minZeros:
                minZeros = zeros
                result = ones * twos

            layers += 1
            layer = ''

    return result

def countDigit(layer, digit):
    s = 0
    for c in layer:
        if c == digit:
            s += 1
    return s