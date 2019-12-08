seq = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
sequence = '43210'

seq = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
sequence = '01234'

seq = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
sequence = '10432'

diagList = seq.split(',')

def getSignal():
    signal = ''
    for c in sequence:
        output = getOutput(diagList, c)
        signal += output[-1]
    return signal

def getOutput(diagList, inp):
    # inp = '7'
    outp = None
    # diagList = diag.split(',')
    i = 0
    while True:
    # for i in range(len(diagList)):
        param = diagList[i]
        instruction = getParameterModeInstruction(param)
        # print('Param {} - Immediate mode: {}'.format(param, isImmediateMode(param)))
        if param == '99':
            break
        elif instruction[0] == '1':
            position1 = int(diagList[i+1]) if instruction[1] == '0' else i + 1
            position2 = int(diagList[i+2]) if instruction[2] == '0' else i + 2
            position3 = int(diagList[i+3]) if instruction[3] == '0' else i + 3
            diagList[position3] = str(int(diagList[position1]) + int(diagList[position2]))
            i += 4
        elif instruction[0] == '2':
            position1 = int(diagList[i+1]) if instruction[1] == '0' else i + 1
            position2 = int(diagList[i+2]) if instruction[2] == '0' else i + 2
            position3 = int(diagList[i+3]) if instruction[3] == '0' else i + 3
            diagList[position3] = str(int(diagList[position1]) * int(diagList[position2]))
            i += 4
        elif instruction[0] == '3':
            if instruction[1] == '0':
                position = int(diagList[i+1])
                diagList[position] = inp
            elif instruction[1] == '1':
                diagList[i+1] = inp
            i += 2
        elif instruction[0] == '4':
            if instruction[1] == '0':
                position = int(diagList[i+1])
                outp = diagList[position]
            elif instruction[1] == '1':
                outp = diagList[i+1]
            i += 2
            print(outp)
        elif instruction[0] == '5':
            if instruction[1] == '0' and int(diagList[int(diagList[i+1])]) != 0:
                i = int(diagList[int(diagList[i+2])])
            elif instruction[1] == '1' and int(diagList[i+1]) != 0:
                i = int(diagList[i+2])
            else:
                i += 3
        elif instruction[0] == '6':
            if instruction[1] == '0' and int(diagList[int(diagList[i+1])]) == 0:
                i = int(diagList[int(diagList[i+2])])
            elif instruction[1] == '1' and int(diagList[i+1]) == 0:
                i = int(diagList[i+2])
            else:
                i += 3
        elif instruction[0] == '7':
            val1 = diagList[i+1] if instruction[1] == '1' else diagList[int(diagList[i+1])]
            val2 = diagList[i+2] if instruction[1] == '1' else diagList[int(diagList[i+2])]
            val3 = '1' if int(val1) < int(val2) else '0'
            if instruction[3] == '0':
                diagList[int(diagList[i+3])] = val3
            elif instruction[3] == '1':
                diagList[i+3] = val3
            i += 4
        elif instruction[0] == '8':
            val1 = diagList[i+1] if instruction[1] == '1' else diagList[int(diagList[i+1])]
            val2 = diagList[i+2] if instruction[1] == '1' else diagList[int(diagList[i+2])]
            val3 = '1' if val1 == val2 else '0'
            if instruction[3] == '0':
                diagList[int(diagList[i+3])] = val3
            elif instruction[3] == '1':
                diagList[i+3] = val3
            i += 4

        # else:
        #     instruction2 = getParameterModeInstruction(param)
        #     i = processInstruction(instruction2, diagList, i, param)


    return outp

def getParameterModeInstruction(param):
    ret = []
    optcode = param[-1]
    ret.append(optcode)
    if len(param) >= 3:
        ret.append(param[-3])
    else:
        ret.append('0')

    if len(param) >= 4:
        ret.append(param[-4])
    else:
        ret.append('0')

    if len(param) >= 5:
        ret.append(param[-5])
    else:
        ret.append('0')

    # ret.append(optcode)
    # j = -3
    # k = 1
    # while True:
    #     if len(param) >= abs(j):
    #         mode = param[j]
    #         ret.append(mode)
    #         j -= 1
    #         k += 1
    #     else:
    #         break
    return ret

def processInstruction(instruction, diagList, position, param):
    operation = instruction[0]
    # for i in range(1, len(instruction)):
    mode1 = instruction[1]
    value1 = ''
    if mode1 == '0': # position mode
        value1 = diagList[int(diagList[position + 1])]
    elif mode1 == '1': # immediate mode
        value1 = diagList[position + 1]

    mode2 = instruction[2]
    value2 = ''
    if mode2 == '0': # position mode
        value2 = diagList[int(diagList[position + 2])]
    elif mode2 == '1': # immediate mode
        value2 = diagList[position + 2]

    operationResult = 0
    if operation == '1':
        operationResult = int(value1) + int(value2)
    elif operation == '2':
        operationResult = int(value1) * int(value2)
    
    mode3 = '0'
    if len(instruction) > 3:
        mode3 = instruction[2]
    if mode3 == '0': # position mode
        diagList[int(diagList[position + 3])] = str(operationResult)
    elif mode3 == '1': # immediate mode
        diagList[position + 2] = str(operationResult)

    return position + 4